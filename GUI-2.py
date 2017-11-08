from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

root = Tk()
root.title("Reisoverzicht")
root.wm_minsize(width=1280, height=720)

screen_width = 1280
screen_height = 720

# custom colors
background_yellow = '#FFCC18'
ns_blue = '#322E9C'

# Title styles
# main title
def main_title():
    return(('Open Sans', 48, 'bold'))

# text bold
def text_bold():
    return(('Open Sans', 16, 'bold'))

#text light
def text_light():
    return(('Open Sans', 16))

# top frame
topFrame = Frame(master=root)
topFrame.pack(side=TOP)
topField = Frame(master=topFrame, bg=background_yellow, width=1280, height=100)
topField.pack(fill=BOTH)

# main frame
mainFrame = Frame(master=root)
mainFrame.pack()
mainField = Frame(master=mainFrame, bg=background_yellow, width=1280, height=520)
mainField.pack(fill=BOTH)

# bottom frame
bottomFrame = Frame(master=root)
bottomFrame.pack(side=BOTTOM)
bottomField = Frame(master=bottomFrame, bg=background_yellow, width=1280, height=100)
bottomField.pack(fill=BOTH)

logo = Image.open("nslogo.png")
tkimage = ImageTk.PhotoImage(logo)
tk.Label(topFrame, bg=background_yellow, image=tkimage).place(x=30, y=25)

# top logo
# ns_logo = PhotoImage(file='nslogo.png')
# label = Label(root, image=ns_logo)
# label.pack()

# title
title = Label(master=topFrame, text="Reisoverzicht", fg=ns_blue, bg=background_yellow, font=main_title())
title.place(x=390,y=25, width=500)

# reisoverzicht
Frame1 = Frame(master=mainFrame, bg="white")
Frame1_label = Label(master=Frame1, bg=ns_blue, height=50)
Frame1_label.pack(side=LEFT)
Frame1.place(x=390, y=150, width=500, height=50)

# reisoverzicht 2
Frame2 = Frame(master=mainFrame, bg="white")
# blue stripe
Frame2_label = Label(master=Frame2, bg=ns_blue, height=50)
Frame2_label.pack(side=LEFT)
Frame2_label_text = Label(master=Frame2, text="13:37", bg="white", padx=20, fg=ns_blue, font=text_bold())
Frame2_label_text.pack(side=LEFT)
Frame2.place(x=390, y=220, width=500, height=50)

# reisplanner button
button1 = Button(master=bottomFrame, text="Plan je reis", relief=FLAT, bg=ns_blue, fg="white", font=text_light())
button1.place(x=565, y=20, width=150, height=50)

# keep running untill close
root.mainloop()