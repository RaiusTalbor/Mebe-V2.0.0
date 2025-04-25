# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Untermenü erstellen - ermöglicht das Erstellen einer komplett neuen Meisterschaft

import time
from tkinter import *
import Daten        #Lesen, Schreiben von Dateien
import ErstelleStrecke
import ErstelleFahrer
import os

def warte():
    x=2

#fügt Radiobutton-Auswahl hinzu
def hinzufügen():

    global varweiter
    global Fahrer       #Radiobuttons
    global strecken     #Radiobuttons
    global rennkalender
    global fahrerliste

    #holt sich die Daten und speichert sie zwischen
    if varweiter == 1:
        rennkalender.append(strecken.get())
    
    if varweiter == 2:
        fahrerliste.append(Fahrer.get())

#fügt entweder neuen Fahrer oder neue Strecke ein
def neuehinzufügen():
    global varweiter
    global rennkalender
    global fahrerliste

    if varweiter == 1:
        #füge nun die Auswahl hinzu
        ErstelleStrecke.StreckeErstellen()

        rennkalender.append(Daten.nehmen())

    if varweiter == 2:
        #füge nun die Auswahl hinzu
        ErstelleFahrer.FahrerErstellen()

        fahrerliste.append(Daten.nehmen())

#zeigt jeweils das neue Fenster mit den neuen Einstellungen an
def weiter():
    global varweiter
    global textStrecke
    global textFahrer
    global meisterschaftspfad
    global strecken
    global Fahrer
    global radio

    global entryNameeinfügen, labelNameeinfügen, labelJahreinfügen, entryJahreinfügen, labelTitelErstellen, fensterErstellen
    global buttonhinzufügen, buttonneuehinzufügen, rennkalender, fahrerliste, fahrerliste
        
    varweiter += 1

    #Fenster 2 - Strecken hinzufügen
    if varweiter == 1:

        #Meisterschaftsdatei anlegen
        meisterschaftspfad = entryNameeinfügen.get()
        #wird in fertig aufgegriffen

        #zerstören der vorigen Elemente
        labelNameeinfügen.destroy()
        labelJahreinfügen.destroy()
        #labelSerieeinfügen.destroy()
        entryJahreinfügen.destroy()
        entryNameeinfügen.destroy()
        #entrySerieeinfügen.destroy()

        labelTitelErstellen.config(text = "Erstellen einer Meisterschaft - Strecken hinzufügen")
        #Hinweis: In Reihenfolge des Rennkalenders

        #listeStrecken = Daten.lesen('Datenbank/Strecken/000 - Verzeichnis Strecken.dat')
        listeStrecken = os.listdir('Datenbank/Strecken')

        strecken = StringVar()

        #für jedes Element der Liste (also alle Strecken) wird ein Radiobutton erzeugt
        for i in range(0, len(listeStrecken)):
            #formated String in Radiobutton wird gesetzt
            textStrecke = listeStrecken[i]
            textStrecke = textStrecke.replace('.dat', '')

            radioStrecken = Radiobutton(master = fensterErstellen, text = f"{textStrecke}", value = listeStrecken[i], variable = strecken)
            radioStrecken.pack()

            radio.append(radioStrecken) #zum löschen
        strecken.set(textStrecke) #letzte wird standardmäßig ausgewählt

        #Aktionsknöpfe
        buttonhinzufügen.pack()
        buttonneuehinzufügen.pack()

    #Fenster 3 - Fahrer hinzufügen
    elif varweiter == 2:

        #zerstören der vorigen Instanzen
        for radioStrecken in radio:
            radioStrecken.destroy()
        radio.clear()

        labelTitelErstellen.config(text = "Erstellen einer Meisterschaft - Fahrer hinzufügen")

        #listeFahrer = Daten.lesen('Datenbank/Fahrer/000 - Verzeichnis Fahrer.dat')
        listeFahrer = os.listdir('Datenbank/Fahrer')

        Fahrer = StringVar()

        #für jedes Element der Liste (also alle Fahrer) wird ein Radiobutton erzeugt
        for i in range(0, len(listeFahrer)):

            #formated String in Radiobutton wird gesetzt
            textFahrer = listeFahrer[i]
            textFahrer = textFahrer.replace('.dat', '')

            radioFahrer = Radiobutton(master = fensterErstellen, text = f"{textFahrer}", 
                                  value = str(textFahrer), variable = Fahrer)
            radioFahrer.pack()

            radio.append(radioFahrer) #zum löschen
        Fahrer.set(textFahrer)

        #Aktionsknöpfe bekommen neue Text
        buttonhinzufügen.config(text = "Fahrer hinzufügen")
        buttonneuehinzufügen.config(text = "neue Fahrer erstellen")

    #Fenster 4 - Fertigstellen und Exit
    elif varweiter == 3:

        #zerstören der vorigen Instanzen
        for radioFahrer in radio:
            radioFahrer.destroy()
        radio.clear()

        #alle Daten sammeln und speichern

        #pfade erstellen
        meisterschaftsname = meisterschaftspfad
        meisterschaftspfad = 'Datenbank/' + str(meisterschaftsname) + '.dat'
        streckenpfad = 'Datenbank/' + str(meisterschaftsname) + 'Strecken' + '.dat'
        fahrerpfad = 'Datenbank/' + str(meisterschaftsname) + 'Fahrer' + '.dat'

        rennkalenderS = []
        #Strecken als Pfad: jedes Element als Pfad speichern
        for strecke in rennkalender:
            strecke = 'Datenbank/Strecken/' + strecke + '.dat'
            rennkalenderS.append(strecke)

        #Strecken werden gespeichert
        Daten.schreiben(streckenpfad, rennkalender)
        #fahrer als pfad

        fahrerlisteS = []
        #Fahrer als Pfad: jedes Element als Pfad speichern
        for pilot in fahrerliste:
            pilot = 'Datenbank/Fahrer/' + str(pilot) + '.dat'
            fahrerlisteS.append(pilot)

        #Fahrer werden gespeichert
        Daten.schreiben(fahrerpfad, fahrerliste)

        #Meisterschaft wird gespeichert
        Daten.schreiben(meisterschaftspfad, [streckenpfad, fahrerpfad])

        #Fertig
        fensterErstellenFertig = Toplevel()
        fensterErstellenFertig.title("Fertig - Mebe V2.0.0")
        fensterErstellenFertig.geometry("200x300")

        labelTitelErstellenFertig = Label(master=fensterErstellenFertig,
                           text="Erstellt!",
                           font=('', 15))
        labelTitelErstellenFertig.pack()

        time.sleep(2)

        varweiter = 0

        fensterErstellenFertig.destroy()

        fensterErstellen.destroy()

