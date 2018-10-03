import requests
import re
from bs4 import BeautifulSoup
r = requests.get("https://www.sinonimos.com.br/previdencia/")
html = r.text
parsed_html = BeautifulSoup(html)
desc = parsed_html.findAll(attrs={"property": re.compile(r"og:description", re.I)}) 
words = desc[0]['content']
words = words.split(':')[1]
words = words.split('.')[0]
sinonimos = words.replace(' ', '').split(',').lower()
print(sinonimos)