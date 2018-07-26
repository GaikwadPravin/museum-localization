'''
Import required libraries
'''
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

'''
global  variable declaration
'''
#Number of files in system(15).
files = [None] * 15
#Labels array in left frame.
llabels = []
#Labels number array in left frame.
llabels_no = []
#Buttons array in left frame.
lbuttons = []
#Delete file buttons array in left frame.
lbuttons_x = []
#Canvas play buttons arrar in mid-frame.
buttons_play = []

labels_play = []
#button_ttp = []
'''
#tooltips

try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()
'''
'''
Function to stream opened audio file.
'''


bttn_clicks = 0
mixer.init()


def play():
    mixer.music.play()
    global bttn_clicks
    bttn_clicks = 0

def pause():
    global bttn_clicks
    bttn_clicks += 1
    if(bttn_clicks % 2 == 0):
        mixer.music.unpause()
    else:
        mixer.music.pause()
    print(bttn_clicks)

def stop():
    mixer.music.stop()
    global bttn_clicks
    bttn_clicks = 0

def play_sounds(button):
    button_name = button["text"]
    button_nu = int(button_name.split(' ')[-1])
    test = files[button_nu]




    mixer.music.load(test)
    window = Toplevel(root)
    window.title('Music Player')

    '''
    image_play= PhotoImage(file = "play_mp.png")
    image_play= image_play.subsample(7,7)
    image_resume= PhotoImage(file = "resume.png")
    image_resume= image_resume.subsample(7,7)
    image_stop= PhotoImage(file = "stop.png")
    image_stop= image_stop.subsample(7,7)
    '''

    #, image=image_play
    play_b = Button(window,text = 'Play',highlightbackground="white", relief="raised")#, image=image_play)
    #play_b.place(x=100, y=15)
    play_b.grid(row=0,column=4,padx=1,pady=8)
    #play_b.pack(side = TOP)

    #image=image_resume
    resume_b = Button(window,text = 'Pause',highlightbackground="white", relief="raised")#, image=image_resume)
    #resume_b.place(x=150, y=15)
    resume_b.grid(row=0,column=5,padx=1,pady=8)
    #resume_b.pack(side = TOP)

    #image=image_stop,
    stop_b = Button(window,text='Stop',highlightbackground="white", relief="raised")#, image=image_stop)
    #stop_b.place(x=200, y=15)
    stop_b.grid(row=0,column=6,padx=1,pady=8)
    #stop_b.pack(side = TOP)

    play_b.config(command=lambda:play())
    resume_b.config(command=lambda:pause())
    stop_b.config(command=lambda:stop())
    '''
    play_b.bind("<Button-1>",play)
    resume_b.bind("<Button-1>",pause)
    stop_b.bind("<Button-1>",stop)
    '''


'''
Function to browse audio file.
'''
def browse_for_file(button):
    for j in range(0,15):
        print(lbuttons[j]["text"])
    button_name = button["text"]
    print("browse_for_file " + button_name)
    file_name_w_path = askopenfilename(parent=leftFrame,title='Open File')
    if(file_name_w_path!=''):
        file_name = file_name_w_path.rsplit('/')
        #button_text = button.cget("text")
        button_nu = int(button_name.split(' ')[-1])
        print("button_nu " + str(button_nu))
        files[15 - button_nu] = file_name_w_path
        temp = file_name[-1].rsplit('.')
        llabels[15 - button_nu].config(text=temp[0])
        leftFrame.update()
    labels_play[15 - button_nu].config(text=temp[0])
    '''
    #tooltips

    button_ttp[15 - button_nu].hidetip()
    print("button_ttp ")
    print(button_ttp)
    print(temp[0])
    button_ttp[15 - button_nu] = CreateToolTip(buttons_play[button_nu], temp[0])
    print("button_ttp ---")
    print(button_ttp)
    '''
    count = 0
    for j in range(0,15):
        if(files[j] is not None):
            load_src_b.config(state=NORMAL)
            load_src_b_m.config(state=NORMAL)
            buttons_play[j].config(state=NORMAL)
            break
        else:
            count = count + 1
    if count == 15:
        load_src_b.config(state=DISABLED)
        load_src_b_m.config(state=DISABLED)

