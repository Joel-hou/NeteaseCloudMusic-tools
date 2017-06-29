# author houzhian@gmail.com


import os

filenames=os.listdir(os.getcwd())

def rename(filenames):
   for filename in filenames:
       if(filename[0] == '2' ):
           newfilename=filename[3:len(filename)]
           print(newfilename)
           os.rename(filename,newfilename)
if __name__ =='__main__':
    rename(filenames)
