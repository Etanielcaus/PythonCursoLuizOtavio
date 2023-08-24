# -*- coding: utf8 -*-

import os
import re
import string
import codecs
import math

from stemming.porter2 import stem
from repoze.lru import lru_cache


SPLIT_RE = re.compile(r'[\n\r\s\t' + string.punctuation + ']')
EMAIL_RE = re.compile(r"<?(mailto:)?[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*>?")
URL_RE = re.compile(r'https?://[^ \t\r\n\<]+')

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')


# cached version of stem
#   maxsize 4096 will use about 128 kb of memory
stem = lru_cache(maxsize=4096)(stem)

class Etiquetador(object):
    def __init__(self, word_min_size=2, min_occurrences=0,
                 max_tags=None, weight_range=None, stopwords=None):

        self.word_min_size = word_min_size
        self.min_occurrences = min_occurrences
        self.max_tags = max_tags
        self.weight_range = weight_range

        self.init_tags()
        self.init_stopwords(stopwords)

    def init_stopwords(self, stopwords):
        stopwords_file_path = os.path.join(DATA_DIR, 'stop_ptbr.txt')
        stopwords_f = codecs.open(stopwords_file_path, 'r', 'utf-8')
        self.stopwords = [word.strip() for word in stopwords_f.readlines()]
        stopwords_f.close()

        if stopwords:
            self.stopwords.extend(stopwords)

    def init_tags(self):
        tags_file_path = os.path.join(DATA_DIR, 'tags_ptbr.txt')
        tag_file = codecs.open(tags_file_path, 'r', 'utf8')

        self.tags = {}
        for line in tag_file:
            line = line.strip()
            key, value = line.split(' ', 1)
            self.tags[key] = value.split(' ')

        tag_file.close()

    def prepare_text(self, text):
        text, n = EMAIL_RE.subn('', text)
        text, n = URL_RE.subn('', text)
        return text

    def is_valid_token(self, token, stemmed_token):
        if not token:
            return False
        elif token in self.stopwords or stemmed_token in self.stopwords:
            return False
        elif token.isdigit():
            return False
        elif len(token) < self.word_min_size:
            return False

        if stemmed_token in self.tags:
            tags = self.tags[stemmed_token]
        elif token in self.tags:
            tags = self.tags[token]
        else:
            return True

        must_have = [u'N', u'N|EST']
        if not any(tag in tags for tag in must_have):
            return False

        cant_have = [u'NPROP', u'V', u'K', u'KC', u'KS']
        if any(tag in tags for tag in cant_have):
            return False

        return True

    def normalize(self, items, new_range):
        if not items:
            return items

        key_func = lambda x: x[1]

        old_min = min(items, key=key_func)[1]
        old_max = max(items, key=key_func)[1]

        new_min, new_max = new_range

        if old_min == old_max:
            return items

        elif old_min >= new_min and old_max <= new_max:
            return items

        # From: http://stackoverflow.com/questions/1471370/normalizing-from-0-5-1-to-0-1#answer-1477265
        #          (D-C)*(X-A)
        #   X' =   -----------  + C
        #             (B-A)
        #
        #   A = old_min, B = old_max
        #   C = new_min, D = new_max

        for item in items:
            n = item[1]
            item[1] = int((new_max - new_min) * (n - old_min) / \
                         (old_max - old_min)) + new_min

        return items

    def __call__(self, text):
        text = self.prepare_text(text)
        tokens = SPLIT_RE.split(text)
        token_count = {}

        for token in tokens:
            stemmed_token = stem(token.lower())
            if not self.is_valid_token(token, stemmed_token):
                continue

            if token_count.has_key(stemmed_token):
                token_count[stemmed_token][0] += 1
                if len(token_count[stemmed_token][1]) > len(token):
                    token_count[stemmed_token][1] = token.lower()
            else:
                token_count[stemmed_token] = [1, token.lower()]

        token_count = sorted(token_count.items(),
                             key=lambda x: x[1][0], reverse=True)

        tokens_weight = []
        for stemmed, (count, token) in token_count:
            if count >= self.min_occurrences:
                log = int(round(math.log(count, 2)))
                tokens_weight.append([token, log])

            if len(tokens_weight) == self.max_tags:
                break

        if self.weight_range:
            tokens_weight = self.normalize(tokens_weight,
                                           self.weight_range)

        return tokens_weight
