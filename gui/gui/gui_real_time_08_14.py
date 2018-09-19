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
import pickle
#import mplayer
import cmath,math
from default_sys import *
from dia_trace import *
from squ_trace import *
from browse_file import *
from tkinter import messagebox


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

museum_info = []
museum_info_b_clicks=0

llabels_no_cases=[]
entries_x = []
entries_y = []
buttons_upload = []
play_manual = []
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
            buttons_upload[j].config(state=DISABLED)
            lbuttons_x[j].config(state=DISABLED)
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

def show_canvas(window, width,length):
    global museum_info_b_clicks


    m_width = int(width.get())
    m_length = int(length.get())
    museum_info_b_clicks += 1

    print(museum_info_b_clicks)
    if(museum_info_b_clicks > 1 ):
        midCanvas.delete(museum_lw, lt, lb, rt, rb)
        rect = [(5,5),(m_width , m_length)]
        museum_lw = midCanvas.create_rectangle(rect, dash=(1,5), tag="museum_l")
        lt = midCanvas.create_text(30,30, text = '(0, ' + str(m_length) + ')')
        lb = midCanvas.create_text(30,m_length-15, text = '(0, 0)')
        rt = midCanvas.create_text(m_width-15,30, text = '( '+str(m_width) + ', ' + str(m_length) + ')')
        rb = midCanvas.create_text(m_width-15,m_length-15, text = '( '+str(m_width) + ', ' + '0)')

    else:
        rect = [(5,5),(m_width , m_length)]
        museum_lw = midCanvas.create_rectangle(rect, dash=(1,5), tag="museum_l")
        lt = midCanvas.create_text(30,30, text = '(0, ' + str(m_length) + ')')
        lb = midCanvas.create_text(30,m_length-15, text = '(0, 0)')
        rt = midCanvas.create_text(m_width-15,30, text = '( '+str(m_width) + ', ' + str(m_length) + ')')
        rb = midCanvas.create_text(m_width-15,m_length-15, text = '( '+str(m_width) + ', ' + '0)')


        global museum_lw, museum_l, lt, rt, lb, rb
        #rect = [(5,5),(canvas_width , canvas_length)]
        #museum_lw = midCanvas.create_rectangle(rect, dash=(1,5))
        #museum_info[0] = museum_lw

    window1 = Toplevel(root)
    window1.title('Place objects')

    Label(window1, text="Number of objects").grid(row=0)
    label_ip = Entry(window1)
    label_ip.grid(row=0, column=1)
    Button(window1, text='Next', command=lambda:show_canvas(width,length)).grid(row=3, column=1, sticky=W, pady=4)

def canvas_details():
    window = Toplevel(root)
    window.title('Canvas Details')


    Label(window, text="Museum Width").grid(row=0)
    Label(window, text="Museum Length").grid(row=1)

    width = Entry(window)
    length = Entry(window)

    width.grid(row=0, column=1)
    length.grid(row=1, column=1)

    quit_button = Button(window, text='Quit', command=window.destroy).grid(row=3, column=0, sticky=W, pady=4)
    next_button = Button(window, text='Next', command=lambda:show_canvas(window,width,length)).grid(row=3, column=1, sticky=W, pady=4)

    window.mainloop()


def input():

    window = Toplevel(root)
    window.title('User Input')


    Label(window, text="x co-ordinate").grid(row=0)
    Label(window, text="y co-ordinate").grid(row=1)
    Label(window, text="orientation").grid(row=2)



    x = Entry(window)
    y = Entry(window)
    r = Entry(window)

    x.grid(row=0, column=1)
    y.grid(row=1, column=1)
    r.grid(row=2, column=1)

    Button(window, text='Quit', command=window.destroy).grid(row=3, column=0, sticky=W, pady=4)
    Button(window, text='Show', command=lambda:show_entry_fields(x,y,r)).grid(row=3, column=1, sticky=W, pady=4)

    window.mainloop()


