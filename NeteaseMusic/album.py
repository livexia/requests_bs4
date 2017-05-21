#encoding=utf8
import requests
import sys
import json
from bs4 import BeautifulSoup
from NeteaseMusic.urlparameter import UrlParameter
from NeteaseMusic.get404 import get_404


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
        # Album.album_dict = {}
        Album.album_url_list = []
        if get_404_album(Album.base_url):
            print(Album.base_url)
            print("该歌手不存在专辑")
        else:
            print(albums)
            for album in albums.children:
                if album != '\n':
                    album_id = album.find('a',{'class': 'msk'})['href'].split("=")[1]
                    # title = album.div['title']
                    # time = album.find('span', {'class': 's-fc3'}).text
                    # img = album.img['src']
                    # Album.album_dict[album_id] = [album_id, title, time, img]
                    Album.album_list.append(album_id)
        # list_album = Album.album_dict
        # for album in list_album:
        #     Album.album_url_list.append(album) #UrlParameter.album_base_url +

