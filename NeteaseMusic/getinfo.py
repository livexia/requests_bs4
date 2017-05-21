#encoding=utf8
import requests
import json
import sys
from bs4 import BeautifulSoup
from NeteaseMusic.urlparameter import UrlParameter
from NeteaseMusic.get404 import get_404


class Getinfo:

    @staticmethod
    def get_info(url):
        s = requests.session()
        s = BeautifulSoup(s.get(url,headers = UrlParameter.random_ua()).content, "lxml")
        info = {}
        if get_404(url):
            print("不存在歌曲")
            return info;
        # try:
        else:
            musics = json.loads(s.find('textarea',{'style': 'display:none;'}).text)
        # except json.decoder.JSONDecodeError:
        #     print("该专辑不存在歌曲")
        #     return info;
        for music in musics:
            song_id = music['id']
            title = music['name']
            author = music['artists'][0]['name']
            author_id = music['artists'][0]['id']
            album = str(music['album']['name'])
            album_id = music['album']['id']
            album_pic_url = music['album']['picUrl']
            song_url = 'http://music.163.com/song?id=' + str(song_id)
            author_url = 'http://music.163.com/artist?id=' + str(author_id)
            album_url = 'http://music.163.com/album?id=' + str(album_id)
            info[song_id]=[title,author,author_id,album,album_id,[song_url,author_url,album_url,album_pic_url]]
            # print(info[song_id][3])
        return info
