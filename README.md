# requests_bs4
一些利用requests+bs4写的python 脚本

结构目录

    requests_bs4
    ├── NeteaseMusic
    │   ├── album.py
    │   ├── getinfo.py
    │   ├── mysql.py
    │   └── urlparameter.py
    ├── README.md
    └── neteasemusic.py

neteasemusic.py 

获取网易云音乐歌单信息。必要参数歌单id

使用方式：$ python netease_music.py < playlist/artist_hot/artist_all/album > < 对应id >

当第一个参数为artist_hot时第二个参数填写歌手id，会输出或者在数据库中保存该歌手热门50单曲

当第一个参数为artist_all时第二个参数填写歌手id，会输出或者在数据库中保存该歌手所有专辑中的歌曲
