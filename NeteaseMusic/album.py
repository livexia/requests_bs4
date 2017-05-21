#encoding=utf8
import requests
import sys
import json
from bs4 import BeautifulSoup
from NeteaseMusic.urlparameter import UrlParameter
from NeteaseMusic.get404 import *


class Album:

    author_id = ''
    base_url = ''
    # album_dict = {}
    album_list = []

    def __init__(self, author_id, base_url):
        Album.author_id = author_id
        Album.base_url = base_url

    @staticmethod
    def crawl_album(artist_id):
        Album.base_url = 'http://music.163.com/artist/album?id=' + str(artist_id) + '&limit=10000&offset=0'
        s = requests.session()
        s = BeautifulSoup(s.get(Album.base_url, headers=UrlParameter.random_ua()).content, 'lxml')
        albums = s.find('ul', {'data-id': artist_id})
        Album.album_url_list = []
        if get_404_album(Album.base_url):
            print("该歌手不存在专辑")
        else:
            for album in albums.children:
                if album != '\n':
                    album_id = album.find('a',{'class': 'msk'})['href'].split("=")[1]
                    Album.album_list.append(album_id)

