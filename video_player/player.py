import os
import vlc

video_sample_folder = "/home/pi/Desktop/video_samples"
vid1 = "vid3.mp4"
vid2 = "vid5.mp4"
vid3 = "vid7.mp4"

class my_player():
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        vlc.libvlc_set_fullscreen(self.player, True)
        
        self.medialist = self.instance.media_list_new()
        self.listplayer = self.instance.media_list_player_new()
        
        self.add_media(os.path.join(video_sample_folder, vid1))
        self.add_media(os.path.join(video_sample_folder, vid2))
        self.add_media(os.path.join(video_sample_folder, vid3))
        
        self.listplayer.set_media_list(self.medialist)
        self.listplayer.set_playback_mode(1)
        self.listplayer.set_media_player(self.player)
        
    def add_media(self, file):
        self.medialist.add_media( self.instance.media_new(file) )
        pass
    
    def pause(self):
        self.listplayer.pause()
        pass
    
    def play(self):
        self.listplayer.play()
        pass
    
    def loop(self):
        pass
    
    
print("Starting Player")
mplayer = my_player()
mplayer.play()

while 1:
    pass