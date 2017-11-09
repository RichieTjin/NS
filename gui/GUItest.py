from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

from main import get_result

root = Tk()
root.title('Reisoverzicht')
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

# title
title = Label(master=topFrame, text="Reisoverzicht", fg=ns_blue, bg=background_yellow, font=main_title())
title.place(x=390,y=25, width=500)

# reisoverzicht

y = 220
frames = []
for index, time in enumerate(get_result()['ReisMogelijkheden']['ReisMogelijkheid']):
    print(index)
    tempname = str(index) + "test"
    tempname = Frame(master=mainFrame, bg="white")
    # blue stripe
    Frame_label = Label(master=tempname, bg=ns_blue, height=50)
    Frame_label.pack(side=LEFT)
    # Starttime
    Frame_label_text_start = Label(master=tempname, text=time['GeplandeVertrekTijd'][11:16], bg="white", padx=20, fg=ns_blue, font=text_bold())
    Frame_label_text_start.pack(side=LEFT)
    # Endttime
    Frame_label_text_end = Label(master=tempname, text=time['GeplandeAankomstTijd'][11:16], bg="white", padx=20, fg=ns_blue, font=text_bold())
    Frame_label_text_end.pack(side=LEFT)
    # spoor
    Frame_label_text_track = Label(master=tempname, text="spoor: 4", bg="white", padx=20, fg=ns_blue, font=text_light())
    Frame_label_text_track.pack(side=RIGHT)
    # Hier frame in de lijst stoppen
    frames.append(tempname)

#Nog een for loop, die de frames plaatst
for frame in frames:
    frame.place(x=390, y=y, width=500, height=50)
    y+=100
    # print('AantalOverstappen: ' + time['AantalOverstappen'])
    # print('GeplandeReisTijd: ' + time['GeplandeReisTijd'])
    # print('ActueleReisTijd: ' + time['ActueleReisTijd'])
    # print('ActueleVertrekTijd: ' + time['ActueleVertrekTijd'][11:16])
    # print('ActueleAankomstTijd: ' + time['ActueleAankomstTijd'][11:16])
    #
    # if time['AantalOverstappen'] > '0':
    #     for ReisDeel in time['ReisDeel']:
    #         print('Ritnummer: ' + ReisDeel['RitNummer'])
    #         print('VervoerType: ' + ReisDeel['VervoerType'])
    #         print('Vervoerder: ' + ReisDeel['Vervoerder'])
    #
    #         try:
    #             for ReisStop in ReisDeel['ReisStop']:
    #                 print('Station: ' + ReisStop['Naam'])
    #                 print('Tijd: ' + ReisStop['Tijd'][11:16])
    #                 if 'Spoor' in ReisStop:
    #                     print('Spoor: ' + ReisStop['Spoor']['#text'])
    #
    #         except TypeError:
    #             continue
    # else:
    #     print('Ritnummer: ' + time['ReisDeel']['RitNummer'])
    #     print('VervoerType: ' + time['ReisDeel']['VervoerType'])
    #     print('Vervoerder: ' + time['ReisDeel']['Vervoerder'])
    #
    #     try:
    #         for ReisStop in time['ReisDeel']['ReisStop']:
    #             print('Station: ' + ReisStop['Naam'])
    #             print('Tijd: ' + ReisStop['Tijd'][11:16])
    #             if 'Spoor' in ReisStop:
    #                 print('Spoor: ' + ReisStop['Spoor']['#text'])
    #     except TypeError:
    #         continue

# arrow
# Frame2_label_icon = Image.open("arrow.png")
# icon = ImageTk.PhotoImage(Frame2_label_icon)
# tk.Label(master=Frame2_label_text, image=tkimage, bg="red").pack(side=RIGHT)



# reisplanner button
button1 = Button(master=bottomFrame, text="Wijzig je reis", relief=FLAT, bg=ns_blue, fg="white", font=text_light())
button1.place(x=565, y=20, width=150, height=50)

# keep running untill close
root.mainloop()