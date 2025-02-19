import pickle

pfad=input("Gib einen Pfad an!")

pfad += ".dat"

f=open(pfad, 'rb')
platzhalter=pickle.load(f)
f.close()

print(platzhalter)