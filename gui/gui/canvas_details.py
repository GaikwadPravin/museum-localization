from tkinter import *

def show_canvas():
   print(int(canvas_width.get()), int(canvas_height.get()))
   midCanvas = Canvas(master, width=canvas_width.get(), height=canvas_height.get(), bg = "white")

master = Tk()


#Label(master, text="First Name").grid(row=0)
#Label(master, text="Last Name").grid(row=1)

Label(master, text="Canvas Width").grid(row=0)
Label(master, text="Canvas Height").grid(row=1)

canvas_width = Entry(window)
canvas_height = Entry(window)

canvas_width.grid(row=0, column=1)
canvas_height.grid(row=1, column=1)


Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=lambda:show_canvas().grid(row=3, column=1, sticky=W, pady=4)

master.mainloop()
