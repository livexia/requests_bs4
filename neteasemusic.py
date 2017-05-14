#encoding=utf8
from NeteaseMusic.album import *
from NeteaseMusic.artist import *
from NeteaseMusic.getinfo import *
from NeteaseMusic.mysql import *
from NeteaseMusic.urlparameter import *
import sys


def crawl_all_album(artist_id,flag1 = 'n',flag2 = 'n'):
    urls = Album.album_url(artist_id)
    for url in urls:
        info = Getinfo.get_info(url)
        if flag1 == 'y':
            MySQL.insert_sql(info)
        if flag2 == 'y':
            print_info(info)
    print("爬取歌手id=" + artist_id + '所有歌曲成功')


def crawl_all_song(flag1='n', flag2='n', flag3='n'):
    if flag3 == 'y':
        list_artist = Artist.crawl_all_artist()
        for key in list_artist:
            crawl_all_album(key, flag1, flag2)


def crawl_other(flag1='n',flag2='n'):
    url = UrlParameter.base_url + sys.argv[1].split('_')[0] + '?id=' + sys.argv[2]
    info = Getinfo.get_info(url)
    if flag1 == 'y':
        MySQL.insert_sql(info)
    if flag2 == 'y':
        print_info(info)
    print("爬取" + sys.argv[1] + '=' + sys.argv[2] + '所有歌曲成功')


def print_info(info):
    for key in info:
        print('歌曲id：', key)
        print('     歌曲标题：'+info[key][0])
        print('     歌手：'+info[key][1])
        print('     歌手id：', info[key][2])
        print('     专辑：'+info[key][3])
        print('     专辑id：', info[key][4])
        print('     Url：')
        print('          歌曲链接：'+info[key][5][0])
        print('          歌手链接：'+info[key][5][1])
        print('          专辑链接：'+info[key][5][2])
        print('          专辑图片：', info[key][5][3])


if sys.argv[1] == 'playlist' or sys.argv[1] == 'artist_hot' or sys.argv[1] == 'album' or sys.argv[1] == 'artist_all' or sys.argv[1] == 'crawlall':
    if sys.argv[1] == 'artist_all':
        flag1 = input("是否需要保存至mysql(y/n 默认n): ")
        flag2 = input("是否需要输出信息(y/n 默认n): ")
        crawl_all_album(sys.argv[2],flag1,flag2)
    elif sys.argv[1] == 'crawlall':
        flag1 = input("是否需要保存至mysql(y/n 默认n): ")
        flag2 = input("是否需要输出信息(y/n 默认n): ")
        flag3 = input("确认是否爬取所有歌曲，这将耗费大量时间，运行过程中可能会出现程序未响应(y/n 默认n): ")
        crawl_all_song(flag1,flag2,flag3)
    else:
        flag1 = input("是否需要保存至mysql(y/n 默认n): ")
        flag2 = input("是否需要输出信息(y/n 默认n): ")
        crawl_other(flag1,flag2)
else:
    print('第一个参数错误，请检查单词拼写')
    exit()



