# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Untermenü bearbeiten - Meisterschaften, Strecken, Fahrer, Fahrzeuge editieren

import time
from tkinter import *
import Daten        #Lesen, Schreiben von Dateien
import os

#---
import Erstellen
import ErstelleStrecke
import ErstelleFahrer
import ErstelleFahrzeug

def test():
    pass

def bearbeiten():
    fensterBearbeiten = Toplevel()
    fensterBearbeiten.title("Bearbeiten - Mebe V2.0.0")
    fensterBearbeiten.geometry("800x600")

    #Frames
    frameInfo = Frame(master=fensterBearbeiten)
    frameButtons = Frame(master=fensterBearbeiten)
    frameInfo.pack()
    frameButtons.pack()

    labelTitelErstellen = Label(master=frameInfo,
                    text="Bearbeiten von Daten - bitte auswählen",
                    font=('', 15))
    labelTitelErstellen.pack()

    buttonMeisterschaft = Button (frameButtons, text = "Meisterschaft bearbeiten", command = Erstellen.bearbeiten)
    buttonMeisterschaft.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

    buttonStrecke = Button (frameButtons, text = "Strecke bearbeiten", command = ErstelleStrecke.bearbeiten)
    buttonStrecke.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

    buttonFahrer = Button (frameButtons, text = "Fahrer bearbeiten", command = ErstelleFahrer.bearbeiten)
    buttonFahrer.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

    buttonFahrzeug = Button (frameButtons, text = "Fahrzeug bearbeiten", command = ErstelleFahrzeug.bearbeiten)
    buttonFahrzeug.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

    buttonZurück = Button (frameButtons, text = "Zurück", command = fensterBearbeiten.destroy)
    buttonZurück.pack(side=LEFT, anchor=N, padx= 20, pady = 20)