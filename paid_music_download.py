#coding: utf-8

# author: houzhian@gmail.com
# python required, tested in python3,win10
# warning: 支持正版，仅供测试
# usage:

import os
import shutil

# get cache_path from netease music config file
cache_file_name=os.path.expanduser('~')+"/AppData/Local/Netease/CloudMusic/cache_path"
buf=bytearray(os.path.getsize(cache_file_name))
with open (cache_file_name,'rb') as f:
    f.readinto(buf)
cache_path=buf.decode('utf-8').replace('\0','')
print("your download cache folder path is %s"%(cache_path))
print("now close your netease cloud music client we will clean the cache folder")
try:
    pass
    shutil.rmtree(cache_path)
except Exception as e:
    print(e)
print("clean cache folder finished")
print("back to your netease music client and start to listen the song to be downloaded")
print("please make sure that your songs has been fully cached")
input("please press enter if you are ready")

if os.path.exists(cache_path)==False:
    os.mkdir(cache_path)
os.chdir(cache_path)
files = os.listdir(os.getcwd())
for f in files:
    file_name, file_extname = f.split('.')
    if file_extname == 'uc':
        os.rename(f, '%s.mp3' %file_name)
print("finished! now upload these songs to your cloud music disk manually")
