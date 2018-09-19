from pygame import *
from tkinter import *

#if __name__ == '__main__':
root = Tk()
root.title('Music Player')
root.configure(background='white')


def play(event):
    mixer.music.play()
    global bttn_clicks
    bttn_clicks = 0

def pause(event):
    global bttn_clicks
    bttn_clicks += 1
    if(bttn_clicks % 2 == 0):
        mixer.music.unpause()
    else:
        mixer.music.pause()
    print(bttn_clicks)

def stop(event):
    mixer.music.stop()
    global bttn_clicks
    bttn_clicks = 0

#def main():
bttn_clicks = 0
mixer.init()
mixer.music.load('1.wav')

image_play= PhotoImage(file = "play_mp.png")
image_play= image_play.subsample(7,7)

play_b = Button(root,text = 'Play', image=image_play, highlightbackground="white", relief="raised")
#play.place(x=20, y=15)
play_b.grid(row=0,column=1,padx=1,pady=8)

image_resume= PhotoImage(file = "resume.png")
image_resume= image_resume.subsample(7,7)

resume_b = Button(root,text = 'Pause', image=image_resume, highlightbackground="white", relief="raised")
#resume.place(x=30, y=15)
resume_b.grid(row=0,column=2,padx=1,pady=8)

image_stop= PhotoImage(file = "stop.png")
image_stop= image_stop.subsample(7,7)

stop_b = Button(root,text='Stop', image=image_stop, highlightbackground="white", relief="raised")
#stop.place(x=40, y=15)
stop_b.grid(row=0,column=3,padx=1,pady=8)

play_b.bind("<Button-1>",play)
resume_b.bind("<Button-1>",pause)
stop_b.bind("<Button-1>",stop)

#if __name__ == '__main__':
root.mainloop()
