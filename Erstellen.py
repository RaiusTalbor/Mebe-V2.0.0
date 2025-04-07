# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Untermenü erstellen - ermöglicht das Erstellen einer komplett neuen Meisterschaft

import pickle
import random
import time
from tkinter import *
import MebeV1 as M1 #Mebe1-Integrierung
import Daten    #Lesen, Schreiben von Dateien
import ErstelleStrecke
import ErstelleFahrer
import os

def hinzufügen():
    #fügt Radiobutton-Auswahl hinzu

    global varweiter
    
    if varweiter == 1:
        auswahl = radioStrecken.get()

        rennkalender = Daten.lesen(meisterschaftspfad)

        rennkalender.append(auswahl)

        Daten.schreiben(meisterschaftspfad, rennkalender)
    
    if varweiter == 2:
        auswahl = radioFahrer.get()

        fahrerliste = Daten.lesen(meisterschaftspfad)

        fahrerliste.append(auswahl)

        Daten.schreiben(meisterschaftspfad, fahrerliste)

def neuehinzufügen():
    #fügt entweder neuen Fahrer oder neue Strecke ein
    
    global varweiter

    if varweiter == 1:
        ErstelleFahrer.erstellen()
    if varweiter == 2:
        ErstelleStrecke.erstellen()

#zeigt jeweils das neue Fenster mit den neuen Einstellungen an
def weiter():
    global varweiter
    global textStrecke
    global textFahrer
    global meisterschaftspfad

    if varweiter == 0:
        meisterschaftspfad = entryNameeinfügen.get()

    varweiter += 1

    #Fenster 2 - Strecken hinzufügen
    if varweiter == 1:
        labelTitelErstellen.config(text = "Erstellen einer Meisterschaft - Strecken hinzufügen")
        #Hinweis: In Reihenfolge des Rennkalenders

        #listeStrecken = Daten.lesen('Datenbank/Strecken/000 - Verzeichnis Strecken.dat')
        listeStrecken = os.listdir('Datenbank/Strecken')

        #für jedes Element der Liste (also alle Strecken) wird ein Radiobutton erzeugt
        for i in range(0, len(listeStrecken)):
            #formated String in Radiobutton wird gesetzt
            textStrecke = listeStrecken[i]
            radioStrecken.pack()

        buttonhinzufügen.pack()
        buttonneuehinzufügen.pack()

    #Fenster 3 - Fahrer hinzufügen
    elif varweiter == 2:
        labelTitelErstellen.config(text = "Erstellen einer Meisterschaft - Fahrer hinzufügen")

        #listeFahrer = Daten.lesen('Datenbank/Fahrer/000 - Verzeichnis Fahrer.dat')
        listeFahrer = os.listdir('Datenbank/Fahrer')

        #für jedes Element der Liste (also alle Fahrer) wird ein Radiobutton erzeugt
        for i in range(0, len(listeFahrer)):
            #formated String in Radiobutton wird gesetzt
            textFahrer = listeFahrer[i]
            radioFahrer.pack()

        buttonhinzufügen.config(text = "Fahrer hinzufügen")
        buttonneuehinzufügen.config(text = "neue Fahrer erstellen")

    #Fenster 4 - Fertigstellen und Exit
    elif varweiter == 3:
        fensterErstellenFertig = Tk()
        fensterErstellenFertig.title("Fertig - Mebe V2.0.0")
        fensterErstellenFertig.geometry("200x300")

        labelTitelErstellenFertig = Label(master=fensterErstellenFertig,
                           text="Erstellt!",
                           font=('', 15))
        labelTitelErstellenFertig.pack()

        time.sleep(2)

        varweiter == 0

        fensterErstellenFertig.destroy()

        fensterErstellenFertig.mainloop() #geht das so??

        global fensterErstellen
        fensterErstellen.destroy()

#das, was beim öffnen des Fensters angezeigt werden soll
def ansicht0():
    labelNameeinfügen.pack()
    entryNameeinfügen.pack()

    labelSerieeinfügen.pack()
    entrySerieeinfügen.pack()

    labelJahreinfügen.pack()
    entryJahreinfügen.pack()

#Anzeigen ----------------------------------------------------------

#Initialisierung ----------

#weiter 0...Pflichtdaten; weiter 1...Strecken; weiter 2...Fahrer
varweiter = 0
meisterschaftspfad = ""

fensterErstellen = Tk()
fensterErstellen.title("Erstellen - Mebe V2.0.0")
fensterErstellen.geometry("800x600")

labelTitelErstellen = Label(master=fensterErstellen,
                   text="Erstellen einer Meisterschaft",
                   font=('', 15))
labelTitelErstellen.pack()

#Entries ----------
# Name der Meisterschaft

labelNameeinfügen = Label(master = fensterErstellen,
                          text = "Name der Meisterschaft")
labelSerieeinfügen = Label(master = fensterErstellen,
                          text = "Serie der Meisterschaft")
labelJahreinfügen = Label(master = fensterErstellen,
                          text = "Jahr der Meisterschaft")

entryNameeinfügen = Entry(master = fensterErstellen)
entrySerieeinfügen = Entry(master = fensterErstellen)
entryJahreinfügen = Entry(master = fensterErstellen)

#Radiobuttons Strecken ----------

textStrecke = ""
strecken = StringVar()
radioStrecken = Radiobutton(master = fensterErstellen, text = f"{textStrecke}", value = f"{textStrecke}", variable = strecken)

#Radiobuttons Fahrer ----------

textFahrer = ""
fahrer = StringVar()
radioFahrer = Radiobutton(master = fensterErstellen, text = f"{textFahrer}", value = f"{textFahrer}", variable = fahrer)

# Buttons ----------

#fügt alle ausgewählten Strecken/Fahrer ein
buttonhinzufügen = Button(master=fensterErstellen,
                       text="Strecken hinzufügen",
                       command=hinzufügen)

# Rennkalender / Strecken/Fahrer hinzufügen
buttonneuehinzufügen = Button(master=fensterErstellen,
                       text="neue Strecke erstellen",
                       command=neuehinzufügen)

# Fertig - wechselt zu Fahrer bzw. wieder ins Hauptmenü (Switch)
buttonWeiter = Button(master=fensterErstellen,
                       text="Weiter",
                       command=weiter)

# MAIN ----------

ansicht0()

buttonWeiter.pack()

fensterErstellen.mainloop()