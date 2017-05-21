#encoding=utf8
import requests
from bs4 import BeautifulSoup
from NeteaseMusic.urlparameter import UrlParameter
from NeteaseMusic.get404 import get_404


class Artist:

    author_id = ''
    base_url = ''
    # artist_dict = {}
    artist_list = []

    def __init__(self, author_id, base_url):
        Artist.author_id = author_id
        Artist.base_url = base_url

    @staticmethod
    def crawl_all_artist():
        url_id = [1001,1002,1003,2001,2002,2003,6001,6002,6003,7001,7002,7003,4001,4002,4003]
        initial=[]
        for i in range(65,91):
            initial.append(i)
        initial.append(0)
        Artist.artist_dict = {}
        Artist.artist_url_list = []
        for key1 in url_id:
            for key2 in initial:
                Artist.base_url = 'http://music.163.com/discover/artist/cat?id='+ str(key1) + '&initial=' + str(key2)
                s = requests.session()
                s = BeautifulSoup(s.get(Artist.base_url,headers = UrlParameter.random_ua()).content, "lxml")
                albums = s.find('ul',{'id': 'm-artist-box'})

                for artist in albums.children:
                    if artist != '\n':
                        artist_id = artist.find('a',{'class': 's-fc0'})['href'].split("=")[1]
                        Artist.artist_list.append(artist_id)
        print("Artist,done!")
