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
    meisterschaft = pfad.replace()

    #Strecken

    #Pfad

fensterImportieren = Tk()
fensterImportieren.title("Importieren")
fensterImportieren.geometry("800x600")

labelTitel = Label(master=fensterImportieren,
                   text="Importieren",
                   font=('', 15))
labelTitel.pack()

# Zeige hier alle Meisterschaften an ?

buttonImportieren = Button(master=fensterImportieren,
                        text="Importieren",
                        command=Importieren)
buttonImportieren.pack()

fensterImportieren.mainloop()