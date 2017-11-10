import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from classes import Api

api = Api.Api()

stations_names = api.get_station_names()
nameAndPassword = api.get_nameAndPassword()

def clear_text_entry_1():
    """Clear text after input of the user"""
    entry_1.delete(0, 'end')

def clear_text_entry_2():
    """Clear text after input of the user"""
    entry_2.delete(0, 'end')

def get_url():
    """Return the URL of the API"""
    word1 = startstation(stations_names).replace(" ", "+")
    word2 = endstation(stations_names).replace(" ", "+")

    url_times = "http://webservices.ns.nl/ns-api-treinplanner?fromStation=" + str(word1) + "&toStation=" + str(word2) + "&departure=true"

    return url_times

def startstation(stations_names):
    """User inputs his station where he/she wants to departure"""
    while True:
        start_station = entry_1.get()
        if start_station in stations_names:
            return start_station
        else:
            print('Verkeerde invoer')
            exit()


def endstation(stations_names):
    """User inputs his station of destination"""
    while True:
        endstation = entry_2.get()
        if endstation in stations_names:
            return endstation
        else:
            print('Verkeerde invoer')
            exit()

def get_result():
    """Using the URL of the API.
    1. Parse into the XML-file
    2. Make use of a for loop
    3. Getting to right data
    4. Print the data for user
    """
    import xmltodict
    import requests

    url = str(get_url())

    naamEnWachtwoord = nameAndPassword
    response = requests.get(url, auth=naamEnWachtwoord)
    xmltodict = xmltodict.parse(response.content)

    return xmltodict

def TrajectInfo():
    """GUI results for the user"""
    root = Toplevel()
    root.title('Reisoverzicht')
    root.wm_minsize(width=1800, height=720)
    screen_width = 2800
    screen_height = 720

    # custom colors
    background_yellow = '#FFCC18'
    ns_blue = '#322E9C'

    # Title styles
    # main title
    def main_title():
        """Fonts that are in use"""
        return (('Open Sans', 48, 'bold'))

    # text bold
    def text_bold():
        """Fonts that are in use"""
        return (('Open Sans', 12, 'bold'))

    # text light
    def text_light():
        """Fonts that are in use"""
        return (('Open Sans', 12))

    # top frame
    topFrame = Frame(master=root)
    topFrame.pack(side=TOP)
    topField = Frame(master=topFrame, bg=background_yellow, width=1800, height=100)
    topField.pack(fill=BOTH)

    # main frame
    mainFrame = Frame(master=root)
    mainFrame.pack()
    mainField = Frame(master=mainFrame, bg=background_yellow, width=1800, height=520)
    mainField.pack(fill=BOTH)

    # bottom frame
    bottomFrame = Frame(master=root)
    bottomFrame.pack(side=BOTTOM)
    bottomField = Frame(master=bottomFrame, bg=background_yellow, width=1800, height=200)
    bottomField.pack(fill=BOTH)

    logo = Image.open("nslogo.png")
    tkimage = ImageTk.PhotoImage(logo)
    tk.Label(topFrame, bg=background_yellow, image=tkimage).place(x=30, y=25)

    # title
    title = Label(master=topFrame, text="Reisoverzicht", fg=ns_blue, bg=background_yellow, font=main_title())
    title.place(x=600, y=25, width=500)

    # reisoverzicht
    y = 30
    frames = []
    for index, time in enumerate(get_result()['ReisMogelijkheden']['ReisMogelijkheid']):

        tempname = str(index) + "test"
        tempname = Frame(master=mainFrame, bg="white")

        # blue stripe
        Frame_label = Label(master=tempname, bg=ns_blue, height=100)
        Frame_label.pack(side=LEFT)

        # Starttime
        Frame_label_text_start = Label(master=tempname, text= time['GeplandeVertrekTijd'][11:16]+ "    > ", bg="white", padx=5, fg=ns_blue, font=text_bold())
        Frame_label_text_start.pack(side=LEFT)

        # arrow
        #arrow = Image.open("arrow.png")
        #icon = ImageTk.PhotoImage(arrow)
        #tk.Label(master=tempname, image=icon).pack(side=LEFT)

        # Endttime
        Frame_label_text_end = Label(master=tempname, text=time['GeplandeAankomstTijd'][11:16], bg="white", padx=5, fg=ns_blue, font=text_bold())
        Frame_label_text_end.pack(side=LEFT)

        # Overstap
        Frame_label_text_track = Label(master=tempname, text="Overstap: " + time['AantalOverstappen'], bg="white", padx=5, fg=ns_blue, font=text_light())
        Frame_label_text_track.pack(side=RIGHT)

        # Reistijd
        Frame_label_text_track = Label(master=tempname, text="Reistijd: " + time['GeplandeReisTijd'], bg="white", padx=5, fg=ns_blue, font=text_light())
        Frame_label_text_track.pack(side=RIGHT)

        if time['AantalOverstappen'] > '0':
            for ReisDeel in time['ReisDeel']:
                # # Ritnummer
                # Frame_label_text_track = Label(master=tempname, text="Ritnummer: " + ReisDeel['RitNummer'], bg="white", padx=20, fg=ns_blue, font=text_light())
                # Frame_label_text_track.pack(side=BOTTOM)
                #
                # Vervoertype
                Frame_label_text_track = Label(master=tempname, text=ReisDeel['VervoerType'], bg="white", padx=4, fg=ns_blue, font=('arial', 10))
                Frame_label_text_track.pack(side=LEFT)

                try:
                    for ReisStop in ReisDeel['ReisStop']:
                        # Naam
                        # Naam
                        Frame_label_text_track = Label(master=tempname, text=ReisStop['Naam'], bg="white", padx=4, fg=ns_blue, font=('arial', 10))
                        Frame_label_text_track.pack(side=LEFT)
                        # Frame_label_text_track = Label(master=tempname, text="Station: " + ReisStop['Naam'], bg="white", padx=20, fg=ns_blue, font=text_light())
                        # Frame_label_text_track.pack(side=LEFT)

                        # Tijd
                        Frame_label_text_track = Label(master=tempname, text=ReisStop['Tijd'][11:16], bg="white", padx=4, fg=ns_blue, font=('arial', 10))
                        Frame_label_text_track.pack(side=LEFT)

                        if 'Spoor' in ReisStop:
                            # spoor
                            Frame_label_text_track = Label(master=tempname, text="spoor:" + ReisStop['Spoor']['#text'] + "   ", bg="white", padx=4, fg=ns_blue, font=('arial', 10))
                            Frame_label_text_track.pack(side=LEFT)

                except TypeError:
                    continue
        else:
            # # Ritnummer
            # Frame_label_text_track = Label(master=tempname, text="Ritnummer: " + time['ReisDeel']['RitNummer'], bg="white", padx=20, fg=ns_blue, font=text_light())
            # Frame_label_text_track.pack(side=BOTTOM)
            #
            # Vervoertype
            Frame_label_text_track = Label(master=tempname, text=time['ReisDeel']['VervoerType'], bg="white", padx=4, fg=ns_blue, font=('arial', 10))
            Frame_label_text_track.pack(side=LEFT)

            try:
                for ReisStop in time['ReisDeel']['ReisStop']:
                    # Naam
                    Frame_label_text_track = Label(master=tempname, text=ReisStop['Naam'], bg="white", padx=4, fg=ns_blue, font=('arial', 10))
                    Frame_label_text_track.pack(side=LEFT)

                    # Tijd
                    Frame_label_text_track = Label(master=tempname, text=ReisStop['Tijd'][11:16], bg="white", padx=4, fg=ns_blue, font=('arial', 10))
                    Frame_label_text_track.pack(side=LEFT)
                    if 'Spoor' in ReisStop:
                        # spoor
                        Frame_label_text_track = Label(master=tempname, text="spoor:" + ReisStop['Spoor']['#text'] + "   ", bg="white", padx=4, fg=ns_blue, font=('arial', 10))
                        Frame_label_text_track.pack(side=LEFT)
            except TypeError:
                continue
        frames.append(tempname)

    # Nog een for loop, die de frames plaatst
    for frame in frames:
        frame.place(x=30, y=y, width=1600, height=50)
        y += 70
        # print('ActueleReisTijd: ' + time['ActueleReisTijd'])
        # print('ActueleVertrekTijd: ' + time['ActueleVertrekTijd'][11:16])
        # print('ActueleAankomstTijd: ' + time['ActueleAankomstTijd'][11:16])

    # keep running untill close
    root.mainloop()

