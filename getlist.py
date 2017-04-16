#encoding=utf8

import requests
import json
import sys
from bs4 import BeautifulSoup


def getlist(play_url):
    s = requests.session()
    s = BeautifulSoup(s.get(play_url,headers = headers).content, "lxml")
    musics = json.loads(s.find('textarea',{'style':'display:none;'}).text)
    list = {}
    for music in musics:
        song_id = music['id']
        title = music['name']
        author = music['artists'][0]['name']
        author_id = music['artists'][0]['id']
        album = music['album']['name']
        album_id = music['album']['id']
        album_picurl = music['album']['picUrl']
        song_url = 'http://music.163.com/song?id=' + str(song_id)
        author_url = 'http://music.163.com/artist?id=' + str(author_id)
        album_url = 'http://music.163.com/album?id=' + str(album_id)
        list[song_id]=[title,author,author_id,album,album_id,[song_url,author_url,album_url,album_picurl]]
    return list


headers = {
    'Referer':'http://music.163.com/',
    'Host':'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
# play_url = 'http://music.163.com/playlist?id='

play_url = 'http://music.163.com/playlist?id=' + sys.argv[1]
list = getlist( play_url)
for key in list:
    print('歌曲id：',key)
    print('     歌曲标题：'+list[key][0])
    print('     歌手：'+list[key][1])
    print('     歌手id：',list[key][2])
    print('     专辑：'+list[key][3])
    print('     专辑id：',list[key][4])
    print('     Url：')
    print('          歌曲链接：'+list[key][5][0])
    print('          歌手链接：'+list[key][5][1])
    print('          专辑链接：'+list[key][5][2])
    print('          专辑图片：'+list[key][5][3])


