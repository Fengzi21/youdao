import sys
import requests

from rich import print
from bs4 import BeautifulSoup


word_in = sys.argv[1]
web_url = 'https://dict.youdao.com/w/eng/{}/'
word_url = web_url.format(word_in)

rep = requests.get(word_url)
soup = BeautifulSoup(rep.text, 'lxml')

collins = soup.find(id="collinsResult")
# print(collins.prettify())

header = collins.find('h4')
# print(header.prettify())

word, phonetic, *_ = list(header.stripped_strings)
print(word, phonetic)

meanings = collins.find(class_='ol')
# print(meanings.prettify())

for item in meanings.find_all('li'):
    tran = item.find(class_='collinsMajorTrans')
    print(tran.prettify())
    print(list(tran.strings))
    m = list(tran.stripped_strings)
    meaning = '{} [bold green]{}[/] - {}'.format(*m[:2], ' '.join(m[2:]))
    print(meaning)

    example_list = item.find(class_='exampleLists')
    if example_list is not None:
        print(example_list.prettify())
        e = example_list.stripped_strings
        example = '{} {}\n{}'.format(*e)
        print(example)
