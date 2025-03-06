from tkinter import filedialog
import pickle

f = filedialog.askopenfile()

platzhalter=pickle.load(f)

print(platzhalter)