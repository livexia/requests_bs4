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
        album = music['album']['name']
        album_id = music['album']['id']
        album_picurl = music['album']['picUrl']
        list[song_id]=[title,author,album,album_id,album_picurl]
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
    print('     歌曲标题'+list[key][0])
    print('     作者：'+list[key][1])
    print('     专辑：'+list[key][2])
    print('     专辑id：',list[key][3])
    print('     专辑图片：'+list[key][4])


