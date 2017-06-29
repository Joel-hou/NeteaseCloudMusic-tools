
import os

def theSongExistCurrentFolder(songName):
    content=os.listdir(os.getcwd())
    existFlag=False
    for item in content:
        if(songName==item):
            existFlag=True
            break;
    return existFlag

os.chdir('Music')
content=os.listdir(os.getcwd())
count=0
for item in content:
    if(item.find('lrc') != -1):
        songName1=item.replace('lrc','mp3')
        songName2=item.replace('lrc','flac')
        songName3=item.replace('lrc','ape')
        if(theSongExistCurrentFolder(songName1)==False and theSongExistCurrentFolder(songName2)==False and theSongExistCurrentFolder(songName3)==False):
            print(os.getcwd()+'\\'+item)
            os.remove(os.getcwd()+'\\'+item)
            count+=1
print('succeed ! 删除了 %d 个条目' %count)

