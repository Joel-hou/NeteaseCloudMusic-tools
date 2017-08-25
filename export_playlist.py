#coding: utf-8

# author: houzhian@gmail.com
# python3 required, tested in windows 10
# usage:
#        running this python script, you will be able to see playlist in m3u format file under the current directory
#        how to run python scripts:
#            if you already have python3 installed in your system and the path to executable file already added to
#        system PATH, open cmd or powershell, change directory to the directory where export_playlist.py exists,
#        type ./export_playlist.py, your playlist will come soon in the current directory.
#            I suggest you download all songs in your playlist firstly, then use this script. It is convenient, you 
#        can import your playlist to other music player or your mp3 which support external m3u format playlist

# for path operations
import os
# netease cloud music save playlist as json format
import json
import codecs
# netease cloud music use sqlite for internal data storage
import sqlite3

class ExportPlayList:
    def __init__(self):
        # connect to sqlite database
        self.conn = sqlite3.connect(os.path.expanduser('~')+"/AppData/Local/Netease/CloudMusic/Library/webdb.dat")

    def extract_playlist_name_from_json(self,jsonStr):
        playlist_detail = json.loads(jsonStr)
        return playlist_detail["name"];

    def get_play_lists(self):
        # create a cursor object to perform sql commands
        my_cursor=self.conn.cursor()
        my_cursor.execute("select * from web_playlist")
        playlists=[]
        for item in my_cursor.fetchall():
            # the return type of mysql execute is tuple
            # playlist: [pid,playlist name]
            playlist=(item[0], self.extract_playlist_name_from_json(item[1]))
            playlists.append(playlist)
        return playlists

    def get_playlist_songs_tid(self, pid):
        my_cursor=self.conn.cursor()
        my_cursor.execute("select * from web_playlist_track where pid=?",[pid])
        songs_id=[]
        for item in my_cursor.fetchall():
            songs_id.append(item[1]);
        return songs_id

    def get_song_detail_by_tid(self,tid):
        my_cursor=self.conn.cursor()
        my_cursor.execute("select * from web_offline_track where track_id=?",[tid])
        song = my_cursor.fetchone()
        if song is None:
            return None
        detail = (self.extract_song_name_from_json(song[4]), song[15])
        return detail

    def write_playlist_to_file(self,pid, playlistName):
        file_name=playlistName+".m3u"
        print(file_name)
        file = codecs.open(file_name, "w","utf-8")
        count = 0
        try:
            file.writelines("#EXTM3U")
            songs_ids = self.get_playlist_songs_tid(pid)
            for tid in songs_ids:
                if tid is not None:
                    detail=self.get_song_detail_by_tid(tid)
                    if detail is not None:
                        count=count + 1
                        file.writelines(u"\n#EXTINF:" + detail[0] + u"\n" + detail[1])
        except Exception as e:
            raise
        else:
            pass
        finally:
            file.close()
            if count <= 0:
                os.remove(file_name)

    def extract_song_name_from_json(self,jsonStr):
        songDetail = json.loads(jsonStr)
        return songDetail["name"];

    def export_playlists(self):
        playlists = self.get_play_lists()
        for item in playlists:
            # params: pid,playlist name
            self.write_playlist_to_file(item[0], item[1])

if __name__ == '__main__':
    ExportPlayList().export_playlists()