'''
Function to remove files corresponding to each button.
'''
def remove_file(button):
    button_name = button["text"]
    button_nu = int(button_name.split(' ')[-1])
    print(str(button_nu) + "--------")
    llabels[15-button_nu].config(text='No File')
    files[15-button_nu] = None
    labels_play[15-button_nu].config(text="No File")
    print("file array" + str(len(files)))
    count = 0
    print(files)
    for j in range(0,15):
        print(j)
        if(files[j] is None):
            buttons_play[j].config(state=DISABLED)
            count = count + 1
    print("count " + str(count))
    if count == 15:
        load_src_b.config(state=DISABLED)
        load_src_b_m.config(state=DISABLED)

'''
Function to remove all files and Canvas objects corresponding to each button.
'''
def remove_all_file():

    for j in range(0,15):
        files[j] = None
    print("files size " + str(len(files)))
    for i in range(0,15):
        llabels[i].config(text='No File')
        buttons_play[i].place_forget()
        labels_play[i].place_forget()

    load_src_b.config(state=DISABLED)
    load_src_b_m.config(state=DISABLED)

    for i in range(0,15):
        print("remove all files" + buttons_play[i]["text"])

def random_trace():

    border_offset = 50
    c_offset = 100
    top_x = c_offset
    top_y = 10
    #midCanvas.create_oval(top_x, top_y, top_x + ball_diameter,
    #                        top_y + ball_diameter, fill = "red", tags = "ball1")
    dx = 1
    dy = 1
    i = 180
    #temp_dai = ball_diameter
    #pointer_image = midCanvas.create_image(50,50,image = image_pointer, state = DISABLED )

    center = 5, 5
    triangle = [(0, 0), (30, 10), (0, 20)]
    polygon_item = midCanvas.create_polygon(triangle)
    rectangle = [(top_x,top_y),(canvas_width - 10, canvas_height - 10)]
    rectangle_item = midCanvas.create_rectangle(rectangle, dash=(1,5))

    while True:
        cangle = cmath.exp(i*1j*math.pi/180)
        i += 0
        offset = complex(center[0], center[1])
        newxy = []
        for x, y in triangle:
            v = cangle * (complex(x, y) - offset) + offset
            newxy.append(v.real)
            newxy.append(v.imag)
        midCanvas.coords(polygon_item, *newxy)
        midCanvas.move(polygon_item,top_x,top_y)

        if(i>360):
            i = 0
        if top_x >= canvas_width - border_offset:
            top_x = canvas_width - border_offset
            dx = -dx

        if top_x <= c_offset+20:
            top_x = c_offset+20
            dx = -dx

        if top_y >= canvas_height - 10:
            top_y = canvas_height - 10
            dy = -dy

        if top_y <= 10:
            top_y = 10
            dy = -dy

        top_x += 0
        top_y += dy

        midCanvas.after(10)
        midCanvas.update()


def square_trace():
    ball_diameter = 20 #draw a ball in pixels
    top_x = ball_diameter
    top_y = ball_diameter
    midCanvas.create_oval(top_x, top_y, top_x + ball_diameter,
                            top_y + ball_diameter, fill = "blue", tags = "ball2")

    dx = 2
    dy = 0
    while True:
        top_x += dx
        top_y += dy
        print(top_x, top_y)
        if top_x >= canvas_width - ball_diameter:
            top_x = canvas_width - ball_diameter
            dx = 0
            dy = 2
            #dx = -dx

        if top_y >= canvas_height - ball_diameter:
            top_y = canvas_height - ball_diameter
            #dy = -dy
            dy = 0
            dx = -2

        if top_x < ball_diameter:
            top_x = ball_diameter
            #dx = -dx
            dx = 0
            dy = -2

        if top_y < ball_diameter:
            top_y = ball_diameter
            #dy = -dy
            dy = 0
            dx = 2

        midCanvas.move("ball2", dx, dy)
        midCanvas.after(15)
        midCanvas.update()

