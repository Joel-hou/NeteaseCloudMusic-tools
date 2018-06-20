# -*- coding: utf-8 -*-
# 用于将各专辑文件夹下的歌曲文件搬到同一个文件夹里边, 使用前请把 neteaseMusicPath 改成自己电脑上的路径
# 特别注意路径末尾的 \\
# zhian.h@qq.com
# python flat_music.py

import io
import os
import sys
import shutil

sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='utf-8')  # 改变标准输出的默认编码

neteaseMusicPath = "D:\\houzhian\\Music\\iTunes\\iTunes Media\\Music\\"
outputPath = "D:\\houzhian\\Music\\iTunes\\iTunes Media\\output\\"


def stealFile(path, outputPath):
    for roots, dirs, files in os.walk(path):
        for file in files:
            try:
                shutil.move(os.path.join(roots, file), outputPath)
                print(os.path.join(roots, file))
            except Exception as e:
                print(e)
                pass
        for dir in dirs:
            stealFile(dir, outputPath)


if __name__ == '__main__':
    stealFile(neteaseMusicPath, outputPath)
