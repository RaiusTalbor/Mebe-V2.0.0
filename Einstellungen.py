#Einstellungen für Mebe 2

#TODO: Speichert wohl nicht richtig

import pickle
from tkinter import *
import Daten

pfad = "Arbeitsdateien/Einstellungen/Einstellungen.dat"

#--------------------------------------------

fensterEinstellungen = Tk()
fensterEinstellungen.title("Einstellungen")
fensterEinstellungen.geometry("800x600")

labelTitel = Label(master=fensterEinstellungen,
                   text="Einstellungen",
                   font=('', 14))
labelTitel.pack()

#-------------------------------------------Einstellungen

#Einstellung, ob Ergebnis gespeichert werden soll oder nicht
Zwischenspeicher = Daten.lesen(pfad)
Ergebnisspeichern = Zwischenspeicher[0]

labelErgebnisspeichern = Label(master=fensterEinstellungen,
                          text="Soll das Ergebnis gespeichert werden?")
labelErgebnisspeichern.pack()

entryErgebnisspeichern = Entry(master=fensterEinstellungen,
                          text=Ergebnisspeichern)
entryErgebnisspeichern.pack()

#---------------------------------------------Speichern

def speichern():
    Einstellungen = []

    #liest Einstellung, ob Ergebnis gespeichert werden soll oder nicht
    Einstellungen.append(entryErgebnisspeichern.get())

buttonSpeichern = Button(master=fensterEinstellungen,
                        text="Speichern",
                        command=speichern)
buttonSpeichern.pack()

#-----------------------------------------------

fensterEinstellungen.mainloop()