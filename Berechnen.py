# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
#berechnet eine Meisterschaft und gibt das Ergebnis aus

import pickle
import random
import time
from tkinter import *
import MebeV1 as M1 #Mebe1-Integrierung
import Daten    #Lesen, Schreiben von Dateien

def berechnen():
    Berechnen = Toplevel()
    Berechnen.title("Berechnen - Mebe V2.0.0")
    Berechnen.geometry("800x600")

    labelTitel = Label(master=Berechnen,
                    text="Berechnen einer Meisterschaft",
                    font=('', 15))
    labelTitel.pack()

    #Auswahl der Meisterschaft

    #Berechnung