def show_entry_fields(x,y,r):

    print(int(x.get()))
    print(int(y.get()))
    print(int(r.get()))

    '''
    first_line = open("stationary_beacon_position.txt", "r").readlines()[0].split(",")
    last_line = open("stationary_beacon_position.txt", "r").readlines()[-1].split(",")

    print(first_line, last_line)

    b = math.floor(float(first_line[1]))
    a = math.floor(float(first_line[0]))
    d = math.floor(float(last_line[1]))
    c = math.floor(float(last_line[0]))

    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
    print(0, type(0))

    #rect = [(a,b),(c,d)]
    rect_item = midCanvas.create_rectangle((a,b), (c,d), dash=(2,5))
    '''

    rectangle = [(100,10),(canvas_width - 10, canvas_height - 10)]
    rectangle_item = midCanvas.create_rectangle(rectangle, dash=(1,5))


    center = 5, 5
    triangle = [(0, 0), (30, 10), (0, 20)]
    polygon_item = midCanvas.create_polygon(triangle)
    top_x = int(x.get())
    top_y = int(y.get())
    angle = int(r.get())

    dx = 1
    dy = 1
    while True:
        #midCanvas.coords(polygon_item, 0+top_x,0+top_y, 30+top_x,10+top_y, 0+top_x, 20+top_y)

        cangle = cmath.exp((angle - 180)*1j*math.pi/180)
        offset = complex(center[0], center[1])
        newxy = []
        for x, y in triangle:
            v = cangle * (complex(x, y) - offset) + offset
            newxy.append(v.real)
            newxy.append(v.imag)
        midCanvas.coords(polygon_item, *newxy)
        midCanvas.move(polygon_item,top_x,top_y)
        #a, b, c, d, e, f = midCanvas.coords(polygon_item)
        #print(a, b, c, d, e, f)
        #top_y+=dy
        #top_x+=dx

        #if(i>360):
        #    i = 0
        if top_x >= canvas_width - 10:
            top_x = canvas_width - 10
            dx = -dx

        if top_x <= 100+20:
            top_x = 100+20
            dx = -dx

        if top_y >= canvas_height - 10:
            top_y = canvas_height - 10
            dy = -dy

        if top_y <= 10:
            top_y = 10
            dy = -dy


        midCanvas.after(10)
        midCanvas.update()

def real_time():
    center = 5, 5
    triangle = [(0, 0), (30, 10), (0, 20)]
    polygon_item = midCanvas.create_polygon(triangle,0,0)

    #angle = int(r.get())

    dx = 1
    dy = 1
    count=0
    prevx=0
    prevy=0
    i=0
    while True:
        count=count+1
        print(count)
        with open('output.txt') as fp:
            for line in fp:
                x,y,angle=line.split(",")
                top_x=math.ceil( float(x)*scale_factor_x)
                top_y= math.ceil(float(y)*scale_factor_y)
                angle= math.ceil(float(angle))
                print(top_x,top_y)
                midCanvas.delete(polygon_item)
                center = 5+top_x, 5+top_y
                triangle = [(0+top_x, 0+top_y), (30+top_x, 10+top_y), (0+top_x, 20+top_y)]
                polygon_item = midCanvas.create_polygon(triangle,0,0)

            #midCanvas.coords(polygon_item, 0+top_x,0+top_y, 30+top_x,10+top_y, 0+top_x, 20+top_y)


                #offset = complex(center[0], center[1])
                #newxy = []
                cangle = cmath.exp(angle*1j*math.pi/180)
                #i += 1
                offset = complex(center[0], center[1])
                newxy = []
                for x, y in triangle:
                    v = cangle * (complex(x, y) - offset) + offset
                    newxy.append(v.real)
                    newxy.append(v.imag)
                midCanvas.coords(polygon_item, *newxy)

                #if(i>360):
                #    i = 0

                #midCanvas.move(polygon_item,top_x-prevx,top_y-prevy)
                #a, b, c, d, e, f = midCanvas.coords(polygon_item)
                #print(a, b, c, d, e, f)
                #top_y+=dy
                #top_x+=dx

                #if(i>360):
                #    i = 0
                '''
                if top_x >= canvas_width - 10:
                    top_x = canvas_width - 10
                    dx = -dx

                if top_x <= 100+20:
                    top_x = 100+20
                    dx = -dx

                if top_y >= canvas_height - 10:
                    top_y = canvas_height - 10
                    dy = -dy

                if top_y <= 10:
                    top_y = 10
                    dy = -dy
                '''

                midCanvas.after(1000)
                midCanvas.update()
                prevx=top_x
                prevy=top_y



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

