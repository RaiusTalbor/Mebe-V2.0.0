# Motorsportmeisterschaftsberechner
# Mebe V2.0.0

import pickle
import random
import time
from tkinter import *
import Daten    #Lesen, Schreiben von Dateien

#Mebe-Module und Funktionen
import MebeV1 as M1 #Mebe1-Integrierung
import Erstellen
import Bearbeiten
import Berechnen

# ----------Knopffunktionen

#beendet das Program sauber
def beenden():
    labelInfo.config(text="Mebe V2.0.0 wird beendet! Auf Wiedersehen!")
    labelInfo.update_idletasks()
    time.sleep(1)
    fenster.destroy()

# ----------pass für Testzwecke

def test():
    pass   

# ----------View

fenster = Tk()
fenster.title("Mebe V2.0.0")
fenster.geometry("800x600")

labelTitel = Label(master=fenster,
                   text="Mebe V2.0.0",
                   font=('', 18))
labelTitel.pack()

# ----------Frames

#frameTitel = Frame(master=fenster)
#frameTitel.pack()

frameButtons = Frame(master=fenster)
frameButtons.pack()

frameInfo = Frame(master=fenster)
frameInfo.pack()

# Hauptmenü - Steuereinheit Mebe V2 ------------------------------------------

#buttonSerien = Button(master=fenster,
#                      text="Serien",
#                      command=test)
#buttonSerien.pack()

# alle ansehen und bearbeiten
#buttonMeisterschaften = Button(master=fenster,
#                               text="Meisterschaften",
#                               command=test)
#buttonMeisterschaften.pack()

#buttonStrecken = Button(master=fenster,
#                        text="Strecken",
#                        command=test)
#buttonStrecken.pack()

#buttonFahrzeuge = Button(master=fenster,
#                         text="Fahrzeuge",
#                         command=test)
#buttonFahrzeuge.pack()

#buttonFahrer = Button(master=fenster,
#                      text="Fahrer",
#                      command=test)
#buttonFahrer.pack()

#erstellen einer Meisterschaft
buttonErstellen = Button(master=frameButtons,
                         text="Erstellen",
                         command=Erstellen.erstellen)
buttonErstellen.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

buttonBearbeiten = Button(master=frameButtons,
                         text="Bearbeiten",
                         command=Bearbeiten.bearbeiten)
buttonBearbeiten.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

#berechnen einer Meisterschaft
buttonBerechnen = Button(master=frameButtons,
                         text="Berechnen",
                         command=Berechnen.berechnen)
buttonBerechnen.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

#Hilfe zu Mebe
buttonHilfe = Button(master=frameButtons,
                     text="Hilfe",
                     command=test)
buttonHilfe.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

# Mebe 2 hat Mebe 1 implementiert, was bedeutet, dass Mebe 1 in Mebe 2 integriert und unabhängig funktioniert
# die alten Daten und das vereinfachte Programm können verwendet werden
#buttonMebe1 = Button(master=frameButtons,
#                       text="Mebe 1",
#                       command=M1.RunMebe)
#buttonMebe1.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

#Programm beenden
buttonBeenden = Button(master=frameButtons,
                       text="Beenden",
                       command=beenden)
buttonBeenden.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

# ----------------------------------------------------------------------------

labelInfo = Label(frameInfo, text="", font=('', 15))
labelInfo.pack()

fenster.mainloop()