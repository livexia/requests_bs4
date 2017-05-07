import requests
import sys
import json
from bs4 import BeautifulSoup
from spider import *


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
        s = BeautifulSoup(s.get(Album.base_url,headers = Spider.headers).content, "lxml")
        albums = s.find('ul',{'data-id':artist_id})

        list_album = {}
        for album in albums.children:
            if album != '\n':
                id = album.find('a',{'class':'msk'})['href']
                #id = id.split("=")[1]
                title = album.div['title']
                time = album.find('span',{'class':'s-fc3'}).text
                img = album.img['src']
                #print(id,time,title,img)
                list_album[id.split("=")[1]]=[id,title,time,img]
        #print(list_album)
        return list_album

list_album=Album.crawl_album(13193)

for album in list_album:
    url = 'http://music.163.com' + list_album[album][0]
    print(url)

