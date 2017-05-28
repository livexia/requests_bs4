#encoding=utf8
from NeteaseMusic.album import *
from NeteaseMusic.artist import *
from NeteaseMusic.getinfo import *
from NeteaseMusic.mysql import *
from NeteaseMusic.urlparameter import *
from NeteaseMusic.general import *
from NeteaseMusic.spider import *
from queue import Queue
import sys
import os
import threading
import time


NUMBER_OF_THREADS = 5
queue = Queue()


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        id = queue.get()
        Spider.artist_process_queue()
        queue.task_done()


def create_jobs(file):
    for link in file_to_list(file):
        queue.put(link)
    queue.join()
    crawl(file)


def crawl(file):
    queued_links = file_to_list(file)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs(file)


create_workers()
Spider('n','n','y','y')
Spider.crawl_all_song()
crawl(Spider.artist_queue_file)