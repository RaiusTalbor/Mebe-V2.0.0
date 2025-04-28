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
import Berechnen

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

# Hauptmenü - Steuereinheit Mebe V2 ------------------------------------------

#buttonSerien = Button(master=fenster,
#                      text="Serien",
#                      command=test)
#buttonSerien.pack()

# alle ansehen und bearbeiten
buttonMeisterschaften = Button(master=fenster,
                               text="Meisterschaften",
                               command=test)
buttonMeisterschaften.pack()

buttonStrecken = Button(master=fenster,
                        text="Strecken",
                        command=test)
buttonStrecken.pack()

buttonFahrzeuge = Button(master=fenster,
                         text="Fahrzeuge",
                         command=test)
buttonFahrzeuge.pack()

buttonFahrer = Button(master=fenster,
                      text="Fahrer",
                      command=test)
buttonFahrer.pack()

#erstellen einer Meisterschaft
buttonErstellen = Button(master=fenster,
                         text="Erstellen",
                         command=Erstellen.erstellen)
buttonErstellen.pack()

#berechnen einer Meisterschaft
buttonBerechnen = Button(master=fenster,
                         text="Berechnen",
                         command=Berechnen.berechnen)
buttonBerechnen.pack()

#Hilfe zu Mebe
buttonHilfe = Button(master=fenster,
                     text="Hilfe",
                     command=test)
buttonHilfe.pack()

# Mebe 2 hat Mebe 1 implementiert, was bedeutet, dass Mebe 1 in Mebe 2 integriert und unabhängig funktioniert
# die alten Daten und das vereinfachte Programm können verwendet werden
buttonMebe1 = Button(master=fenster,
                       text="Mebe 1",
                       command=M1.RunMebe)
buttonMebe1.pack()

#Programm beenden
buttonBeenden = Button(master=fenster,
                       text="Beenden",
                       command=test)
buttonBeenden.pack()

# ----------------------------------------------------------------------------

fenster.mainloop()