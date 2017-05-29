#encoding=utf8
from NeteaseMusic.album import *
from NeteaseMusic.artist import *
from NeteaseMusic.getinfo import *
from NeteaseMusic.mysql import *
from NeteaseMusic.urlparameter import *
from NeteaseMusic.general import *
from NeteaseMusic.multithreading import *
from NeteaseMusic.spider import *
import sys
import os

#
# def crawl_all_album(artist_id, flag1, flag2):
#     album_crawled = []
#     if os.path.getsize('album_queue.txt') == 0:
#         Album.crawl_album(artist_id)
#         album_list=Album.album_list
#         album_list.reverse()
#         create_data_files('album', UrlParameter.base_url)
#         truncate_file('album_crawled.txt')
#         list_to_file(Album.album_list, 'album_queue.txt')
#     else:
#         album_list = file_to_list('album_queue.txt')
#         album_list.reverse()
#         album_crawled = file_to_list('album_crawled.txt')
#     length = len(album_list)
#     while length>0:
#         length -= 1
#         album_id = album_list.pop()
#         url = UrlParameter.album_base_url + album_id
#         info = Getinfo.get_info(url)
#         # album_list.remove(album_id)
#         album_crawled.append(album_id)
#         list_to_file(album_list, 'album_queue.txt')
#         list_to_file(album_crawled, 'album_crawled.txt')
#         if flag1 == 'y':
#             MySQL.insert_sql(info)
#         if flag2 == 'y':
#             print_info(info)
#     truncate_file('album_queue.txt')
#     truncate_file('album_crawled.txt')
#     print("爬取歌手id=" + artist_id + '所有歌曲成功')
#
#
# def crawl_all_song(flag1, flag2, flag3, flag4):
#     if flag3 == 'y':
#         artist_crawled = []
#         if flag4 == 'y':
#             Artist.crawl_all_artist()
#             artist_list = Artist.artist_list
#             artist_list.reverse()
#             create_data_files('artist', UrlParameter.base_url)
#             truncate_file('artist_queue.txt')
#             truncate_file('artist_crawled.txt')
#             truncate_file('album_queue.txt')
#             truncate_file('album_crawled.txt')
#             list_to_file(artist_list, 'artist_queue.txt')
#         else:
#             artist_list = file_to_list('artist_queue.txt')
#             artist_list.reverse()
#             artist_crawled = file_to_list('artist_crawled.txt')
#         length = len(artist_list)
#         while length > 0:
#             length -= 1
#             artist_id = artist_list.pop()
#             crawl_all_album(artist_id, flag1, flag2)
#             # artist_list.remove(artist_id)
#             artist_crawled.append(artist_id)
#             list_to_file(artist_list, 'artist_queue.txt')
#             list_to_file(artist_crawled, 'artist_crawled.txt')
#             if length == 95:
#                 print("程序结束")
#                 exit(0);
#         truncate_file('artist_queue.txt')
#         truncate_file('artist_crawled.txt')
#         print('All song,done!')
#


def crawl_other(flag1='n',flag2='n'):
    url = UrlParameter.base_url + sys.argv[1].split('_')[0] + '?id=' + sys.argv[2]
    info = Getinfo.get_info(url)
    if flag1 == 'y':
        MySQL.insert_sql(info)
    if flag2 == 'y':
        print_info(info)
    print("爬取" + sys.argv[1] + '=' + sys.argv[2] + '所有歌曲成功')


if sys.argv[1] == 'playlist' or sys.argv[1] == 'artist_hot' or sys.argv[1] == 'album' or sys.argv[1] == 'artist_all' or sys.argv[1] == 'crawlall':
    if sys.argv[1] == 'artist_all':
        flag1 = input("是否需要保存至mysql(y/n 默认n): ")
        flag2 = input("是否需要输出信息(y/n 默认n): ")
        truncate_file(Spider.album_crawled_file)
        truncate_file(Spider.album_queue_file)
        truncate_file(Spider.artist_crawled_file)
        truncate_file(Spider.artist_queue_file)
        Spider(flag1,flag2)
        Spider.crawl_all_album(sys.argv[2])
        Spider.album_process_queue()
    elif sys.argv[1] == 'crawlall':
        # flag1 = input("是否需要保存至mysql(y/n 默认n): ")
        # flag2 = input("是否需要输出信息(y/n 默认n): ")
        # flag3 = input("确认是否爬取所有歌曲，这将耗费大量时间，运行过程中可能会出现程序未响应(y/n 默认n): ")
        # flag4 = input('是否从头开始爬取(y/n 默认n): ')
        flag1 = flag2 = 'n'
        flag3 = flag4 = 'y'
        create_workers()
        Spider(flag1,flag2,flag3,flag4)
        Spider.crawl_all_song()
        crawl(Spider.artist_queue_file)
    else:
        flag1 = input("是否需要保存至mysql(y/n 默认n): ")
        flag2 = input("是否需要输出信息(y/n 默认n): ")
        crawl_other(flag1,flag2)
else:
    print('第一个参数错误，请检查单词拼写')
    exit()



