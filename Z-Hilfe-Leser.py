from tkinter import filedialog
import pickle

# pfad = filedialog.askopenfile()

f = open("Datenbank/Fahrer/B.dat", mode='rb')

platzhalter=pickle.load(f)

print(platzhalter)