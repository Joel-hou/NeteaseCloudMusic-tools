#coding: utf-8

# author: houzhian@gmail.com
# python required, tested in python3,win10
# warning: 支持正版，仅供测试
# usage:

import os

# get cache_path from netease music config file
cache_file_name=os.path.expanduser('~')+"/AppData/Local/Netease/CloudMusic/cache_path"
buf=bytearray(os.path.getsize(cache_file_name))
with open (cache_file_name,'rb') as f:
    f.readinto(buf)
cache_path=buf.decode('utf-8')
print(cache_path)
print(cache_path.replace('\0', ''))
