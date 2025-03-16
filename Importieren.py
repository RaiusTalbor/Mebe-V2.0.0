# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Importiert Mebe 1-Dateien in Mebe 2

import pickle
import random
import time
from tkinter import *
from tkinter import filedialog
import MebeV1 as M1 #Mebe1-Integrierung
import Daten    #Lesen, Schreiben von Dateien

def abbruch():
    #Abbruch des Importierens
    a = a

def Importieren():
    pfad = filedialog.askopenfilename()
    f = open(pfad, mode = 'rb')
    streaminhalt = pickle.load(f)
    f.close()

    #testet gültiges Format
    #mit in? Problem: Liegt ja nur in Datenbank
    
    # Alle Dateien in die Verzeichnisse schreiben

    #Meisterschaft selbst
    #meisterschaft = pfad.replace()

    #----------Strecken
    #öffnet zu importierende Strecken
    f = open(streaminhalt[0], mode='wb')
    streckenliste = pickle.load(f)
    f.close()
    
    #öffnen des vorhandenen Streckenverzeichnisses
    f = open('Datenbank/Strecken/000 - Verzeichnis Strecken.dat', mode='rb')
    streckenMebe2 = pickle.load(f)
    f.close()

    #hinzufügen der neuen Strecken
    for i in range(0, len(streckenliste)):
        if  streckenliste[i] not in streckenMebe2:
            streckenMebe2.append(streckenliste[i])

    #speichern des Streckenverzeichnisses
    f = open('Datenbank/Strecken/000 - Verzeichnis Strecken.dat', mode='wb')
    pickle.dump(streckenMebe2, f)
    f.close()

    #----------Fahrer

    #Fahrzeuge
    #durchsuchen jeder Fahrer nach fahrzeug, was evtl. nicht dabei ist

    #Pfad

fensterImportieren = Tk()
fensterImportieren.title("Importieren")
fensterImportieren.geometry("800x600")

labelTitel = Label(master=fensterImportieren,
                   text="Importieren aus Mebe V1.x",
                   font=('', 15))
labelTitel.pack()

# Zeige hier alle Meisterschaften an ?

buttonImportieren = Button(master=fensterImportieren,
                        text="Importieren",
                        command=Importieren)
buttonImportieren.pack()

fensterImportieren.mainloop()