import pygame as pg


def gusty_garden_galaxy():
    pg.mixer.music.load("Music/MarioGalaxy1/17 Garden.mp3")
    pg.mixer.music.set_volume(0.7)


def overtune():
    pg.mixer.music.load("Music/MarioGalaxy1/01 Overture.mp3")
    pg.mixer.music.set_volume(0.7)


def play():
    pg.mixer.music.play()


def pause():
    pg.mixer.music.pause()


def unpause():
    pg.mixer.music.unpause()


def skip():
    pass


def shuffle():
    pass
