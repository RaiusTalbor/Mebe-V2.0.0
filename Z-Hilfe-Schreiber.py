import pickle
from tkinter import *
import Daten

pfad = "Arbeitsdateien/Einstellungen/Einstellungen.dat"

liste = ['', '']

f = open(pfad, mode = 'wb')
pickle.dump(liste, f)
f.close()