def diagonal_trace():
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


def show_entry_fields(x,y,r):
   print('in show function')
   print(x)
   print(y)
   print(r)

def input():

    window = Toplevel(root)
    window.title('User Input')


    Label(window, text="x co-ordinate").grid(row=0)
    Label(window, text="y co-ordinate").grid(row=1)
    Label(window, text="orientation").grid(row=2)

    x1 = IntVar()
    y1 = IntVar()
    r1 = IntVar()


    x = Entry(window, textvariable=x1)
    y = Entry(window, textvariable=y1)
    r = Entry(window, textvariable=r1)

    x.grid(row=0, column=1)
    y.grid(row=1, column=1)
    r.grid(row=2, column=1)

    x_co=int(x1.get())
    y_co=int(y1.get())
    r_co=int(r1.get())


    user_button1 = Button(window, text='Quit', command=window.destroy)
    user_button1.grid(row=3, column=0, sticky=W, pady=4)
    user_button2 = Button(window, text='Show', command=lambda:show_entry_fields(x_co,y_co,r_co))
    user_button2.grid(row=3, column=1, sticky=W, pady=4)

    print("man loop")
    print(x_co)
    print(y_co)
    print(r_co)

    window.mainloop()

def update_co():

    border_offset = 50
    c_offset = 100
    top_x = c_offset
    top_y = 10
    #midCanvas.create_oval(top_x, top_y, top_x + ball_diameter,
    #                        top_y + ball_diameter, fill = "red", tags = "ball1")
    dx = 1
    dy = 1
    i = 180
    #temp_dai = ball_diameter
    #pointer_image = midCanvas.create_image(50,50,image = image_pointer, state = DISABLED )

    center = 5, 5
    triangle = [(0, 0), (30, 10), (0, 20)]
    polygon_item = midCanvas.create_polygon(triangle)
    rectangle = [(top_x,top_y),(canvas_width - 10, canvas_height - 10)]
    rectangle_item = midCanvas.create_rectangle(rectangle, dash=(1,5))
    i = r_co
    print(type(i))
    while True:
        cangle = cmath.exp(i*1j*math.pi/180)
        #i += 0
        offset = complex(center[0], center[1])
        newxy = []
        for x, y in triangle:
            v = cangle * (complex(x, y) - offset) + offset
            newxy.append(v.real)
            newxy.append(v.imag)
        midCanvas.coords(polygon_item, *newxy)
        midCanvas.move(polygon_item,top_x,top_y)

        if(i>360):
            i = 0
        if top_x >= canvas_width - border_offset:
            top_x = canvas_width - border_offset
            dx = -dx

        if top_x <= c_offset+20:
            top_x = c_offset+20
            dx = -dx

        if top_y >= canvas_height - 10:
            top_y = canvas_height - 10
            dy = -dy

        if top_y <= 10:
            top_y = 10
            dy = -dy

        top_x += x_co
        top_y += y_co

        midCanvas.after(10)
        midCanvas.update()


'''
Function to load objects on Canvas.
'''
def default_source():
    for i in range(0,15):
        print("button_play" + buttons_play[i]["text"])

    for i in range(0,15):
        buttons_play.append(Button(midFrame, text = "Play "+str(i),command=lambda i=i:play_sounds(buttons_play[i]), anchor = W, image = play))
        buttons_play[i].configure(width = 50,height = 34, activebackground = "#33B5E5", relief = FLAT, highlightbackground="white")
        #button_window = midCanvas.create_window(15, 15*(i*3+1), anchor=NW, window=buttons_play[i])
        buttons_play[i].place(x=20, y=15*(i*3+1))
        #if(labels_play_flag == 1):
        #check whether file is present or not
        if(files[i] == None):
            temp = "No File"
            labels_play[i].config(text=temp)
        else:
            #set text = wave file name without .wav extension
            temp = files[i].rsplit('/')[-1].rsplit('.')
            labels_play[i].config(text=temp[0])
        #palce the object on canvas
        labels_play[i].place(x=80, y=15*(i*3+2))

    for i in range(0,15):
        if(files[i] is None):
            buttons_play[i].configure(state=DISABLED)
        else:
            buttons_play[i].configure(state=NORMAL)

