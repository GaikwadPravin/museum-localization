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

def browse_for_file(button, buttons_upload, lbuttons_x, files, llabels, leftFrame, labels_play, load_src_b, buttons_play):
    #for j in range(0,15):
    #    print(lbuttons[j]["text"])
    button_name = button["text"]
    print("button in browse file" + button_name)
    #print("browse_for_file " + button_name)
    file_name_w_path = askopenfilename(parent=leftFrame,title='Open File')
    if(file_name_w_path!=''):
        file_name = file_name_w_path.rsplit('/')
        #button_text = button.cget("text")
        button_nu = int(button_name.split(' ')[-1])
        #print("button_nu " + str(button_nu))
        files[15 - button_nu] = file_name_w_path
        temp = file_name[-1].rsplit('.')
        llabels[15 - button_nu].config(text=temp[0])
        leftFrame.update()
    labels_play[15 - button_nu].config(text=temp[0])
    print("all files after browse")
    print(files)
    count = 0
    for j in range(0,15):
        if(files[j] is not None):
            print("button to be enabled:" + str(j))
            load_src_b.config(state=NORMAL)
            buttons_play[j].config(state=NORMAL)
            buttons_upload[j].config(state=NORMAL)
            lbuttons_x[j].config(state=NORMAL)
#check for other buttons as break will stop the for loop
        else:
            count = count + 1
    if count == 15:
        load_src_b.config(state=DISABLED)
