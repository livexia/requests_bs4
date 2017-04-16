#encoding=utf8

import requests
import json
import sys
from bs4 import BeautifulSoup


def getlist(play_url):
    s = requests.session()
    s = BeautifulSoup(s.get(play_url,headers = headers).content, "lxml")
    musics = json.loads(s.find('textarea',{'style':'display:none;'}).text)
    for music in musics:
        song_id = music['id']
        title = music['name']
        author = music['artists'][0]['name']
        album_id = music['album']['id']
        album = music['album']['name']
        album_picurl = music['album']['picUrl']
        print('歌曲标题：{}   歌手：{}    专辑：{}'.format(title,author,album))


headers = {
    'Referer':'http://music.163.com/',
    'Host':'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
# play_url = 'http://music.163.com/playlist?id='

play_url = 'http://music.163.com/playlist?id=' + sys.argv[1]
getlist( play_url)