def erstellen():
    global entryNameeinfügen, labelNameeinfügen, labelJahreinfügen, entryJahreinfügen, labelTitelErstellen, fensterErstellen
    global buttonhinzufügen, buttonneuehinzufügen, varweiter, meisterschaftspfad, rennkalender, fahrerliste, fahrerliste, radio

    #weiter 0...Pflichtdaten; weiter 1...Strecken; weiter 2...Fahrer
    varweiter = 0

    meisterschaftspfad = ""
    rennkalender = []
    fahrerliste = []

    #alle Radiobuttons, damit sie hinterher auch gelöscht werden können
    radio = []

    #Fenster
    fensterErstellen = Toplevel()
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
    #labelSerieeinfügen = Label(master = fensterErstellen,
    #                          text = "Serie der Meisterschaft")
    labelJahreinfügen = Label(master = fensterErstellen,
                            text = "Jahr der Meisterschaft")

    entryNameeinfügen = Entry(master = fensterErstellen)
    #entrySerieeinfügen = Entry(master = fensterErstellen)
    entryJahreinfügen = Entry(master = fensterErstellen)

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

    labelNameeinfügen.pack()
    entryNameeinfügen.pack()

    #labelSerieeinfügen.pack()
    #entrySerieeinfügen.pack()

    labelJahreinfügen.pack()
    entryJahreinfügen.pack()

    buttonWeiter.pack()