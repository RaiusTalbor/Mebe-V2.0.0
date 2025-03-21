# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Untermenü Meisterschaften - zeigt Meisterschaften an, bearbeiten können

import pickle
import random
import time
from tkinter import *
import MebeV1 as M1 #Mebe1-Integrierung
import Daten    #Lesen, Schreiben von Dateien

def test():
    pass

def Meisterschaften():
    fensterMeisterschaften = Tk()
    fensterMeisterschaften.title("Meisterschaften - Mebe V2.0.0")
    fensterMeisterschaften.geometry("800x600")

    labelTitelMeisterschaften = Label(master=fensterMeisterschaften,
                   text="Meisterschaften",
                   font=('', 15))
    labelTitelMeisterschaften.pack()

    f = open("Datenbank/000 - VerzeichnisMeisterschaften.dat", mode='rb')
    VerzeichnisMeisterschaften = pickle.load(f)
    f.close()

    for i in range(0, len(VerzeichnisMeisterschaften)):
        buttonBeenden = Button(master=fensterMeisterschaften,
                       text="Beenden",
                       command=test)
        buttonBeenden.pack()

    fensterMeisterschaften.mainloop()

Meisterschaften()

