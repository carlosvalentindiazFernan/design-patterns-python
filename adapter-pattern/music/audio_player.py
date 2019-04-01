from .media_player import MediaPlayer
from .media_adapter import MediaAdapter
class AudioPlayer(MediaPlayer):
    """ Audio Player Class """

    def play(self,audioType,fileName):
        if audioType == 'mp3':
            print(f'playing mp3 file {fileName}')
        elif audioType == 'mp4' or audioType == "vlc":
            media = MediaAdapter(audioType)
            media.play(audioType,fileName)
        else:
            print(f'File not support')