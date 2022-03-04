import pygame as pg
from MusicApp import


def play():
    pg.mixer.music.play()


def pause():
    pg.mixer.music.pause()


def unpause():
    pg.mixer.music.unpause()


def get_element(event):
    selection = event.widget.curselection()
    index = selection[0]
    value = event.widget.get(index)
    if value == "Overtune":
        mn.overtune()
        play()
    elif value == "Gusty Garden Galaxy":
        mn.gusty_garden_galaxy()
        play()
    else:
        print("How?!")
        # adapted from https://www.code4example.com/python/python3-get-selected-value-from-listbox-in-tkinter/


def skip():
    pass


def shuffle():
    pass
