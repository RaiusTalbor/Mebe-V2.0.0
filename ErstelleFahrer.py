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

    #Beim Bearbeiten existiert entryName nicht
    try:
        Fahrername = entryName.get() #Hier wird die Variable gesetzt, sodass andere Module dann auch darauf zugreifen können --> kein return
    except:
        pass

    pfad = "Datenbank/Fahrer/" + Fahrername + ".dat"
    
    Daten.schreiben(pfad, fahrerdaten)

    #TODO Fehler abfangen

    #gibt Info, dass Fahrer erstellt wurde
    labelInfo.config(text = "Fahrer wird gespeichert...")
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
    global labelTitelErstellenFahrer
    global fensterErstellenFahrer
    global labelInfo
    global labelName
    global entryName
    global entryGebJahr
    global entry1Rennen
    global scaleAggressivität
    global scaleGeschicklichkeit
    global scaleGrundkönnen
    global vorliebe
    global kurvig, schnell
    global entryDurchschnittPlatzierung
    global entryFahrzeug
    global labelFahrzeugAuswahl
    global entryFahrzeugwann
    global buttonerstellen

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

def bearbeitenStarten():
    global labelTitelErstellenFahrer
    global fensterErstellenFahrerBearbeitenAuswahl
    global labelName
    global entryName
    global entryGebJahr
    global entry1Rennen
    global scaleAggressivität
    global scaleGeschicklichkeit
    global scaleGrundkönnen
    global vorliebe
    global kurvig, schnell
    global entryDurchschnittPlatzierung
    global entryFahrzeug
    global labelFahrzeugAuswahl
    global entryFahrzeugwann
    global buttonerstellen

    global Fahrername #! für andere Module extrem wichtig, speichert Namen der aktuellen Strecke

    Fahrername = fahrer.get() #speichert Auswahl

    fensterErstellenFahrerBearbeitenAuswahl.destroy() #löscht das Fenster

    #verarbeitet die Auswahl
    fahrerpfad = "Datenbank/Fahrer/" + Fahrername + ".dat"

    fahrerdaten = Daten.lesen(fahrerpfad)

    FahrerErstellen() #Widgets werden erstellt

    #Widgets werden angepasst

    labelTitelErstellenFahrer.config(text="Bearbeite Fahrer")
    labelTitelErstellenFahrer.update_idletasks()

    fensterErstellenFahrer.title("Bearbeite Fahrer - Mebe V2.0.0")
    fensterErstellenFahrer.update_idletasks()

    labelName.destroy()
    entryName.destroy() #Name soll nicht änderbar sein

    entryGebJahr.delete(0, END)
    entryGebJahr.insert(0, fahrerdaten[0])
    entryGebJahr.update_idletasks()

    entry1Rennen.delete(0, END)
    entry1Rennen.insert(0, fahrerdaten[1])
    entry1Rennen.update_idletasks()

    scaleAggressivität.set(fahrerdaten[2])
    scaleAggressivität.update_idletasks()

    scaleGeschicklichkeit.set(fahrerdaten[3])
    scaleGeschicklichkeit.update_idletasks()

    scaleGrundkönnen.set(fahrerdaten[4])
    scaleGrundkönnen.update_idletasks()

    if fahrerdaten[5] == 1:
        kurvig.select()
    else:
        schnell.select()
    
    kurvig.update_idletasks()
    schnell.update_idletasks()

    entryDurchschnittPlatzierung.delete(0, END)
    entryDurchschnittPlatzierung.insert(0, fahrerdaten[6])
    entryDurchschnittPlatzierung.update_idletasks()

    entryFahrzeug = fahrerdaten[7]
    labelFahrzeugAuswahl.config(text = entryFahrzeug)
    labelFahrzeugAuswahl.update_idletasks()

    entryFahrzeugwann.delete(0, END)
    entryFahrzeugwann.insert(0, fahrerdaten[8])
    entryFahrzeugwann.update_idletasks()

    buttonerstellen.config(text = "Speichern")
    buttonerstellen.update_idletasks()

def bearbeiten():
    global fensterErstellenFahrerBearbeitenAuswahl
    global fahrer

    #Auswahl der Strecke
    fensterErstellenFahrerBearbeitenAuswahl = Toplevel()
    fensterErstellenFahrerBearbeitenAuswahl.title("Bearbeite Fahrer - Mebe V2.0.0")
    fensterErstellenFahrerBearbeitenAuswahl.geometry("800x600")

    labelTitelErstellenFahrer = Label(master=fensterErstellenFahrerBearbeitenAuswahl,
                                        text="Bearbeite Strecke",
                                        font=('', 15))
    labelTitelErstellenFahrer.pack()

    buttonStreckenauswahl = Button(fensterErstellenFahrerBearbeitenAuswahl, text = "Fahrer bearbeiten", command = bearbeitenStarten)
    buttonStreckenauswahl.pack()

    fahrer = StringVar()

    listeFahrer = os.listdir('Datenbank/Fahrer')

    #für jedes Element der Liste (also alle Strecken) wird ein Radiobutton erzeugt
    for i in range(0, len(listeFahrer)):

        #formated String in Radiobutton wird gesetzt
        textFahrzeug = listeFahrer[i]
        textFahrzeug = textFahrzeug.replace('.dat', '')

        radioFahrer = Radiobutton(master = fensterErstellenFahrerBearbeitenAuswahl, text = f"{textFahrzeug}", 
                                  value = str(textFahrzeug), variable = fahrer)
        radioFahrer.pack()

    fahrer.set(textFahrzeug)