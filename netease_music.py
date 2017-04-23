#encoding=utf8

import requests
import json
import sys
from bs4 import BeautifulSoup
import pymysql


def getinfo(play_url):
    s = requests.session()
    s = BeautifulSoup(s.get(play_url,headers = headers).content, "lxml")
    judge = s.find('class',{'class':'n-for404'})
    if judge != '':
        print("输入id有误，请检查")
        exit()
    else:
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


def insertsql(info):
    #修改你的mysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='XGCxiagu0cha0515', db='NeteaseMusic')
    cur = conn.cursor()
    for key in info:
        cur.execute("REPLACE into song values(%s,%s,%s,%s)",
                    (key, info[key][0].encode('utf-8'), info[key][2], info[key][4]))
        cur.execute("REPLACE into author values(%s,%s)",
                    (info[key][2], info[key][1].encode('utf-8')))
        cur.execute("REPLACE into album values(%s,%s,%s)",
                    (info[key][4], info[key][3].encode('utf-8'), info[key][5][3].encode('utf-8')))

    conn.commit()
    cur.close()
    conn.close()


headers = {
    'Referer':'http://music.163.com/',
    'Host':'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


play_url = 'http://music.163.com/'
if sys.argv[1] == 'playlist' or sys.argv[1] == 'artist' or sys.argv[1] == 'album':
    play_url = play_url + sys.argv[1] + '?id=' + sys.argv[2]
else:
    print('第一个参数错误，请检查单词拼写')
    exit()


info = getinfo(play_url)

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

flag = input("是否需要保存至mysql(y/n): ")
if flag == 'y':
    insertsql(info)
    print("存入mysql成功")
else:
    print("没有存入mysql")
