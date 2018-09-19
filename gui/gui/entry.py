from tkinter import *

def show_entry_fields():
   print(int(x.get()), int(y.get()), int(r.get()))

master = Tk()
window = Toplevel(master)
window.title('User Input')

#Label(master, text="First Name").grid(row=0)
#Label(master, text="Last Name").grid(row=1)

Label(window, text="x co-ordinate").grid(row=0)
Label(window, text="y co-ordinate").grid(row=1)
Label(window, text="orientation").grid(row=2)

x = Entry(window)
y = Entry(window)
r = Entry(window)

#e1 = Entry(master)
#e2 = Entry(master)

x.grid(row=0, column=1)
y.grid(row=1, column=1)
r.grid(row=2, column=1)

Button(window, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(window, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
