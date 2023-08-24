# -*- coding: utf-8 -*-

from django.shortcuts import render


class HitCounterViewMixin(object):
    def get_object(self, *args, **kwargs):
        try:
            super(HitCounterViewMixin, self).get_object(*args, **kwargs)
        except AttributeError:
            raise NotImplementedError

    def dispatch(self, request, *args, **kwargs):
        response = super(HitCounterViewMixin, self).dispatch(request,
                                                           *args, **kwargs)
        if 200 <= response.status_code < 300:
            obj = self.get_object()
            if obj: obj.hit(request)
        return response
