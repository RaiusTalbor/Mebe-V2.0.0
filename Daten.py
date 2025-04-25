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

#gibt einen Wert an ein anderes Modul zurück
def übergabe(daten):
    schreiben("temporäre Dateien/000 - Zwischendaten.dat", daten)


#nimmt Daten aus Zwischenspeicher und gibt sie zurück
def nehmeDaten():
    f = open("temporäre Dateien/000 - Zwischendaten.dat", mode = 'rb')
    rückgabe = pickle.load(f)
    f.close()

    return rückgabe

#nimmt sich die zwischengespeicherten Daten
#Toplevel geht aber direkt weiter, deswegen wartet er, bis die Daten aus dem Unterprogramm da sind
def nehmen(wartendesfenster):
    übergabe("")

    #prüft, ob die Daten da sind; wenn ja, aus Schleife raus und returnt es, während das Fenster aber wartet
    def check():
        if(nehmeDaten() == ""):
                wartendesfenster.after(1000, check)
        else:
            rückgabe = nehmeDaten()

            return rückgabe

    daten = check()
    return daten

#Idee
#Hier Callback-Fkt. einfügen
#eine Funktion wird übergeben, die dann wieder im Aufruf-Modull aufgerufen werden soll
#Diese Callback-Fkt. speichert dann den Wert in die globale Variable, wo das Programm sie dann hin haben will