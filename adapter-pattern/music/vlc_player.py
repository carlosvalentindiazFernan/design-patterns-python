from .advanced_media_player import AdvancedMediaPlayer

class VlcPlayer(AdvancedMediaPlayer):
    """ VLC Player Class """

    def playVlc(self,fileName):
        print(f'playing vlc file {fileName}')
