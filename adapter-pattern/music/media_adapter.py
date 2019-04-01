from .media_player import MediaPlayer
from .mp4_player import Mp4Player
from .vlc_player import VlcPlayer

class MediaAdapter(MediaPlayer):
    """ Media Adapter Class """

    def __init__(self, audioType):
        if audioType.upper() == 'VLC':
            self.player = VlcPlayer()
        elif audioType.upper() == 'MP4':
            self.player = Mp4Player()
    

    def play(self,audioType,fileName):
        if audioType.upper() == 'VLC':
            self.player.playVlc(fileName)
        elif audioType.upper() == 'MP4':
            self.player.playMp4(fileName)
