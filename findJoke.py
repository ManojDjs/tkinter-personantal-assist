#Find a joke

from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import re, random
import urllib.request

def tellAJoke():
	# open a connection to a URL using urllib
	# fh = open("hello.txt", "w")
	webUrl  = urllib.request.urlopen('http://www.laughfactory.com/jokes/latest-jokes')
	data = webUrl.read()
	soup = BeautifulSoup(data, "lxml", from_encoding="utf-8")
	raw_joke_list = soup.find_all('p', {'id':re.compile('joke_')})
	joke_list = []
	for joke in raw_joke_list:
		joke_list.append(joke.getText().strip())
		
	return joke_list[random.randint(0, len(joke_list) - 1)]