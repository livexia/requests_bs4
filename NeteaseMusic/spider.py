#encoding=utf8
from NeteaseMusic.album import *
from NeteaseMusic.artist import *
from NeteaseMusic.getinfo import *
from NeteaseMusic.mysql import *
from NeteaseMusic.urlparameter import *
from NeteaseMusic.general import *
from queue import Queue
import sys
import os


class Spider:

    flag1 = ''
    flag2 = ''
    flag3 = ''
    flag4 = ''

    artist_crawled = ['test']
    artist_queue = ['test']
    artist_crawled_file = 'artist_crawled.txt'
    artist_queue_file = 'artist_queue.txt'
    album_crawled = ['test']
    album_queue = ['test']
    album_crawled_file = 'album_crawled.txt'
    album_queue_file = 'album_queue.txt'
    
    def __init__(self, flag1='y', flag2='y', flag3='y', flag4='y'):
        Spider.flag1 = flag1
        Spider.flag2 = flag2
        Spider.flag3 = flag3
        Spider.flag4 = flag4

    @staticmethod
    def crawl_all_song():
        if Spider.flag3 == 'y':
            if Spider.flag4 == 'y':
                Artist.crawl_all_artist()
                Spider.artist_crawled = []
                Spider.artist_queue = Artist.artist_queue
                Spider.artist_queue.reverse()
                create_data_files('artist', UrlParameter.base_url)
                truncate_file(Spider.album_queue_file)
                truncate_file(Spider.album_crawled_file)
                truncate_file(Spider.artist_queue_file)
                truncate_file(Spider.artist_crawled_file)
                list_to_file(Spider.artist_queue, Spider.artist_queue_file)
            else:
                Spider.artist_queue = file_to_list(Spider.artist_queue_file)
                Spider.artist_queue.reverse()
                Spider.artist_crawled = file_to_list(Spider.artist_crawled_file)

    @staticmethod
    def crawl_all_album(artist_id):
        if os.path.getsize(Spider.album_queue_file) == 0:
            Album.crawl_album(artist_id)
            Spider.album_queue = Album.album_queue
            Spider.album_queue.reverse()
            create_data_files('album', UrlParameter.base_url)
            truncate_file(Spider.album_crawled_file)
            list_to_file(Album.album_queue, Spider.album_queue_file)
        else:
            Spider.album_queue = file_to_list(Spider.album_queue_file)
            Spider.album_queue.reverse()
            Spider.album_crawled = file_to_list(Spider.album_crawled_file)
        Spider.album_process_queue()

    @staticmethod
    def artist_process_queue():
        while True:
            if not Spider.artist_queue:
                break
            artist_id = Spider.artist_queue.pop()
            Spider.crawl_all_album(artist_id)
            Spider.artist_crawled.append(artist_id)
            list_to_file(Spider.artist_queue, Spider.artist_queue_file)
            list_to_file(Spider.artist_crawled, Spider.artist_crawled_file)
            print("爬取歌手id=" + artist_id + '所有歌曲成功')
            print(len(Spider.artist_queue))
                # exit(0);

    @staticmethod
    def album_process_queue():
        while True:
            if not Spider.album_queue:
                break
            while Spider.album_queue:
                album_id = Spider.album_queue.pop()
                url = UrlParameter.album_base_url + album_id
                info = Getinfo.get_info(url)
                Spider.album_crawled.append(album_id)
                list_to_file(Spider.album_queue, Spider.album_queue_file)
                list_to_file(Spider.album_crawled, Spider.album_crawled_file)
                if Spider.flag1 == 'y':
                    MySQL.insert_sql(info)
                if Spider.flag2 == 'y':
                    print_info(info)
                print(len(Spider.album_queue))
            truncate_file(Spider.album_crawled_file)
            truncate_file(Spider.album_queue_file)


