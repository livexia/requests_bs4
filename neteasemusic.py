#encoding=utf8
from NeteaseMusic.album import *
from NeteaseMusic.getinfo import *
from NeteaseMusic.mysql import *
from NeteaseMusic.urlparameter import *
import sys

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


if sys.argv[1] == 'playlist' or sys.argv[1] == 'artist_hot' or sys.argv[1] == 'album' or sys.argv[1] == 'artist_all':
    if sys.argv[1] == 'artist_all':
        urls = Album.album_url(sys.argv[2])
        flag1 = input("是否需要保存至mysql(y/n): ")
        flag2 = input("是否需要输出信息(y/n): ")
        for url in urls:
            #print(url)
            info = Getinfo.get_info(url)
            if flag1 == 'y':
                MySQL.insert_sql(info)
            if flag2 == 'y':
                print_info(info)
        print("爬取歌手id=" + sys.argv[2] + '所有歌曲成功')
    else:
        flag1 = input("是否需要保存至mysql(y/n): ")
        flag2 = input("是否需要输出信息(y/n): ")
        url = UrlParameter.base_url + sys.argv[1].split('_')[0] + '?id=' + sys.argv[2]
        info = Getinfo.get_info(url)
        if flag1 == 'y':
            MySQL.insert_sql(info)
        if flag2 == 'y':
            print_info(info)
        print("爬取" + sys.argv[1] + '=' + sys.argv[2] + '所有歌曲成功')
else:
    print('第一个参数错误，请检查单词拼写')
    exit()



