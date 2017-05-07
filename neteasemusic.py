#encoding=utf8
from NeteaseMusic.album import *
from NeteaseMusic.getinfo import *
from NeteaseMusic.mysql import *
from NeteaseMusic.urlparameter import *
import sys

def Printinfo(info):
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
        print('          专辑图片：'+info[key][5][3])

def InsertMySQL(info):
    flag = input("是否需要保存至mysql(y/n): ")
    if flag == 'y':
        MySQL.insertsql(info)
        print("存入mysql成功")
    else:
        print("没有存入mysql")

    list_album=Album.crawl_album(13193)

    for album in list_album:
        url = UrlParameter.base_url + list_album[album][0]
        print(url)

if sys.argv[1] == 'playlist' or sys.argv[1] == 'artist_hot' or sys.argv[1] == 'album' or sys.argv[1] == 'artist_all':
    play_url = UrlParameter.base_url + sys.argv[1].split('_')[0] + '?id=' + sys.argv[2]
    if sys.argv[1] == 'artist_all':
        urls = Album.album_url(sys.argv[2])
        for url in urls:
            info = Getinfo.get_info(url)
            Printinfo(info)
else:
    print('第一个参数错误，请检查单词拼写')
    exit()



