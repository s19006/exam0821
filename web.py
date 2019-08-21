import requests
from bs4 import BeautifulSoup

url = 'https://mojim.com/jph108196-A1.htm'
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

song=soup.select("span a")

c = 'python/siken/exam0821/web.txt'

with open("web.txt", mode='w',encoding="utf-8") as f:
    for i in song:
        f.write("{}\n".format(i.getText()))





