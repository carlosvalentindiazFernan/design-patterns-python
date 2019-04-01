from music.audio_player import AudioPlayer

def main():
    player = AudioPlayer()
    player.play('mp3','wild wild son')
    player.play('mp4','show me love')
    player.play('vlc','Rage Rage')


if __name__ == "__main__":
    main()