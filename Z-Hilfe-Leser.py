from tkinter import filedialog
import pickle

# pfad = filedialog.askopenfile()

#f = open("temporäre Dateien/000 - Zwischendaten.dat", mode='rb')
f = open("Datenbank/BTMTest2020Fahrer.dat", mode='rb')

platzhalter=pickle.load(f)

print(platzhalter)