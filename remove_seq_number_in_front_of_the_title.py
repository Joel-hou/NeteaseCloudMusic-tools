# -*- coding: utf-8 -*-
# 删除歌曲名字前边的数字序号(应该是专辑中的吧。。。)
# zhian.h@qq.com
# python xxx.py

import io
import os
import sys

sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='utf-8')  # 改变标准输出的默认编码

path = "D:\\houzhian\\Music\\iTunes\\iTunes Media\\Music\\"


def isNumber(character):
    return True if (ord(character) >= 48 and ord(character) <= 57) else False


def findIndex(filename):
    index = 0
    for character in filename:
        if((ord(character) >= 48 and ord(character) <= 57) or character == '-' or character == ' '):
            index = index + 1
        else:
            break
    return index


def rename(path):
    filenames = os.listdir(path)
    for filename in filenames:
        # 思路，从左到右，删除至第一个非数字，非'-'的字母
        # 跳过纯数字名字的歌曲,如 90.mp3
        if(filename.isNumber):
            pass
        elif(isNumber(filename[0])):
            newfilename = filename[findIndex(filename): len(filename)]
            print(newfilename)
            try:
                os.rename(os.path.join(path, filename),
                          os.path.join(path, newfilename))
            except Exception as e:
                print(e)
                pass


if __name__ == '__main__':
    try:
        rename(path)
    except Exception as e:
        print(e)
        pass
