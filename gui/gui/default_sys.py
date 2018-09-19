from tkinter import *
from tkinter.filedialog import askopenfilename
import pyaudio
import wave
import turtle
import math
from PIL import ImageTk, Image
from pygame import *
#import mplayer
import cmath,math

def default_sys(midFrame, lbuttons_x, buttons_upload, files, llabels, load_src_b, buttons_play, labels_play, play,y2_cord):
    space_cal=y2_cord/15
    for i in range(15,0,-1):
        files[15 - i] = str(16-i) + ".wav"
        llabels[15-i].configure(text=str(i) + ".wav")

    load_src_b.config(state=NORMAL)
    #load_src_b_m.config(state=NORMAL)

    for i in range(0,15):
        #play_sounds(buttons_play[i])
        buttons_play.append(Button(midFrame, text = str(i),command=lambda i=i:play_sounds(buttons_play[i]), anchor = W, image = play, relief = FLAT, bg="white",highlightbackground="white"))
        #buttons_play[i].configure(width = 30,height = 20, activebackground = "white", relief = FLAT, highlightbackground="white")
        buttons_play[i].place(x=20, y=i*space_cal)
        buttons_play[i].config(compound="top")
        #set text as file name without extension
        #temp = files[14-i].rsplit('.')
        #labels_play[i].config(text=temp[0])
        #labels_play[i].place(x=80, y=i*space_cal)
        #tooltip
        #button_ttp.append(CreateToolTip(buttons_play[i], files[14-i]))

    load_src_b.configure(state=DISABLED)

    for i in range(0,15):
        if(files[i] is None):
            buttons_play[i].configure(state=DISABLED)
            lbuttons_x[i].configure(state=DISABLED)
            buttons_upload[i].configure(state=DISABLED)
        else:
            buttons_play[i].configure(state=NORMAL)
            lbuttons_x[i].configure(state=NORMAL)
            buttons_upload[i].configure(state=NORMAL)
