# -*- coding: utf-8 -*-
# 下载网易云音乐的收费歌曲, 原理就是从，缓存文件里边拿出来~ 没什么意思，不是无损的, 还是买ＶＩＰ
# zhian.h@qq.com
# python xxx.py

import os
import shutil

cache_file_name=os.path.expanduser('~')+"/AppData/Local/Netease/CloudMusic/cache_path"
buf=bytearray(os.path.getsize(cache_file_name))
with open (cache_file_name,'rb') as f:
    f.readinto(buf)
cache_path=buf.decode('utf-8').replace('\0','')
print("your download cache folder path is %s"%(cache_path))
print("now close your netease cloud music client we will clean the cache folder")
try:
    shutil.rmtree(cache_path)
except Exception as e:
    print(e)
    pass

print("clean cache folder finished")
print("back to your netease music client and start to listen to the song")
print("make sure that your songs has been fully cached")

input("press ENTER if you are ready")

if os.path.exists(cache_path)==False:
    os.mkdir(cache_path)
os.chdir(cache_path)
files = os.listdir(os.getcwd())
for f in files:
    file_name, file_extname = f.split('.')
    if file_extname == 'uc':
        os.rename(f, '%s.mp3' %file_name)
print("finished! now upload the song to your cloud disk manually")
