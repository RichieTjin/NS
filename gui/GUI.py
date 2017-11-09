from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

from classes import Api

root = Tk()
root.title("NS Reisplanner")
root.wm_minsize(width=1280, height=720)

screen_width = 1280
screen_height = 720

# custom colors
background_yellow = '#FFCC18'
ns_blue = '#322E9C'

# icons
icon_cross = Image.open("cross.png")

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

# NS logo
logo = Image.open("nslogo.png")
tkimage = ImageTk.PhotoImage(logo)
tk.Label(topFrame, bg=background_yellow, image=tkimage).place(x=30, y=25)

# title
title = Label(master=topFrame, text="NS Reisplanner", fg=ns_blue, bg=background_yellow, font=main_title())
title.place(x=390,y=25, width=500)

# beginstation
entry_1 = Entry(master=mainFrame, justify='center', fg="black", font=text_light())
entry_label1 = Label(master=entry_1, text="Van:", padx=20, fg=ns_blue ,font=text_bold())
entry_label1.pack(side=LEFT)
# Clear text button
icon_button = ImageTk.PhotoImage(icon_cross)
entry_label_button1 = Button(master=entry_1, bg="white", borderwidth=0, width=20, height=20, image=icon_button)
entry_label_button1.pack(side=RIGHT)

entry_1.insert(0, "Voer het beginstation in")
entry_1.place(x=390, y=150, width=500, height=50)

# eindstation
entry_2 = Entry(master=mainFrame, bg="white", justify='center', fg="black", font=text_light())
entry_label2 = Label(master=entry_2, text="Naar:", padx=20, fg=ns_blue ,font=text_bold())
entry_label2.pack(side=LEFT)
# Clear text button
icon_button2 = ImageTk.PhotoImage(icon_cross)
entry_label_button2 = Button(master=entry_2, bg="white", borderwidth=0, width=20, height=20, image=icon_button2)
entry_label_button2.pack(side=RIGHT)

entry_2.insert(0, 'Voer het eindstation in')
entry_2.place(x=390, y=225, width=500, height=50)

# reisplanner button
button1 = Button(master=bottomFrame, text="Plan je reis", relief=FLAT, bg=ns_blue, fg="white", font=text_light())
button1.place(x=565, y=20, width=150, height=50)

# keep running untill close
root.mainloop()