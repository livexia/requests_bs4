#encoding=utf8
import requests
from bs4 import BeautifulSoup
from NeteaseMusic.urlparameter import UrlParameter


class Artist:

    author_id = ''
    base_url = ''

    def __init__(self, author_id, base_url):
        Artist.author_id = author_id
        Artist.base_url = base_url

    @staticmethod
    def crawl_all_artist():
        id=[1001,1002,1003,2001,2002,2003,6001,6002,6003,7001,7002,7003,4001,4002,4003]
        initial=[]
        for i in range(65,91):
            initial.append(i)
        initial.append(0)
        list_artist = {}
        for key1 in id:
            for key2 in initial:
                Artist.base_url = 'http://music.163.com/discover/artist/cat?id='+ str(key1) + '&initial=' + str(key2)
                # print (Artist.base_url)
                s = requests.session()
                s = BeautifulSoup(s.get(Artist.base_url,headers = UrlParameter.random_ua()).content, "lxml")
                albums = s.find('ul',{'id':'m-artist-box'})

                for artist in albums.children:
                    if artist != '\n':
                        id = artist.find('a',{'class':'s-fc0'})['href'].split("=")[1]
                        name = artist.find('a',{'class':'s-fc0'}).text
                        list_artist[id]=[id,name]
        # print(list_artist)
        return list_artist

    @staticmethod
    def artist_info(artist_id):
        return 0;

    @staticmethod
    def crawl_all_artist_url():
        urls = []
        list_artist = Artist.crawl_all_artist()
        for artist in list_artist:
            urls.append(UrlParameter.artist_base_url + artist)
            print(urls)
        return urls
