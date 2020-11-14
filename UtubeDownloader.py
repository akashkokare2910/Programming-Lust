import os
from tkinter import *
root = Tk()
root.geometry('470x620')
def runit():
    os.startfile('link.bat')
def downloadvideo():
    with open('link.bat','w') as down_load:
        down_load.write(f'youtube-dl {link.get()}')
        down_load.close()
    runit()

frame = Frame(root)
frame.grid()
label1 = Label(frame,font=('Impact',18,'bold'),text ='**YOUTUBE VIDEO DIGITIZE**',fg='Salmon').pack()

frame1 = Frame(root)
frame1.grid()
Label(frame1,text = 'ENTER LINK HERE ',font=(' Comic Sans MS',15,'bold ')).grid(row=2)

link = StringVar()

entry = Entry(frame1,font = 7,textvariable=link).grid(row=2,column=1,pady=5,padx=10)

Btn1 = Button(frame1,text='DOWNLOAD',bd=6,fg='black',bg='white',relief=RAISED,font=10,borderwidth=7,command=downloadvideo)
Btn1.grid(column=1,pady=5)

root.mainloop()
