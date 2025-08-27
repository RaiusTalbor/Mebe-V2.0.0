# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Untermenü Meisterschaften - zeigt Meisterschaften an, bearbeiten können

import pickle
import random
import time
from tkinter import *
import MebeV1 as M1 #Mebe1-Integrierung
import Daten    #Lesen, Schreiben von Dateien
import os

def Meisterschaften():
    fensterMeisterschaften = Toplevel()
    fensterMeisterschaften.title("Meisterschaften - Mebe V2.0.0")
    fensterMeisterschaften.geometry("800x600")

    #Frames
    frameInfo = Frame(fensterMeisterschaften)
    #frameButtons = Frame(fensterMeisterschaften)
    frameInteraktion = Frame(fensterMeisterschaften)
    frameInfo.pack()
    #frameButtons.pack()
    frameInteraktion.pack()

    labelTitelMeisterschaften = Label(master=frameInfo,
                   text="Meisterschaften",
                   font=('', 15))
    labelTitelMeisterschaften.pack()

    VerzeichnisMeisterschaftenohnefilter = os.listdir('Datenbank')
    VerzeichnisMeisterschaften = []

    #für alle Dateien, die nicht auf 'Strecken.dat' oder 'Fahrer.dat', aber auf '.dat' enden, wird zur Liste hinzugefügt
    for i in range(0, len(VerzeichnisMeisterschaftenohnefilter)):
        if (not VerzeichnisMeisterschaftenohnefilter[i].endswith('Fahrer.dat') 
            and not VerzeichnisMeisterschaftenohnefilter[i].endswith('Strecken.dat') 
            and VerzeichnisMeisterschaftenohnefilter[i].endswith('.dat')):

            VerzeichnisMeisterschaften.append(VerzeichnisMeisterschaftenohnefilter[i])

    meisterschaft = StringVar()
    #zeige alle Meisterschaften als Button an
    for i in range(0, len(VerzeichnisMeisterschaften)):

        #richtige Anzeige ohne .dat
        anzeige = VerzeichnisMeisterschaften[i]
        anzeige = anzeige.replace('.dat', '')

        radiobuttonMeisterschaft = Radiobutton(master=frameInteraktion, text=f"{anzeige}", 
                                               value=VerzeichnisMeisterschaften[i], variable = meisterschaft)
        radiobuttonMeisterschaft.pack()

    meisterschaft.set(VerzeichnisMeisterschaften[0])

    #Aktionsbuttons hier einfügen