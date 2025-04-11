# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Menü zur Erstellung eines Fahrers

import pickle
import random
import time
from tkinter import *
import MebeV1 as M1 #Mebe1-Integrierung
import Daten    #Lesen, Schreiben von Dateien

def auswählen():
    pass

def erstellen():
    fensterErstellenFahrer = Toplevel()
    fensterErstellenFahrer.title("Erstelle Fahrer - Mebe V2.0.0")
    fensterErstellenFahrer.geometry("800x600")

    labelTitelErstellenFahrer = Label(master=fensterErstellenFahrer,
                                        text="Erstelle Fahrer",
                                        font=('', 15))
    labelTitelErstellenFahrer.pack()

    labelName = Label(fensterErstellenFahrer, text="Name des Fahrers:")
    labelName.pack()

    entryName = Entry(fensterErstellenFahrer).pack()

    #GebJahr
    labelGebJahr = Label(fensterErstellenFahrer, text="Geburtsjahr des Fahrers:").pack()
    entryGebJahr = Entry(fensterErstellenFahrer).pack()

    #1. Rennen
    label1Rennen = Label(fensterErstellenFahrer, text="Wann fuhr der Fahrer/die Fahrerin sein/ihr erstes Rennen").pack()
    entry1Rennen = Entry(fensterErstellenFahrer).pack()

    #Aggressivität
    labelAggressivität = Label(fensterErstellenFahrer, text="Wie aggressiviv fährt der Fahrer?").pack()
    scaleAggressivität = Scale(master = fensterErstellenFahrer, from_= 1, to = 10, orient=HORIZONTAL).pack()

    #Geschicklichkeit
    labelGeschicklichkeit = Label(fensterErstellenFahrer, text="Wie geschickt fährt der Fahrer?").pack()
    scaleGeschicklichkeit = Scale(master = fensterErstellenFahrer, from_= 1, to = 10, orient=HORIZONTAL).pack()

    #Grundkönnen
    labelGeschicklichkeit = Label(fensterErstellenFahrer, text="Wie hoch ist sein Grundkönnen?").pack()
    scaleGeschicklichkeit = Scale(master = fensterErstellenFahrer, from_= 1, to = 100, orient=HORIZONTAL).pack()
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
    entryDurchschnittPlatzierung = Entry(fensterErstellenFahrer).pack()

    #Fahrzeug
    labelFahrzeug = Label(fensterErstellenFahrer, text="Welches Fahrzeug wird gefahren?").pack()
    entryAuswählen = Entry(master = fensterErstellenFahrer)
    entryAuswählen.pack()

    buttonAuswählen = Button(master = fensterErstellenFahrer, text = "Fahrzeug aus Datenbank auswählen...", command = auswählen)
    buttonAuswählen.pack()

    #seit wann Fahrzeug
    labelFahrzeugwann = Label(fensterErstellenFahrer, text="Seit wann wird das Fahrzeug gefahren?").pack()
    entryFahrzeugwann = Entry(master = fensterErstellenFahrer)
    entryFahrzeugwann.pack()

    fensterErstellenFahrer.mainloop()

erstellen()