'''
Function to load objects on Canvas.
'''
def default_sys():
    for i in range(15,0,-1):
        files[15 - i] = str(16-i) + ".wav"
        llabels[15-i].configure(text=str(i) + ".wav")

    load_src_b.config(state=NORMAL)
    load_src_b_m.config(state=NORMAL)

    for i in range(0,15):
        #play_sounds(buttons_play[i])
        buttons_play.append(Button(midFrame, text = "Play "+str(i),command=lambda i=i:play_sounds(buttons_play[i]), anchor = W, image = play))
        buttons_play[i].configure(width = 50,height = 34, activebackground = "#33B5E5", relief = FLAT, highlightbackground="white")
        buttons_play[i].place(x=20, y=15*(i*3+1))
        #set text as file name without extension
        temp = files[14-i].rsplit('.')
        labels_play[i].config(text=temp[0])
        labels_play[i].place(x=80, y=15*(i*3+2))
        #tooltip
        #button_ttp.append(CreateToolTip(buttons_play[i], files[14-i]))


    for i in range(0,15):
        if(files[i] is None):
            buttons_play[i].configure(state=DISABLED)
        else:
            buttons_play[i].configure(state=NORMAL)


root = Tk()
root.title('3D Audio Museum Exhibit')
topFrame = Frame(root)
topFrame.pack(side=TOP)

label1 = Label(topFrame, text="3D Audio Museum Exhibit", fg="black",  relief="flat")
label1.config(font=(None, 25))
label1.pack(fill=X)

leftFrame = Frame(root,highlightbackground="black", highlightcolor="green", highlightthickness=2, bg="dark slate gray")
leftFrame.pack(side=LEFT,fill="both")

midFrame = Frame(root, highlightbackground="black", highlightcolor="green", highlightthickness=2, bg="orange")
midFrame.pack(side=LEFT,fill="both", expand=True)

rightFrame = Frame(root, highlightbackground="black", highlightcolor="green", highlightthickness=2, bg="dark slate gray")
rightFrame.pack(side=RIGHT,fill="both")

canvas_width = 850
canvas_height = 700
midCanvas = Canvas(midFrame, width=canvas_width, height=canvas_height, bg = "white")
#y axis
midCanvas.create_line(14,14, 14, canvas_height - 10, dash=(4, 2), arrow=FIRST, state = DISABLED)
#x axis
midCanvas.create_line(14,canvas_height - 10, canvas_width - 50, canvas_height - 10, dash=(4, 2), arrow=LAST, state = DISABLED)
# x and y axis labels
midCanvas.create_text(14,canvas_height - 1, text = "  (0,0)")
midCanvas.create_text(14,10, text = "  y-axis")
midCanvas.create_text(canvas_width - 35,canvas_height - 30, text = "  x-axis")
midCanvas.pack(expand = YES, fill = BOTH)

image2= PhotoImage(file = "gator.png")
image = midCanvas.create_image(450,335,image = image2, state = DISABLED )

midCanvas.itemconfig(buttons_play,tags="canvasButtons")

