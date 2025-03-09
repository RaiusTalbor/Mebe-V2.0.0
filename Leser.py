from tkinter import filedialog
import pickle

# pfad = filedialog.askopenfile()

f = open("Arbeitsdateien/Einstellungen/Einstellungen.dat", mode='rb')

platzhalter=pickle.load(f)

print(platzhalter)