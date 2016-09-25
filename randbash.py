from bottle import route, run, template
from random import choice
from bs4 import BeautifulSoup
import requests


@route('/')
def index():
        url = 'http://bash.im/random' #get page with random quotes of bash.im
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        quotes = soup.findAll("div", {"class":"text"}) #prepare list of quotes
        return str(choice(quotes)).replace('<br/>', '\n').replace('<div class="text">', '').replace('</div>', '')#get random quote and clean data

run(host='127.0.0.1', port=8000)