for i in range(15, 0, -1):
    temp_j = 15-i
    llabels_no.append(Label(leftFrame, text=str(i)+'.', bg="dark slate gray", fg="white"))
    llabels_no[15-i].grid(row=15-i, column=1,padx=1,pady=8)

    lbuttons.append(Button(leftFrame,command=lambda temp_j=temp_j:browse_for_file(lbuttons[temp_j]) ,text="Upload File "+ str(i), fg="white", bg = "dim gray", highlightbackground="black", relief="flat"))
    lbuttons[15-i].grid(row=15-i, column=2,padx=1,pady=8)

    llabels.append(Label(leftFrame, text="No File", fg = "white", bg = "dark slate gray", anchor=E, width = 10))
    llabels[15-i].grid(row=15-i, column=3,padx=1,pady=8)

    lbuttons_x.append(Button(leftFrame,command=lambda temp_j=temp_j:remove_file(lbuttons[temp_j]) ,text="X", fg="white", bg = "dim gray", highlightbackground="black", relief="flat"))
    lbuttons_x[15-i].grid(row=15-i, column=4,padx=8,pady=8)

image_play= PhotoImage(file = "play.png")
play = image_play.subsample(3,3)


for i in range(0,15):
    buttons_play.append(Button(midFrame, text = "Play "+str(i),command=lambda i=i:play_sounds(buttons_play[i]), anchor = W, image = play))
    buttons_play[i].configure(width = 50,height = 34, activebackground = "#33B5E5", relief = FLAT, highlightbackground="white")
    labels_play.append(Label(midFrame, text="None", bg="white", fg="black", state=DISABLED))


load_src_b = Button(leftFrame,command=lambda temp_j=temp_j:default_source() ,text="Load GUI(A)", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", state=DISABLED, width = 8)
load_src_b.grid(row=16, column = 2, padx=1,pady=8)

load_src_b_m = Button(leftFrame,command=lambda temp_j=temp_j:default_source() ,text="Load GUI(M)", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", state=DISABLED, width = 8)
load_src_b_m.grid(row=16, column = 3, padx=10,pady=8)

rbutton1 = Button(rightFrame, text="Start", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton2 = Button(rightFrame, text="Check Log", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton3 = Button(rightFrame, command=lambda:remove_all_file(),text="Remove Files",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton4 = Button(rightFrame, command=lambda:default_sys(),text="Default",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton5 = Button(rightFrame, command=lambda:random_trace(),text="Random Trace",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton6 = Button(rightFrame, command=lambda:square_trace(),text="Square Trace",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton7 = Button(rightFrame, command=lambda:diagonal_trace(),text="Diagonal Trace",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton8 = Button(rightFrame, command=lambda:input(),text="User Trace",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton9 = Button(rightFrame, text="Exit", command=root.destroy, fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)


rbutton1.grid(row=0, column=3,padx=1,pady=8)
rbutton2.grid(row=1, column=3,padx=1,pady=8)
rbutton3.grid(row=2, column=3,padx=1,pady=8)
rbutton4.grid(row=3, column=3,padx=1,pady=8)
rbutton5.grid(row=4, column=3,padx=1,pady=8)
rbutton6.grid(row=5, column=3,padx=1,pady=8)
rbutton7.grid(row=6, column=3,padx=1,pady=8)
rbutton8.grid(row=7, column=3,padx=1,pady=8)
rbutton9.grid(row=8, column=3,padx=1,pady=8)

'''
image_play= PhotoImage(file = "play_mp.png")
image_play= image_play.subsample(7,7)
image_resume= PhotoImage(file = "resume.png")
image_resume= image_resume.subsample(7,7)
image_stop= PhotoImage(file = "stop.png")
image_stop= image_stop.subsample(7,7)
'''
image_pointer = PhotoImage(file = "pointer.png")
image_pointer = image_pointer.subsample(30,30)

'''
play_b = Button(midFrame,text = 'Play',highlightbackground="white", relief="raised", image=image_play)
resume_b = Button(midFrame,text = 'Pause',highlightbackground="white", relief="raised", image=image_resume)
stop_b = Button(midFrame,text='Stop',highlightbackground="white", relief="raised", image=image_stop)
'''
root.mainloop()
