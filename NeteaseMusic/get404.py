#encoding=utf8
import requests
from bs4 import BeautifulSoup
from NeteaseMusic.urlparameter import UrlParameter


def get_404(url):
    s = requests.session()
    s = BeautifulSoup(s.get(url,headers = UrlParameter.random_ua()).content, "lxml")

    pages = s.find('div', {'class': 'n-for404'})
    if(pages):
        # print(pages.find('p').text)
        # print(url)
        return 1
    else:
        return 0

def get_404_album(url):
    s = requests.session()
    s = BeautifulSoup(s.get(url,headers = UrlParameter.random_ua()).content, "lxml")

    pages = s.find('div', {'class': 'n-nmusic'})
    if(pages):
        # print(pages.find('p').text)
        # print(url)
        return 1
    else:
        return 0

