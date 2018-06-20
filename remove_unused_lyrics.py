# -*- coding: utf-8 -*-
# 删除歌曲不存在的歌词
# zhian.h@qq.com
# python xxx.py, remeber to change Music to your directory

import os


def findLyric(lyricName):
    content = os.listdir(os.getcwd())
    for item in content:
        if(lyricName == item):
            return True
    return False


def do():
    os.chdir('Music')
    content = os.listdir(os.getcwd())
    count = 0
    for item in content:
        if(item.find('lrc') != -1):
            songName1 = item.replace('lrc', 'mp3')
            songName2 = item.replace('lrc', 'flac')
            songName3 = item.replace('lrc', 'ape')
            if(findLyric(songName1) == False and findLyric(songName2) == False and findLyric(songName3) == False):
                print(os.getcwd()+'\\'+item)
                os.remove(os.getcwd()+'\\'+item)
                count += 1
    print('succeed ! 删除了 %d 个条目' % count)


if __name__ == '__main__':
    do()
