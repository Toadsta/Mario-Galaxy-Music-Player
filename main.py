from tkinter import *
from MusicApp import MusicFunctions as Mf
import pygame as pg


def main():
    pg.mixer.init()

    # creates a window
    window = Tk()
    window.title("Music Player")
    window.geometry("250x300")
    window.resizable(False, False)
    # creates a label
    # title = Label(window, text="Mario Galaxy: Music Player")

    # add to window
    # title.pack()

    # create a quit box
    # tkinter.Button(window, text="Quit", command=window.destroy).pack()

    # creates a list box
    list_box = Listbox(window)

    list_box.insert(0, "Overtune")
    list_box.insert(1, "Gusty Garden Galaxy")

    # create an play music button
    # play_button = Button(window, text="Play", command=play)
    # play_button.pack(side='bottom')

    # play_selected = Button(window, text="Play", command=selected_item)
    # play_selected.pack(side='bottom')

    pause = Button(window, text="Pause", command=Mf.pause)
    pause.place(x=10, y=230)

    unpause = Button(window, text="Unpause", command=Mf.unpause)
    unpause.place(x=150, y=230)

    list_box.bind('<<ListboxSelect>>', Mf.get_element)

    # add to window
    list_box.pack()

    # waits for user inout
    window.mainloop()


if __name__ == '__main__':
    main()
