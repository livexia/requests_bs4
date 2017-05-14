# requests_bs4
一些利用requests+bs4写的python 脚本

结构目录

    requests_bs4
    ├── NeteaseMusic
    │   ├── album.py //爬取指定歌手的所有专辑
    │   ├── artist.py //爬取所有歌手
    │   ├── getinfo.py //爬取指定专辑、歌单、歌手的热门50单曲
    │   ├── mysql.py //数据存入mysql
    │   └── urlparameter.py //连接参数，headers......
    ├── README.md
    └── neteasemusic.py  //程序入口

neteasemusic.py 

获取网易云音乐歌单信息。必要参数歌单id

使用方式：
$ python netease_music.py < playlist/artist_hot/artist_all/album > < 对应id >

$ python netease_music.py crawlall  //爬取所有歌曲（不完全正常工作）
当第一个参数为artist_hot时第二个参数填写歌手id，会输出或者在数据库中保存该歌手热门50单曲

当第一个参数为artist_all时第二个参数填写歌手id，会输出或者在数据库中保存该歌手所有专辑中的歌曲
