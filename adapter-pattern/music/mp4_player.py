from .advanced_media_player import AdvancedMediaPlayer

class Mp4Player(AdvancedMediaPlayer):
    """ Mp4 player Class """

    def playMp4(self,fileName):
        print(f'playing mp4 file {fileName}')
