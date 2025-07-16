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

    labelTitelErstellen = Label(master=fensterBearbeiten,
                    text="Bearbeiten von Daten - bitte auswählen",
                    font=('', 15))
    labelTitelErstellen.pack()

    buttonMeisterschaft = Button (fensterBearbeiten, text = "Meisterschaft bearbeiten", command = Erstellen.bearbeiten)
    buttonMeisterschaft.pack()

    buttonStrecke = Button (fensterBearbeiten, text = "Strecke bearbeiten", command = ErstelleStrecke.bearbeiten)
    buttonStrecke.pack()

    buttonFahrer = Button (fensterBearbeiten, text = "Fahrer bearbeiten", command = ErstelleFahrer.bearbeiten)
    buttonFahrer.pack()

    buttonFahrzeug = Button (fensterBearbeiten, text = "Fahrzeug bearbeiten", command = ErstelleFahrzeug.bearbeiten)
    buttonFahrzeug.pack()