def clear_all():
    """Clears the first GUI, open the results GUI"""
    get_result()
    TrajectInfo()

root = Tk()
root.title("NS Reisplanner")
root.wm_minsize(width=1280, height=720)

# custom colors
background_yellow = '#FFCC18'
ns_blue = '#322E9C'

# Title styles
# main title
def main_title():
    return (('Open Sans', 48, 'bold'))

# text bold
def text_bold():
    return (('Open Sans', 16, 'bold'))

# text light
def text_light():
    return (('Open Sans', 16))

screen_width = 1280
screen_height = 720

# icons
icon_cross = Image.open("cross.png")

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
entry_label1 = Label(master=entry_1, text="Van:",bg='white' , padx=20, fg=ns_blue ,font=text_bold())
entry_label1.pack(side=LEFT)
# Clear text button
icon_button = ImageTk.PhotoImage(icon_cross)
entry_label_button1 = Button(master=entry_1, bg="white", borderwidth=0, width=20, height=20,image=icon_button, command=clear_text_entry_1)
entry_label_button1.pack(side=RIGHT, padx=10)


entry_1.insert(0, "Voer het beginstation in")
entry_1.place(x=390, y=150, width=500, height=50)

# eindstation
entry_2 = Entry(master=mainFrame, bg="white", justify='center', fg="black", font=text_light())
entry_label2 = Label(master=entry_2, text="Naar:",bg='white' , padx=20, fg=ns_blue ,font=text_bold())
entry_label2.pack(side=LEFT)
# Clear text button
icon_button2 = ImageTk.PhotoImage(icon_cross)
entry_label_button2 = Button(master=entry_2, bg="white", borderwidth=0, width=20, height=20, image=icon_button2, command=clear_text_entry_2)
entry_label_button2.pack(side=RIGHT, padx=10)

entry_2.insert(0, 'Voer het eindstation in')
entry_2.place(x=390, y=225, width=500, height=50)


# reisplanner button
button1 = Button(master=bottomFrame, text="Plan je reis", relief=FLAT, bg=ns_blue, fg="white", font=text_light(), command=clear_all)
button1.place(x=565, y=20, width=150, height=50)

# keep running untill close
root.mainloop()