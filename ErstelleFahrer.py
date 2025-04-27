# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Menü zur Erstellung eines Fahrers

import time
from tkinter import *
import Daten    #Lesen, Schreiben von Dateien
import os
import ErstelleFahrzeug

#Erstellen der Datei
def FahrerFertig():
    global fensterErstellenFahrer
    global labelInfo
    global entryName
    global entryGebJahr
    global entry1Rennen
    global scaleAggressivität
    global scaleGeschicklichkeit
    global scaleGrundkönnen
    global vorliebe
    global entryDurchschnittPlatzierung
    global entryFahrzeug
    global entryFahrzeugwann
    global Fahrername

    fahrerdaten = []

    fahrerdaten.append(entryGebJahr.get())
    fahrerdaten.append(entry1Rennen.get())
    fahrerdaten.append(scaleAggressivität.get())
    fahrerdaten.append(scaleGeschicklichkeit.get())
    fahrerdaten.append(scaleGrundkönnen.get())
    fahrerdaten.append(vorliebe.get())
    fahrerdaten.append(entryDurchschnittPlatzierung.get())
    fahrerdaten.append(entryFahrzeug) #.get() , wenn es wieder ein entry ist
    fahrerdaten.append(entryFahrzeugwann.get())
    fahrerdaten.append(Fahrername)

    Fahrername = entryName.get() #Hier wird die Variable gesetzt, sodass andere Module dann auch darauf zugreifen können --> kein return

    pfad = "Datenbank/Fahrer/" + Fahrername + ".dat"
    
    Daten.schreiben(pfad, fahrerdaten)

    #TODO Fehler abfangen

    #gibt Info, dass Fahrer erstellt wurde
    labelInfo.config(text = "Fahrer wird erstellt...")
    labelInfo.update_idletasks()

    time.sleep(0.5)

    #zerstören
    fensterErstellenFahrer.destroy()

#Button; fügt richtiges Fahrzeug in Auswahl ein
def fügeFahrzeugein():
    global Fahrzeug
    global entryFahrzeug
    global fensterErstellenFahrerFahrzeugauswählen

    #ausgewählterFahrer = Fahrzeug.get()
    entryFahrzeug = Fahrzeug.get()

    #vielleicht vorher leeren
    #entryFahrzeug.insert(0, ausgewählterFahrer)
    text = str(entryFahrzeug) #vorher mit [], geht ja aber nicht, da Programm etwas da rausholen
    labelFahrzeugAuswahl.config(text=text)

    fensterErstellenFahrerFahrzeugauswählen.destroy()

#ein neues Fahrzeug wird erstellt
def neuesFahrzeug():
    global entryFahrzeug
    global fensterErstellenFahrerFahrzeugauswählen
    global labelFahrzeugAuswahl

    #entryFahrzeug.insert(0, ErstelleFahrzeug.erstellen())
    ErstelleFahrzeug.FahrzeugErstellen()

    fensterErstellenFahrer.wait_window(ErstelleFahrzeug.fensterErstellenFahrzeug)
    
    entryFahrzeug = ErstelleFahrzeug.Fahrzeugname

    text = str(entryFahrzeug) #vorher mit [], geht ja aber nicht, da Programm etwas da rausholen
    labelFahrzeugAuswahl.config(text=text)
    labelFahrzeugAuswahl.update_idletasks()

    #Es gibt zwei Möglichkeiten, hier her zu kommen. Einmal aus ErstelleFahrer und einmal aus der Fahrzeugauswahl.
    #Bei der Fahrzeugauswahl muss das Fenster geschlossen werden, sonst nicht.
    try:
        fensterErstellenFahrerFahrzeugauswählen.destroy()
    except:
        pass

#öffnet Fenster, mit dem das Fahrzeug ausgewählt werden kann; aus ErstelleFahrer
def Fahrzeugauswählen():
    global Fahrzeug
    global fensterErstellenFahrerFahrzeugauswählen

    fensterErstellenFahrerFahrzeugauswählen = Toplevel()
    fensterErstellenFahrerFahrzeugauswählen.title("Fahrzeug auswählen - Mebe V2.0.0")
    fensterErstellenFahrerFahrzeugauswählen.geometry("800x600")

    labelTitelErstellenStrecke = Label(master=fensterErstellenFahrerFahrzeugauswählen,
                                        text="Wähle Fahrzeug aus",
                                        font=('', 15))
    labelTitelErstellenStrecke.pack()

    buttonneu = Button(master = fensterErstellenFahrerFahrzeugauswählen, text = "Neues Fahrzeug erstellen", command = neuesFahrzeug)
    buttonneu.pack()

    buttonauswählen = Button(master = fensterErstellenFahrerFahrzeugauswählen, text = "Fahrzeug auswählen", command = fügeFahrzeugein)
    buttonauswählen.pack()

    Fahrzeug = StringVar()

    listeFahrzeuge = os.listdir('Datenbank/Fahrzeuge')

    #für jedes Element der Liste (also alle Fahrer) wird ein Radiobutton erzeugt
    for i in range(0, len(listeFahrzeuge)):

        #formated String in Radiobutton wird gesetzt
        textFahrzeug = listeFahrzeuge[i]
        textFahrzeug = textFahrzeug.replace('.dat', '')

        radioFahrer = Radiobutton(master = fensterErstellenFahrerFahrzeugauswählen, text = f"{textFahrzeug}", 
                                  value = str(textFahrzeug), variable = Fahrzeug)
        radioFahrer.pack()

    Fahrzeug.set(textFahrzeug)

