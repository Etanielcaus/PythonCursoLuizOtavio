from bs4 import BeautifulSoup
import requests

url = 'https://www.pstu.org.br/'

# Use o módulo 'requests' para buscar o conteúdo da URL
response = requests.get(url)

# Obtenha o conteúdo HTML da resposta
html_content = response.text

# Agora você pode usar o BeautifulSoup para analisar o conteúdo HTML
soup = BeautifulSoup(html_content, 'html.parser')

# print(soup.prettify())  # print the parsed data of html
# print(soup.title)
if soup.title is not None:
    print(soup.title.name)

# extrair o texto de uma tag
# for link in soup.find_all('a'):
#     print(link.get('href'))


print(soup.get_text())
