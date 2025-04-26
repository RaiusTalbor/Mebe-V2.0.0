# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Lesen, Schreiben von Dateien

import pickle

# Daten werden gelesen
def lesen(pfad):
    f = open(pfad, mode = 'rb')
    daten = pickle.load(f)
    f.close()
    return daten

# Daten werden geschrieben
def schreiben(pfad, daten):
    f = open(pfad, mode = 'wb')
    pickle.dump(daten, f)
    f.close()