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



'''
Function to stream opened audio file.
'''
def play_sounds(button):
    button_name = button["text"]
    button_nu = int(button_name.split(' ')[-1])
    test = files[button_nu]

    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(test,"rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()


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
        buttons_play[i].destroy()

    load_src_b.config(state=DISABLED)
    load_src_b_m.config(state=DISABLED)

    for i in range(0,15):
        print("remove all files" + buttons_play[i]["text"])

def random_trace():
    ball_diameter = 20 #draw a ball in pixels
    top_x = 2
    top_y = 2
    midCanvas.create_oval(top_x, top_y, top_x + ball_diameter,
                            top_y + ball_diameter, fill = "red", tags = "ball1")
    dx = 2
    dy = 2

    while True:
        #horizontal movement
        top_x += dx
        top_y += dy

        if top_x >= canvas_width - ball_diameter:
            top_x = canvas_width - ball_diameter
            dx = -dx
        if top_x <= ball_diameter:
            top_x = ball_diameter
            dx = -dx
        if top_y >= canvas_height - ball_diameter:
            top_y = canvas_height - ball_diameter
            dy = -dy
        if top_y <= ball_diameter:
            top_y = ball_diameter
            dy = -dy

        midCanvas.move("ball1", dx, dy)
        midCanvas.after(15)
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

def on_enter(button):
    button.config(text="-------")

def on_leave(button):
    button.config(text="")

'''
Function to load objects on Canvas.
'''
def default_source():
    for i in range(0,15):
        print("button_play" + buttons_play[i]["text"])
    for i in range(0,15):
        buttons_play.append(Button(midFrame, text = "Play "+str(i),command=lambda i=i:play_sounds(buttons_play[i]), anchor = W, image = play))
        buttons_play[i].configure(width = 50,height = 34, activebackground = "#33B5E5", relief = FLAT, highlightbackground="white")
        button_window = midCanvas.create_window(15, 15*(i*3+1), anchor=NW, window=buttons_play[i])
    for i in range(0,15):
        if(files[i] is None):
            buttons_play[i].configure(state=DISABLED)
        else:
            buttons_play[i].configure(state=NORMAL)
    buttons_play[i].bind("<Enter>", on_enter(buttons_play[i]))
    buttons_play[i].bind("<Leave>", on_leave(buttons_play[i]))


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
midCanvas.create_line(14,14, 14, canvas_height - 20, dash=(4, 2), arrow=FIRST, state = DISABLED)
#x axis
midCanvas.create_line(14,canvas_height - 20, canvas_width - 50, canvas_height - 20, dash=(4, 2), arrow=LAST, state = DISABLED)
# x and y axis labels
midCanvas.create_text(14,canvas_height - 10, text = "  (0,0)")
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


load_src_b = Button(leftFrame,command=lambda temp_j=temp_j:default_source() ,text="Load GUI(A)", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", state=DISABLED, width = 8)
load_src_b.grid(row=16, column = 2, padx=1,pady=8)

load_src_b_m = Button(leftFrame,command=lambda temp_j=temp_j:default_source() ,text="Load GUI(M)", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", state=DISABLED, width = 8)
load_src_b_m.grid(row=16, column = 3, padx=10,pady=8)

rbutton1 = Button(rightFrame, text="Start", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton2 = Button(rightFrame, text="Check Log", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton3 = Button(rightFrame, command=lambda:remove_all_file(),text="Remove Files",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton4 = Button(rightFrame, command=lambda:default_source(),text="Default",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton5 = Button(rightFrame, command=lambda:random_trace(),text="Random Trace",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton6 = Button(rightFrame, command=lambda:square_trace(),text="Square Trace",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton7 = Button(rightFrame, command=lambda:diagonal_trace(),text="Diagonal Trace",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton8 = Button(rightFrame, text="Exit", command=root.destroy, fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)


rbutton1.grid(row=0, column=3,padx=1,pady=8)
rbutton2.grid(row=1, column=3,padx=1,pady=8)
rbutton3.grid(row=2, column=3,padx=1,pady=8)
rbutton4.grid(row=3, column=3,padx=1,pady=8)
rbutton5.grid(row=4, column=3,padx=1,pady=8)
rbutton6.grid(row=5, column=3,padx=1,pady=8)
rbutton7.grid(row=6, column=3,padx=1,pady=8)
rbutton8.grid(row=7, column=3,padx=1,pady=8)

root.mainloop()
