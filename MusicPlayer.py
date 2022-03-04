from Music import MusicNames as Music
from pydub.playback import play


def play_song(song_name):
    play(song_name)


def pause():
    pause()


def skip():
    pass


def shuffle():
    pass


play_song(Music.gusty_garden_galaxy)