def show(window, act_sys_nu, entries_x, entries_y):
    print("Inside show")
    x_co = int(entries_x.get())
    y_co = int(entries_y.get())
    if(len(play_manual) > 0):
        for i in range(0,len(play_manual)):
            buttin_no = int(play_manual[i]["text"].split(' ')[-1])
            print(buttin_no, act_sys_nu)

            if( buttin_no == act_sys_nu):
                midCanvas.delete(play_manual[i])
                #play_manual.append(Button(midFrame, text = "Play "+str(i),command=lambda i=i:play_sounds(buttons_play[i]), anchor = W, image = play, relief = FLAT, bg="white",highlightbackground="white"))
                play_manual[i].place(x=x_co, y=y_co)
            else:
                play_manual.append(Button(midFrame, text = "Play "+str(i),command=lambda i=i:play_sounds(buttons_play[i]), anchor = W, image = play, relief = FLAT, bg="white",highlightbackground="white"))
                play_manual[-1].place(x=x_co, y=y_co)
    else:
        play_manual.append(Button(midFrame, text = "Play 0",command=lambda:play_sounds(play_manual[0]), anchor = W, image = play, relief = FLAT, bg="white",highlightbackground="white"))
        play_manual[0].place(x=x_co, y=y_co)
    print(play_manual)

def manual_source(button):
    window = Toplevel(root)
    window.title('Showcase locations')

    button_name = button["text"]
    button_nu = int(button_name.split(' ')[-1])
    print("manual source "+button_name)
    act_sys_nu = 15 - button_nu
    if(files[act_sys_nu] is not None):
    #messagebox.showerror("Error", "Error message")
        Label(window, text="x co-ordinate").grid(row=0,column=1)
        Label(window, text="y co-ordinate").grid(row=0,column=2)
        Label(window, text='Button Number '+str(button_nu)+'.').grid(row=1,column=0)
        Label(window, text='max_width_canvas '+ str(canvas_width)).grid(row=2,column=0)
        Label(window, text='max_length_canvas '+ str(canvas_height)).grid(row=3,column=0)
        entries_x = Entry(window)
        entries_x.grid(row=1,column=1)
        entries_y = Entry(window)
        entries_y.grid(row=1,column=2)

        show_b = Button(window, text='Show', command=lambda:show(window, act_sys_nu,  entries_x, entries_y))
        show_b.grid(row=3,column=1)
        exit = Button(window, text='Quit', command=window.withdraw)
        exit.grid(row=3,column=2)


'''
Function to load objects on Canvas.
'''
file = open("1.txt", "r")
sensor1,x1_cord,y1_cord,sensor2,x2_cord,y2_cord= file.readline().split(",")

root = Tk()
root.title('3D Audio Museum Exhibit')
#root.attributes('-fullscreen',True)
root.resizable(0,0)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_width)
print(screen_height)

'''
window = Toplevel(root)
window.title('Showcase number')

label_nu_cases = Label(window, text="Enter total number of showcases in museum")
label_nu_cases.pack(side=LEFT,expand=True)
global_nu_cases = Entry(window)
global_nu_cases.pack(side=LEFT,expand=True)
'''

