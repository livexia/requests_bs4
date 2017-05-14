#encoding=utf8
import requests
import sys
import json
from bs4 import BeautifulSoup
from NeteaseMusic.urlparameter import UrlParameter


class Album:

    author_id = ''
    base_url = ''

    def __init__(self, author_id, base_url):
        Album.author_id = author_id
        Album.base_url = base_url

    @staticmethod
    def crawl_album(artist_id):
        Album.base_url = 'http://music.163.com/artist/album?id=' + str(artist_id) + '&limit=1200&offset=0'
        s = requests.session()
        s = BeautifulSoup(s.get(Album.base_url,headers = UrlParameter.random_ua()).content, "lxml")
        albums = s.find('ul',{'data-id': artist_id})
        list_album = {}
        try:
            for album in albums.children:
                if album != '\n':
                    id = album.find('a',{'class': 'msk'})['href'].split("=")[1]
                    title = album.div['title']
                    time = album.find('span', {'class':'s-fc3'}).text
                    img = album.img['src']
                    list_album[id] = [id, title, time, img]
        except AttributeError:
            print("该歌手不存在专辑")
            list_album = {}
        return list_album

    @staticmethod
    def album_url(artist_id):
        urls = []
        list_album = Album.crawl_album(artist_id)
        for album in list_album:
            urls.append(UrlParameter.album_base_url + album)
        return urls
