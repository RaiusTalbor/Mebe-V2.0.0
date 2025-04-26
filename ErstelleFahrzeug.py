# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Menü zur Erstellung eines Fahrzeugs

import time
from tkinter import *
import Daten    #Lesen, Schreiben von Dateien

#Erstellen der Datei
def FahrzeugFertig():
    global fensterErstellenFahrzeug
    global labelInfo
    global entryName
    global Leistung
    global Wendigkeit
    global Fahrzeugname

    fahrzeugdaten = []

    fahrzeugdaten.append(int(Leistung.get()))
    fahrzeugdaten.append(int(Wendigkeit.get()))

    Fahrzeugname = entryName.get() #Hier wird die Variable gesetzt, sodass andere Module dann auch darauf zugreifen können --> kein return

    pfad = "Datenbank/Fahrzeuge/" + Fahrzeugname + ".dat"
    
    Daten.schreiben(pfad, fahrzeugdaten)

    #TODO Fehler abfangen

    #gibt Info, dass Fahrzeug erstellt wurde
    labelInfo.config(text = "Fahrzeug wird erstellt...")
    labelInfo.update_idletasks()

    time.sleep(0.5)

    #zerstören
    fensterErstellenFahrzeug.destroy()

def FahrzeugErstellen():
    global fensterErstellenFahrzeug
    global labelInfo
    global entryName
    global Leistung
    global Wendigkeit

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

    Leistung = StringVar()
    wenig = Radiobutton(master = fensterErstellenFahrzeug, text = "Wenig", value = 1, variable = Leistung)
    mittel = Radiobutton(master = fensterErstellenFahrzeug, text = "Ausgeglichen", value = 2, variable = Leistung)
    viel = Radiobutton(master = fensterErstellenFahrzeug, text = "Viel", value = 3, variable = Leistung)
    wenig.pack()
    mittel.pack()
    viel.pack()
    wenig.select()

    labelWendigkeit = Label(fensterErstellenFahrzeug, text="Wie wenidg das Fahrzeug im Vergleich zu den anderen der Meisterschaft?")
    labelWendigkeit.pack()

    #Gegenteil von Wendig?
    Wendigkeit = StringVar()
    schnell = Radiobutton(master = fensterErstellenFahrzeug, text = "Schnell", value = 1, variable = Wendigkeit)
    ausgeglichen = Radiobutton(master = fensterErstellenFahrzeug, text = "Ausgeglichen", value = 2, variable = Wendigkeit)
    wendig = Radiobutton(master = fensterErstellenFahrzeug, text = "Wendig", value = 3, variable = Wendigkeit)
    schnell.pack()
    ausgeglichen.pack()
    wendig.pack()
    schnell.select()

    buttonerstellen = Button(master = fensterErstellenFahrzeug, text = "Fahrzeug erstellen", command = FahrzeugFertig)
    buttonerstellen.pack()

    labelInfo = Label(fensterErstellenFahrzeug, text="")
    labelInfo.pack()