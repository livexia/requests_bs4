#encoding=utf8
import requests
import json
import sys
from bs4 import BeautifulSoup
from NeteaseMusic.urlparameter import UrlParameter


class Getinfo:

    @staticmethod
    def get_info(url):
        s = requests.session()
        s = BeautifulSoup(s.get(url,headers = UrlParameter.random_ua()).content, "lxml")
        print(UrlParameter.random_ua())
        musics = json.loads(s.find('textarea',{'style':'display:none;'}).text)
        info = {}
        for music in musics:
            song_id = music['id']
            title = music['name']
            author = music['artists'][0]['name']
            author_id = music['artists'][0]['id']
            album = music['album']['name']
            album_id = music['album']['id']
            album_pic_url = music['album']['picUrl']
            song_url = 'http://music.163.com/song?id=' + str(song_id)
            author_url = 'http://music.163.com/artist?id=' + str(author_id)
            album_url = 'http://music.163.com/album?id=' + str(album_id)
            info[song_id]=[title,author,author_id,album,album_id,[song_url,author_url,album_url,album_pic_url]]
        return info
