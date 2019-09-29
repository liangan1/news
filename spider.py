import requests
from bs4 import BeautifulSoup

class Spider:
    def __init__(self, url = ""):
	self.url = url
        self.menu_r = requests.get(self.url)
        self.soup = BeautifulSoup(self.menu_r.content, features='html.parser')
    
    def url(self):
	return self.url
   
    def menu_r(self):
	return self.menu_r

    def soup(self):
	return self.soup


