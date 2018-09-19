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

def diagonal_trace(midCanvas, canvas_width, canvas_height):
    ball_diameter = 20 #draw a ball in pixels
    top_x = ball_diameter
    top_y = ball_diameter
    midCanvas.create_oval(top_x, top_y, top_x + ball_diameter,
                            top_y + ball_diameter, fill = "green", tags = "ball3")

    dx = 2
    dy = 2
    while True:
        top_x += dx
        top_y += dy
        print(top_x, top_y)
        if top_x > canvas_width - ball_diameter or top_y > canvas_height - ball_diameter:
            top_x = canvas_width - ball_diameter
            top_y = canvas_height - ball_diameter
            dx = -2
            dy = -2
        elif top_y < ball_diameter or top_x < ball_diameter:
            top_y = ball_diameter
            top_x = ball_diameter
            dy = 2
            dx = 2
        midCanvas.move("ball3", dx, dy)
        midCanvas.after(15)
        midCanvas.update()
