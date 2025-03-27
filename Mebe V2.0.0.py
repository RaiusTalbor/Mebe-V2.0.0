# Motorsportmeisterschaftsberechner
# Mebe V2.0.0

import pickle
import random
import time
from tkinter import *
import MebeV1 as M1 #Mebe1-Integrierung
import Daten    #Lesen, Schreiben von Dateien


# ----------Hauptmenüknopffunktionen

# Idee: Knopf soll einen Stream öffnen, bei der alle hinterlegten Dateien gespeichert sind. Er soll alle anzeigen
# Über ein weiteres Menü Auswahl zur Bearbeitung, neu erstellen, neue Meisterschaft, Meisterschaften

# ----------pass

def test():
    pass   

#----------View

fenster = Tk()
fenster.title("Mebe V2.0.0")
fenster.geometry("800x600")

labelTitel = Label(master=fenster,
                   text="Mebe V2.0.0",
                   font=('', 18))
labelTitel.pack()

buttonSerien = Button(master=fenster,
                      text="Serien",
                      command=test)
buttonSerien.pack()

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

buttonErstellen = Button(master=fenster,
                         text="Erstellen",
                         command=test)
buttonErstellen.pack()

buttonBerechnen = Button(master=fenster,
                         text="Berechnen",
                         command=test)
buttonBerechnen.pack()

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

buttonImportieren = Button(master=fenster,
                       text="Importieren",
                       command=test)
buttonImportieren.pack()

buttonBeenden = Button(master=fenster,
                       text="Beenden",
                       command=test)
buttonBeenden.pack()

# ----------

fenster.mainloop()