topFrame = Frame(root)
topFrame.pack(side=TOP)

label1 = Label(topFrame, text="3D Audio Museum Exhibit", fg="black",  relief="flat")
label1.config(font=(None, 25))
label1.pack(fill=X)

leftFrame = Frame(root,highlightbackground="black", highlightcolor="green", highlightthickness=2, bg="dark slate gray")
leftFrame.pack(side=LEFT,fill="both")

midFrame = Frame(root, highlightbackground="black", highlightcolor="green", highlightthickness=2, bg="orange")
midFrame.pack(side=LEFT,fill="both")

rightFrame = Frame(root, highlightbackground="black", highlightcolor="green", highlightthickness=2, bg="dark slate gray")
rightFrame.pack(side=LEFT, fill="both")



canvas_width = screen_width-1000
canvas_height = screen_height- 150

print(type(x2_cord))
print(type(canvas_width))

midCanvas = Canvas(midFrame, width=canvas_width, height=canvas_height, bg = "white", bd=0, highlightthickness=0)
midCanvas.pack(fill=BOTH, expand=1)
#midCanvas.bind("<Configure>",configure)


scale_factor_x = float(canvas_width/math.ceil( float(x2_cord)))
scale_factor_y = float(canvas_height/math.ceil( float(y2_cord)))
print("scale factor X is: ",scale_factor_x)
print("y is : ",scale_factor_y)
x1_cord = scale_factor_x * math.ceil(float( x1_cord)) + 5
y1_cord = scale_factor_y * math.ceil( float(y1_cord)) + 5
x2_cord = scale_factor_x * math.ceil( float(x2_cord)) - 10
y2_cord = scale_factor_y * math.ceil( float(y2_cord)) - 10
a = midCanvas.create_rectangle(x1_cord,y1_cord,x2_cord,y2_cord,dash=(4,2))

midCanvas.create_text(canvas_width-50,10, text = "Width X Height")
canvas_info = midCanvas.create_text(canvas_width-50,30, text = str(canvas_width) + " X " + str(canvas_height))

#y axis
#midCanvas.create_line(5,5, 5, canvas_height - 10, dash=(4, 2), arrow=FIRST, state = DISABLED)
#x axis
#midCanvas.create_line(5,canvas_height - 10, canvas_width-10, canvas_height - 10, dash=(4, 2), arrow=LAST, state = DISABLED)
# x and y axis labels

midCanvas.create_text(14,canvas_height - 5, text = "  (0,0)")
midCanvas.create_text(30,10, text = "y-axis")
midCanvas.create_text(canvas_width-30 ,canvas_height - 5, text = "  x-axis")
midCanvas.pack(expand = YES, fill = BOTH)
#image2= PhotoImage(file = "gator.png")
#gator_image = midCanvas.create_image(450,335,image = image2, state = DISABLED )

image_upload= PhotoImage(file = "upload.png")
upload = image_upload.subsample(12,12)

#midCanvas.itemconfig(buttons_play,tags="canvasButtons")