def FahrerErstellen():
    global fensterErstellenFahrer
    global labelInfo
    global entryName
    global entryGebJahr
    global entry1Rennen
    global scaleAggressivität
    global scaleGeschicklichkeit
    global scaleGrundkönnen
    global vorliebe
    global entryDurchschnittPlatzierung
    global entryFahrzeug
    global labelFahrzeugAuswahl
    global entryFahrzeugwann

    fensterErstellenFahrer = Toplevel()
    fensterErstellenFahrer.title("Erstelle Fahrer - Mebe V2.0.0")
    fensterErstellenFahrer.geometry("800x600")

    labelTitelErstellenFahrer = Label(master=fensterErstellenFahrer,
                                        text="Erstelle Fahrer",
                                        font=('', 15))
    labelTitelErstellenFahrer.pack()

    labelName = Label(master = fensterErstellenFahrer, text="Name des Fahrers:")
    labelName.pack()

    entryName = Entry(master = fensterErstellenFahrer)
    entryName.pack()

    #GebJahr
    labelGebJahr = Label(fensterErstellenFahrer, text="Geburtsjahr des Fahrers:").pack()
    entryGebJahr = Entry(master = fensterErstellenFahrer)
    entryGebJahr.pack()

    #1. Rennen
    label1Rennen = Label(fensterErstellenFahrer, text="Wann fuhr der Fahrer/die Fahrerin sein/ihr erstes Rennen").pack()
    entry1Rennen = Entry(master = fensterErstellenFahrer)
    entry1Rennen.pack()

    #Aggressivität
    labelAggressivität = Label(fensterErstellenFahrer, text="Wie aggressiviv fährt der Fahrer?").pack()
    scaleAggressivität = Scale(master = fensterErstellenFahrer, from_= 1, to = 10, orient=HORIZONTAL)
    scaleAggressivität.pack()

    #Geschicklichkeit
    labelGeschicklichkeit = Label(fensterErstellenFahrer, text="Wie geschickt fährt der Fahrer?").pack()
    scaleGeschicklichkeit = Scale(master = fensterErstellenFahrer, from_= 1, to = 10, orient=HORIZONTAL)
    scaleGeschicklichkeit.pack()

    #Grundkönnen
    labelGrundkönnen = Label(fensterErstellenFahrer, text="Wie hoch ist sein Grundkönnen?").pack()
    scaleGrundkönnen = Scale(master = fensterErstellenFahrer, from_= 1, to = 100, orient=HORIZONTAL)
    scaleGrundkönnen.pack()
    #noch eine vereinfachte Variante?

    #Vorliebe
    labelvorliebe = Label(fensterErstellenFahrer, text="Vorliebe für schnelle Strecken?").pack()

    vorliebe = StringVar()
    kurvig = Radiobutton(master = fensterErstellenFahrer, text = "Kurvige Strecke", value = 1, variable = vorliebe)
    schnell = Radiobutton(master = fensterErstellenFahrer, text = "Schnelle Strecke", value = 2, variable = vorliebe)
    kurvig.pack()
    schnell.pack()
    kurvig.select()

    #Durchschnittl. Platzierung
    labelDurchschnittPlatzierung = Label(fensterErstellenFahrer, text="Welche durchschnittliche Platzierung?").pack()
    entryDurchschnittPlatzierung = Entry(master = fensterErstellenFahrer)
    entryDurchschnittPlatzierung.pack()

    #Fahrzeug
    labelFahrzeug = Label(fensterErstellenFahrer, text="Welches Fahrzeug wird gefahren?").pack()
    #entryFahrzeug = Entry(master = fensterErstellenFahrer)
    #entryFahrzeug.pack()
    entryFahrzeug = ""

    labelFahrzeugAuswahl = Label(master = fensterErstellenFahrer, text="[Kein Fahrzeug ausgewählt]")
    labelFahrzeugAuswahl.pack()

    buttonneu = Button(master = fensterErstellenFahrer, text = "Neues Fahrzeug erstellen", command = neuesFahrzeug)
    buttonneu.pack()

    buttonFahrzeugAuswählen = Button(master = fensterErstellenFahrer, text = "Fahrzeug aus Datenbank auswählen...", command = Fahrzeugauswählen)
    buttonFahrzeugAuswählen.pack()

    #seit wann Fahrzeug
    labelFahrzeugwann = Label(master = fensterErstellenFahrer, text="Seit wann wird das Fahrzeug gefahren?").pack()
    entryFahrzeugwann = Entry(master = fensterErstellenFahrer)
    entryFahrzeugwann.pack()

    buttonerstellen = Button(master = fensterErstellenFahrer, text = "Fahrer erstellen", command = FahrerFertig)
    buttonerstellen.pack()

    labelInfo = Label(fensterErstellenFahrer, text="", font=('', 15))
    labelInfo.pack()