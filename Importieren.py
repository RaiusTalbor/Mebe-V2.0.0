# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Importiert Mebe 1-Dateien in Mebe 2

import pickle
import random
import time
from tkinter import *
from tkinter import filedialog
import Daten    #Lesen, Schreiben von Dateien

def Importieren():
    labelTitelImportieren.config(text="Meisterschaft wird importiert...")

    pfad = filedialog.askopenfilename()
    streaminhalt = Daten.lesen(pfad)

    #testet gültiges Format
    #mit in? Problem: Liegt ja nur in Datenbank
    
    #---------- Alle Dateien in die Verzeichnisse schreiben

    #Pfad kopiert, aber ".dat" wird nicht übernommen
    meisterschaftsname = pfad[:-4]

    #zählt von hinten alle Zeichen durch, bis auf ersten / --> liegt ja im letzten Ordner, Name muss dahinter sein
    #von vorne geht nicht, da Anzahl Ordner unbekannt
    i = len(meisterschaftsname) - 1
    while meisterschaftsname[i] != "/":
        i -= 1

    #i entspricht Stelle des /, deswegen wieder eins zurück, um auf 1. Buchstaben des Namens zu zeigen
    #alles dahinter muss der Name sein
    i += 1
    meisterschaftsname = meisterschaftsname[i:]
    
    #öffnen des vorhandenen Meisterschaftsverzeichnisses
    meisterschaftenMebe2 = Daten.lesen('Datenbank/000 - Verzeichnis Meisterschaften.dat')

    meisterschaftenMebe2.append(meisterschaftsname)

    #speichern des Meisterschaftsverzeichnisses
    Daten.schreiben('Datenbank/000 - Verzeichnis Meisterschaften.dat', meisterschaftenMebe2)

    #----------Strecken
    #öffnet zu importierende Strecken
    streckenliste = Daten.lesen(streaminhalt[0])
    
    #öffnen des vorhandenen Streckenverzeichnisses
    streckenMebe2 = Daten.lesen('Datenbank/Strecken/000 - Verzeichnis Strecken.dat')

    #hinzufügen der neuen Strecken
    for i in range(0, len(streckenliste)):
        if  streckenliste[i] not in streckenMebe2:
            streckenMebe2.append(streckenliste[i])

    #speichern des Streckenverzeichnisses
    Daten.schreiben('Datenbank/Strecken/000 - Verzeichnis Strecken.dat', streckenMebe2)

    #----------Fahrer
    fahrerliste = Daten.lesen(streaminhalt[1])
    
    #öffnen des vorhandenen Fahrerverzeichnisses
    fahrerMebe2 = Daten.lesen('Datenbank/Fahrer/000 - Verzeichnis Fahrer.dat')

    #hinzufügen der neuen Fahrer
    for i in range(0, len(fahrerliste)):
        if  fahrerliste[i] not in fahrerMebe2:
            fahrerMebe2.append(fahrerliste[i])

    #speichern des Fahrerverzeichnisses
    Daten.schreiben('Datenbank/Fahrer/000 - Verzeichnis Fahrer.dat', fahrerMebe2)

    #----------Fahrzeuge
    #durchsuchen jeder Fahrer nach fahrzeug, was evtl. nicht dabei ist

    #hinzufügen der neuen Fahrzeuge, nur die Fahrer, die auch wirklich hinzukommen
    for i in range(0, fahrerliste):

        #baut den Pfad des jeweiligen Fahrers zusammen
        pfadFahrer = "Datenbank/Fahrer/"
        pfadFahrer += fahrerliste[i]
        pfadFahrer += ".dat"

        fahrerdaten = Daten.lesen(pfadFahrer)

        #nur Fahrzeug herausgesucht
        neuesFahrzeug = fahrerdaten[7]

        #öffnen des vorhandenen Fahrzeugverzeichnisses
        fahrzeugMebe2 = Daten.lesen('Datenbank/Fahrzeuge/000 - Verzeichnis Fahrzeuge.dat')

        #hinzufügen des neuen Fahrzeugs
        if  neuesFahrzeug not in fahrzeugMebe2:
            fahrzeugMebe2.append(neuesFahrzeug)

    #speichern des Fahrerverzeichnisses
    Daten.schreiben('Datenbank/Fahrzeuge/000 - Verzeichnis Fahrzeuge.dat', fahrzeugMebe2)

    #Hier mögliche Kontrollausgabe hinzufügen TODO

    labelTitelImportieren.config(text="Importieren aus Mebe V1.x")

#----------View

fensterImportieren = Toplevel()
fensterImportieren.title("Importieren")
fensterImportieren.geometry("800x600")

labelTitelImportieren = Label(master=fensterImportieren,
                   text="Importieren aus Mebe V1.x",
                   font=('', 15))
labelTitelImportieren.pack()

# Zeige hier alle Meisterschaften an ?

buttonImportieren = Button(master=fensterImportieren,
                        text="Importieren",
                        command=Importieren)
buttonImportieren.pack()

fensterImportieren.mainloop()