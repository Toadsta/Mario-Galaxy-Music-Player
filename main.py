import tkinter
from tkinter import *
from Music import MusicFunctions as Mf
import pygame as pg

pg.mixer.init()

def get_element(event):
    selection = event.widget.curselection()
    index = selection[0]
    value = event.widget.get(index)
    if value == "Overtune":
        Mf.overtune()
        Mf.play()
    elif value == "Gusty Garden Galaxy":
        Mf.gusty_garden_galaxy()
        Mf.play()
    else:
        print("How?!")


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

list_box.bind('<<ListboxSelect>>', get_element)

# add to window
list_box.pack()

# waits for user inout
window.mainloop()