for i in range(15, 0, -1):
    temp_j = 15-i
    llabels_no.append(Label(leftFrame, text=str(i)+'.', bg="dark slate gray", fg="white"))
    llabels_no[15-i].grid(row=15-i, column=1,padx=1,pady=8)

    lbuttons.append(Button(leftFrame,command=lambda temp_j=temp_j:browse_for_file(lbuttons[temp_j], buttons_upload, lbuttons_x, files, llabels, leftFrame, labels_play, load_src_b, load_src_b_m, buttons_play) ,text="Upload File "+ str(i), fg="white", bg = "dim gray", highlightbackground="black", relief="flat"))
    lbuttons[15-i].grid(row=15-i, column=2,padx=1,pady=8)

    llabels.append(Label(leftFrame, text="No File", fg = "white", bg = "dark slate gray", anchor=E, width = 8))
    llabels[15-i].grid(row=15-i, column=3,padx=1,pady=8)

    lbuttons_x.append(Button(leftFrame,command=lambda temp_j=temp_j:remove_file(lbuttons[temp_j]) ,text="X", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", state=DISABLED))
    lbuttons_x[15-i].grid(row=15-i, column=4,padx=1,pady=8)

    buttons_upload.append(Button(leftFrame, command=lambda temp_j=temp_j:manual_source(lbuttons[temp_j]), anchor = W, text="U", relief = FLAT, fg="white", bg="dim gray",highlightbackground="black", state=DISABLED))
    #buttons_play[i].configure(width = 30,height = 20, activebackground = "white", relief = FLAT, highlightbackground="white")
    buttons_upload[15-i].grid(row=15-i, column=5,padx=1,pady=8)

image_play= PhotoImage(file = "play.png")
play = image_play.subsample(10,10)


for i in range(0,15):
    buttons_play.append(Button(midFrame, text = "Play "+str(i),command=lambda i=i:play_sounds(buttons_play[i]), anchor = W, image = play, bg="white", relief = FLAT, highlightbackground="white"))
    #buttons_play[i].configure(width = 50,height = 34, activebackground = "white", relief = FLAT, highlightbackground="white")
    labels_play.append(Label(midFrame, text="None", bg="white", fg="black", state=DISABLED))


load_src_b = Button(leftFrame,command=lambda temp_j=temp_j:default_source() ,text="Load GUI(A)", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", state=DISABLED, width = 8)
load_src_b.grid(row=16, column = 2, padx=1,pady=8)

load_src_b_m = Button(leftFrame,command=lambda temp_j=temp_j:manual_source() ,text="Load GUI(M)", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", state=DISABLED, width = 8)
load_src_b_m.grid(row=16, column = 3, padx=10,pady=8)

rbutton1 = Button(rightFrame, text="Start", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton2 = Button(rightFrame, command=lambda:canvas_details(), text="Canvas Resize", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton3 = Button(rightFrame, text="Check Log", fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton4 = Button(rightFrame, command=lambda:remove_all_file(),text="Remove Files",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton5 = Button(rightFrame, command=lambda:default_sys(midFrame, files, llabels, load_src_b, buttons_play, labels_play, play, y2_cord),text="Default",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton6 = Button(rightFrame, command=lambda:random_trace(),text="Random Trace",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton7 = Button(rightFrame, command=lambda:square_trace(midCanvas, canvas_width, canvas_height),text="Square Trace",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton8 = Button(rightFrame, command=lambda:diagonal_trace(midCanvas, canvas_width, canvas_height),text="Diagonal Trace",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton9 = Button(rightFrame, command=lambda:real_time(),text="User Trace",fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)
rbutton10 = Button(rightFrame, text="Exit", command=root.destroy, fg="white", bg = "dim gray", highlightbackground="black", relief="flat", width=9)


rbutton1.grid(row=0, column=3,padx=1,pady=8)
rbutton2.grid(row=1, column=3,padx=1,pady=8)
rbutton3.grid(row=2, column=3,padx=1,pady=8)
rbutton4.grid(row=3, column=3,padx=1,pady=8)
rbutton5.grid(row=4, column=3,padx=1,pady=8)
rbutton6.grid(row=5, column=3,padx=1,pady=8)
rbutton7.grid(row=6, column=3,padx=1,pady=8)
rbutton8.grid(row=7, column=3,padx=1,pady=8)
rbutton9.grid(row=8, column=3,padx=1,pady=8)
rbutton10.grid(row=9, column=3,padx=1,pady=8)

#print(midCanvas.cget("width"))
#print(midCanvas.cget("height"))

#midCanvas.scale("all",0,0,canvas_width,canvas_height)
#image_pointer = PhotoImage(file = "pointer.png")
#image_pointer = image_pointer.subsample(30,30)

root.mainloop()
