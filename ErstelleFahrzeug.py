# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Menü zur Erstellung eines Fahrzeugs

import time
import os
from tkinter import *
import Daten    #Lesen, Schreiben von Dateien

#Erstellen der Datei
def FahrzeugFertig():
    global fensterErstellenFahrzeug
    global labelInfo
    global entryName
    global leistung
    global wendigkeit
    global Fahrzeugname

    fahrzeugdaten = []

    fahrzeugdaten.append(int(leistung.get()))
    fahrzeugdaten.append(int(wendigkeit.get()))

    #Beim Bearbeiten existiert entryName nicht
    try:
        #Hier wird die Variable gesetzt, sodass andere Module dann auch darauf zugreifen können --> kein return
        Fahrzeugname = entryName.get()
    except:
        pass

    pfad = "Datenbank/Fahrzeuge/" + Fahrzeugname + ".dat"
    
    Daten.schreiben(pfad, fahrzeugdaten)

    #TODO Fehler abfangen

    #gibt Info, dass Fahrzeug erstellt wurde
    labelInfo.config(text = "Fahrzeug wird gespeichert...")
    labelInfo.update_idletasks()

    time.sleep(0.5)

    #zerstören
    fensterErstellenFahrzeug.destroy()

def FahrzeugErstellen():
    global labelTitelErstellenFahrzeug
    global fensterErstellenFahrzeug
    global labelInfo
    global labelName
    global entryName
    global leistung
    global wendigkeit
    global buttonerstellen

    #Radios
    global schnell, ausgeglichen, wendig
    global wenig, mittel, viel

    fensterErstellenFahrzeug = Toplevel()
    fensterErstellenFahrzeug.title("Erstelle Fahrzeug - Mebe V2.0.0")
    fensterErstellenFahrzeug.geometry("800x600")

    labelTitelErstellenFahrzeug = Label(master=fensterErstellenFahrzeug,
                                        text="Erstelle Fahrzeug",
                                        font=('', 15))
    labelTitelErstellenFahrzeug.pack()

    labelName = Label(master = fensterErstellenFahrzeug, text="Name des Fahrzeugs:")
    labelName.pack()

    entryName = Entry(master = fensterErstellenFahrzeug)
    entryName.pack()

    labelLeistung = Label(fensterErstellenFahrzeug, text="Wie viel Leistung hat das Fahrzeug im Vergleich zu den anderen der Meisterschaft?")
    labelLeistung.pack()

    leistung = StringVar()
    wenig = Radiobutton(master = fensterErstellenFahrzeug, text = "Wenig", value = 1, variable = leistung)
    mittel = Radiobutton(master = fensterErstellenFahrzeug, text = "Ausgeglichen", value = 2, variable = leistung)
    viel = Radiobutton(master = fensterErstellenFahrzeug, text = "Viel", value = 3, variable = leistung)
    wenig.pack()
    mittel.pack()
    viel.pack()
    wenig.select()

    labelWendigkeit = Label(fensterErstellenFahrzeug, text="Wie wenidg das Fahrzeug im Vergleich zu den anderen der Meisterschaft?")
    labelWendigkeit.pack()

    #Gegenteil von Wendig?
    wendigkeit = StringVar()
    schnell = Radiobutton(master = fensterErstellenFahrzeug, text = "Schnell", value = 1, variable = wendigkeit)
    ausgeglichen = Radiobutton(master = fensterErstellenFahrzeug, text = "Ausgeglichen", value = 2, variable = wendigkeit)
    wendig = Radiobutton(master = fensterErstellenFahrzeug, text = "Wendig", value = 3, variable = wendigkeit)
    schnell.pack()
    ausgeglichen.pack()
    wendig.pack()
    schnell.select()

    buttonerstellen = Button(master = fensterErstellenFahrzeug, text = "Fahrzeug erstellen", command = FahrzeugFertig)
    buttonerstellen.pack()

    labelInfo = Label(fensterErstellenFahrzeug, text="", font=('', 15))
    labelInfo.pack()

def bearbeitenStarten():
    global labelTitelErstellenFahrzeug
    global fensterErstellenFahrzeugBearbeitenAuswahl
    global fahrzeug
    global buttonerstellen
    global labelName
    global entryName

    global Fahrzeugname #! für andere Module extrem wichtig, speichert Namen der aktuellen Strecke

    Fahrzeugname = fahrzeug.get() #speichert Auswahl

    fensterErstellenFahrzeugBearbeitenAuswahl.destroy() #löscht das Fenster

    #verarbeitet die Auswahl
    fahrzeugpfad = "Datenbank/Fahrzeuge/" + Fahrzeugname + ".dat"

    fahrzeugdaten = Daten.lesen(fahrzeugpfad)

    FahrzeugErstellen() #Widgets werden erstellt

    #Widgets werden angepasst

    labelTitelErstellenFahrzeug.config(text="Bearbeite Fahrzeug")
    labelTitelErstellenFahrzeug.update_idletasks()

    fensterErstellenFahrzeug.title("Bearbeite Fahrzeug - Mebe V2.0.0")
    fensterErstellenFahrzeug.update_idletasks()

    labelName.destroy()
    entryName.destroy() #Name soll nicht änderbar sein

    if fahrzeugdaten[0] == 1:
        wenig.select()
    elif fahrzeugdaten[0] == 2:
        mittel.select()
    else:
        viel.select()
    
    wenig.update_idletasks()
    mittel.update_idletasks()
    viel.update_idletasks()

    if fahrzeugdaten[1] == 1:
        schnell.select()
    elif fahrzeugdaten[1] == 2:
        ausgeglichen.select()
    else:
        wendig.select()
    
    schnell.update_idletasks()
    ausgeglichen.update_idletasks()
    wendig.update_idletasks()

    buttonerstellen.config(text = "Speichern")
    buttonerstellen.update_idletasks()

def bearbeiten():
    global fensterErstellenFahrzeugBearbeitenAuswahl
    global fahrzeug

    #Auswahl der Strecke
    fensterErstellenFahrzeugBearbeitenAuswahl = Toplevel()
    fensterErstellenFahrzeugBearbeitenAuswahl.title("Bearbeite Fahrzeug - Mebe V2.0.0")
    fensterErstellenFahrzeugBearbeitenAuswahl.geometry("800x600")

    labelTitelErstellenFahrzeug = Label(master=fensterErstellenFahrzeugBearbeitenAuswahl,
                                        text="Bearbeite Fahrzeug",
                                        font=('', 15))
    labelTitelErstellenFahrzeug.pack()

    buttonFahrzeugauswahl = Button(fensterErstellenFahrzeugBearbeitenAuswahl, text = "Fahrzeug bearbeiten", command = bearbeitenStarten)
    buttonFahrzeugauswahl.pack()

    fahrzeug = StringVar()

    listeFahrzeug = os.listdir('Datenbank/Fahrzeuge')

    #für jedes Element der Liste (also alle Strecken) wird ein Radiobutton erzeugt
    for i in range(0, len(listeFahrzeug)):

        #formated String in Radiobutton wird gesetzt
        textFahrzeug = listeFahrzeug[i]
        textFahrzeug = textFahrzeug.replace('.dat', '')

        radioFahrer = Radiobutton(master = fensterErstellenFahrzeugBearbeitenAuswahl, text = f"{textFahrzeug}", 
                                  value = str(textFahrzeug), variable = fahrzeug)
        radioFahrer.pack()

    fahrzeug.set(textFahrzeug)