# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
#berechnet eine Meisterschaft und gibt das Ergebnis aus

import pickle
import random
import time
from tkinter import *
import os
import MebeV1 as M1 #Mebe1-Integrierung
import Daten    #Lesen, Schreiben von Dateien

def auswahl():
    global meisterschaft
    global fensterBerechnen
    global labelInfo

    meisterschaftAusgewählt = meisterschaft.get()

    #Ausgabe, dass Meisterschaft gerade berechnet wird
    anzeige = "Meisterschaft '" + meisterschaftAusgewählt + "' wird berechnet..."
    labelInfo.config(text = anzeige)
    labelInfo.update_idletasks()

    berechnenStarten(meisterschaftAusgewählt)

def berechnen():
    global meisterschaft
    global fensterBerechnen
    global labelInfo

    fensterBerechnen = Toplevel()
    fensterBerechnen.title("Berechnen - Mebe V2.0.0")
    fensterBerechnen.geometry("800x600")

    #Frames
    frameInfo = Frame(master=fensterBerechnen)
    frameButtons = Frame(master=fensterBerechnen)
    frameInteraktion = Frame(master=fensterBerechnen)
    frameAnzeige = Frame(master = fensterBerechnen)
    frameInfo.pack()
    frameButtons.pack()
    frameInteraktion.pack()
    frameAnzeige.pack()

    labelTitel = Label(master=frameInfo,
                    text="Berechnen einer Meisterschaft",
                    font=('', 15))
    labelTitel.pack()

    #Auswahl der Meisterschaft

    buttonAuswahl = Button(master = frameButtons, text = "Meisterschaft auswählen", command = auswahl)
    buttonAuswahl.pack(side=LEFT, anchor=N, padx= 20, pady = 20)
    buttonZurück = Button(master = frameButtons, text = "Zurück", command = fensterBerechnen.destroy)
    buttonZurück.pack(side=LEFT, anchor=N, padx= 20, pady = 20)

    VerzeichnisMeisterschaftenohnefilter = os.listdir('Datenbank')
    VerzeichnisMeisterschaften = []

    #für alle Dateien, die nicht auf 'Strecken.dat' oder 'Fahrer.dat', aber auf '.dat' enden, wird zur Liste hinzugefügt
    for i in range(0, len(VerzeichnisMeisterschaftenohnefilter)):
        if (not VerzeichnisMeisterschaftenohnefilter[i].endswith('Fahrer.dat') 
            and not VerzeichnisMeisterschaftenohnefilter[i].endswith('Strecken.dat') 
            and VerzeichnisMeisterschaftenohnefilter[i].endswith('.dat')):

            VerzeichnisMeisterschaften.append(VerzeichnisMeisterschaftenohnefilter[i])

    meisterschaft = StringVar()
    #zeige alle Meisterschaften als Button an
    for i in range(0, len(VerzeichnisMeisterschaften)):

        #richtige Anzeige ohne .dat
        anzeige = VerzeichnisMeisterschaften[i]
        anzeige = anzeige.replace('.dat', '')

        radiobuttonMeisterschaft = Radiobutton(master=frameInteraktion, text=f"{anzeige}", 
                                               value=anzeige, variable = meisterschaft)
        radiobuttonMeisterschaft.pack()

    meisterschaft.set(VerzeichnisMeisterschaften[0])

    labelInfo = Label (master = frameAnzeige, text = "", font = ("",13), wraplength = 800)
    labelInfo.pack()

# Sortieren und richtig anordnen------------------------------------------------------------------------
def strecke_berechnen(streckendaten_moment, fahrerdaten):  # , fahrzeugdaten):

    Ergebnisliste = []

    for i in range(0, len(fahrerdaten)):

        pfad = fahrerdaten[i] #aktueller Pfad wird herausgenommen

        fahrerdatenAktuell = Daten.lesen(pfad) #Fahrerdaten werden ausgelesen

        fahrername = fahrerdatenAktuell[9] #Name wird gespeichert

        #Fahrzeug wird herausgesucht
        pfadfahrzeuge = 'Datenbank/Fahrzeuge/' + fahrerdatenAktuell[7] + '.dat'

        #Fahrzeugdaten werden gelesen
        fahrzeug = Daten.lesen(pfadfahrzeuge)

        #Zufallszahlen werden festgelegt
        zufallszahl1 = random.randint(0, 101)
        zufallszahl2 = random.randint(0, 101)

        #Alter wird berechnet
        Alter = time.localtime()
        Alter = Alter.tm_year
        Alter = Alter - fahrerdatenAktuell[0]

        #Fahrerfahrung wird berechnet
        FahrerSeit = time.localtime()
        FahrerSeit = FahrerSeit.tm_year
        FahrerSeit = FahrerSeit - fahrerdatenAktuell[1]

        #Fahrerfahrung mit Fahrzeug wird berechnet
        FährtAutoSeit = time.localtime()
        FährtAutoSeit = FährtAutoSeit.tm_year
        FährtAutoSeit = FährtAutoSeit - fahrerdatenAktuell[8]

        Grunderfahrung = Alter + FahrerSeit

        Grundstärke = Grunderfahrung + fahrerdatenAktuell[4] + FährtAutoSeit * 2

        #Ist es der Rekordhalter?
        if streckendaten_moment[0] in pfad:
            Streckenbonus = 5
        else:
            Streckenbonus = 0

        #welche Vorliebe hat er?
        # Hat der Fahrer eine Vorliebe für schnelle Strecken, so wird geprüft, ob die Strecke schnell ist.
        # Hat der Fahrer sie nicht, wird geprüft, ob die Strecke kurvig ist. Passen hier auch die Werte zusammen, gibt es die Punkte
        if fahrerdatenAktuell[5] == 2:
            if streckendaten_moment[1] == 3:
                Vorliebe = 5
            else:
                Vorliebe = 0
        else:
            if streckendaten_moment[1] == 1:
                Vorliebe = 5
            else:
                Vorliebe = 0

        #Fahrzeug wird geprüft
        # Eine schnelle Strecke verlangt ein leistungsstarkes, aber nicht wendiges Fahrzeug (stabile Fahrt)
        # Eine kurvige Strecke hingegen ein leistungsschwaches, aber wendiges Fahrzeug (darf nicht aus den Kurven geschleudert werden)
        # ausgeglichene Fahrzeuge haben weder Vorteile noch Nachteile
        # i.d.R. schließen sich Leistung und Wendigkeit gegenseitig aus
        if fahrzeug[0] == 3 and fahrzeug[1] == 1 and streckendaten_moment[1] == 3:
            Wagenvorteil = 5
        elif fahrzeug[0] == 1 and fahrzeug[1] == 3 and streckendaten_moment[1] == 1:
            Wagenvorteil = 5
        elif fahrzeug[0] == 3 and fahrzeug[1] == 1 and streckendaten_moment[1] == 3:
            Wagenvorteil = -5
        elif fahrzeug[0] == 1 and fahrzeug[1] == 3 and streckendaten_moment[1] == 1:
            Wagenvorteil = -5
        else:
            Wagenvorteil = 0

        #festgelegt, ob Zufallsbonus oder nicht
        if zufallszahl2 > 98:
            Glückstag = 50
        elif zufallszahl2 < 4:
            Glückstag = -50
        else:
            Glückstag = 0

        if zufallszahl1 + zufallszahl2 < fahrerdatenAktuell[2] * 2:
            Strafe = -20
        else:
            Strafe = 0

        #Wetter; 1-3: sonnig; 3-4: nass; 5-6: Regen
        Wetter = random.randint(1, 6)

        #Unfallwahrscheinlichkeiten
        if zufallszahl2 / 10 + fahrerdatenAktuell[3] < Wetter + Wetter / 2.5:
            Dreher = -40
        else:
            Dreher = 0
        # experimentelle Werte

        if zufallszahl1 == 1 and (
                streckendaten_moment[1] * fahrerdatenAktuell[2] * streckendaten_moment[2]) - Grunderfahrung > 190:
            Unfall = -70
        else:
            Unfall = 0
        # je höher die Schwierigkeit, je schneller der Kurs, je aggressiver der Fahrer, desto wahrscheinlicher ist ein Unfall
        # je erfahrener der Fahrer, desto unwahrscheinlicher der Unfall

        # Unfall mit einem anderen Fahrer später auswerten?

        if zufallszahl1 < 3:
            Boxenfehler = -50
        else:
            Boxenfehler = 0

        #Wenn Unfall, prüft, ob er schwer ist
        # hat der schwere Unfall zu einem Aus oder einer Disqualifikation geführt, dann ist der Fahrer Letzter
        if Unfall == -70 and zufallszahl1 == 1:
            SchwererUnfall = -100
        else:
            SchwererUnfall = 0

        if SchwererUnfall == -100 and random.randint(0, 101) < 11:
            Aus = -500
        else:
            Aus = 0

        # Neustartschance mit einbauen?
        # Wenn jemand einen schweren Unfall hatte, derjenige aber nicht rausgeflogen ist
        Neustart = 0

        #Gesamtergebnis wird berechnet
        Rennergebnis = zufallszahl1 + Grundstärke + Streckenbonus + Vorliebe + Wagenvorteil + zufallszahl2 + Glückstag + Strafe + Dreher + Unfall + Boxenfehler + SchwererUnfall + Aus + Neustart

        # falls zwei Fahrer exakt die selben Errechnungspunkte erreicht hat, entscheidet die Grundstärke, wer gewinnt
        Rennergebnis = Rennergebnis * 100000 + Grundstärke

        #Ergebnis wird als Tupel übergeben
        zusammenführung = [Rennergebnis, fahrername]

        Ergebnisliste.append(zusammenführung)

    return Ergebnisliste  # , Unfall, Rennergebnis?

def berechnenStarten(meisterschaft):
    global fensterBerechnen
    global labelInfo

    pfad = 'Datenbank/' + meisterschaft + '.dat'

    # Meisterschaftsdaten werden gelesen
    meisterschaftsdaten = Daten.lesen(pfad)

    #Liste der Strecken wird geladen
    streckenliste = Daten.lesen(meisterschaftsdaten[0])

    # Liste der Fahrer wird geladen
    fahrerliste = Daten.lesen(meisterschaftsdaten[1])

    #für jede Strecke in der Meisterschaft, tue das:
    for i in range(0, len(streckenliste)):
        pfad = streckenliste[i]

        #aktuelle Strecke wird gelesen
        streckendaten_moment = Daten.lesen(pfad)

        # Ergebnisliste wird wiedergegeben; sind ja nur die Rohdaten ohne Platzrierung
        Ergebnis = strecke_berechnen(streckendaten_moment, fahrerliste)  # , fahrzeugdaten)

        # Rangfolge berechnen, kleinste zuerst!! --> letzter ist ganz vorn, daher reverse
        # Problem: Die Punkte sind immer noch drin als Name
        Ergebnis.sort()
        Ergebnis.reverse()

        Streckenergebnis = []

        # nimm Element der Liste und ordne den richtigen Punktewert hinzu; vorgeschriebenes Punktesystem
        # Es sind noch die Berechnungswerte drin, sie werden jetzt mit den vom Punktesystem vorgesehenen Punkten ausgetauscht
        for j in range(0, len(Ergebnis)):
            
            aktuellesErgebnisElement = Ergebnis[j] #!Ergebnis ist ein Tupel! [Rennergebnis, Fahrername]

            if j == 0:
                aktuellesErgebnisElement[0] = 20
            elif j == 1:
                aktuellesErgebnisElement[0] = 18
            elif j == 2:
                aktuellesErgebnisElement[0] = 15
            elif j == 3:
                aktuellesErgebnisElement[0] = 14
            elif j == 4:
                aktuellesErgebnisElement[0] = 12
            elif j == 5:
                aktuellesErgebnisElement[0] = 10
            elif j == 6:
                aktuellesErgebnisElement[0] = 8
            elif j == 7:
                aktuellesErgebnisElement[0] = 5
            elif j == 8:
                aktuellesErgebnisElement[0] = 4
            elif j == 9:
                aktuellesErgebnisElement[0] = 2
            elif j == 10:
                aktuellesErgebnisElement[0] = 1
            else:
                aktuellesErgebnisElement[0] = 0

            Ergebnis[j] = aktuellesErgebnisElement

            # Idee: ein Element wird herausgenommen, dann wird der Name und die Punktzahl extrahiert, zugeordnet und temporär (wegen Benennung) gespeichert?
            Punkte = []

            einzelnesFahrerergebnis = Ergebnis[j] #hier ist ja ein Tupel drin

            # Name nun einzeln
            einzelnesFahrerergebnisName = einzelnesFahrerergebnis[1]

            # Punkte nun einzeln
            Punkte.append(einzelnesFahrerergebnis[0])

            #Streckenergebnis wird abgespeichert
            Streckenergebnis.append(einzelnesFahrerergebnisName)

            #jeder Fahrer erhält eine temporäre Datei, in der die bisher erreichten Punkte stehen
            temporärerPfad = 'temporäre Dateien/' + einzelnesFahrerergebnisName + '.dat'

            #teste, ob schon da, wenn nicht, erstelle
            #liest bisherige Punkte aus
            try:
                erreichtePunkte = Daten.lesen(temporärerPfad)

            except:
                Daten.schreiben(temporärerPfad, [0, 0]) #Tupel, damit als Liste erkannt
                erreichtePunkte = Daten.lesen(temporärerPfad)            

            #fügt alle Punkte in einer Liste zusammen
            for p in range(0, len(erreichtePunkte)):
                Punkte.append(erreichtePunkte[p])

            # eine Liste wird mit der Punktzahl gespeichert
            Daten.schreiben(temporärerPfad, Punkte)

            # jeder Fahrer hat nun unter temporäre Dateien eine Liste mit seinen errungenen Punkten. Sie muss nur noch zusammengezählt werden

        # Abspeichern und Auswerten:

        prüfung = 0
        prüfziffer = 1

        # Schleife soll herausfinden, ob es eine solche Datei schon gibt, denn ältere Dateien sollen nicht überschrieben werden
        #solange die Prüfung 0 ist, teste
        while prüfung == 0:
            rennpfad = 'Datenbank/Meisterschaften/' + str(meisterschaft) + str(prüfziffer) + 'Rennergebnisse' + \
                        streckenliste[i].replace('Datenbank/Strecken/', '') #mit neuer Prüfziffer
            
            try:
                # pfad wird geöffnet --> wenn es glückt, dann existiert der Pfad schon
                platzhalter = Daten.lesen(rennpfad)

                # eine andere Prüfziffer wird verwendet, mit ihr wird es noch mal probiert
                prüfziffer = prüfziffer + 1
            except:
                # das Programm springt aus der Schleife heraus
                prüfung = 1

        # Streckenergebnis wird mit Punkten gespeichert
        Daten.schreiben(rennpfad, Ergebnis)
        
        # txt-Datei anlegen, unter selben Namen speichern, oder gleich html? über s.format/Platzhalter; zur Not Zugriff auf temporäre Dateien?

    # Ergebnisse werden gelesen und die Meisterschaft wird ausgewertet

    Rangliste = []

    #für jeden Fahrer der Meisterschaft, tue das:
    for i in range(0, len(fahrerliste)):

        berechnungspfad = 'temporäre Dateien/' + fahrerliste[i].replace('Datenbank/Fahrer/', '')

        # die temporären Dateien werden gelesen, dort ist für jeden Fahrer eine Datei mit seinen errungenen Punkten gespeichert
        errungenePunkteeinzeln = Daten.lesen(berechnungspfad)

        Punktzahl = 0

        #addiere alle Punkte zusammen
        # die Gesamtpunktzahl des Fahrers wird ermittelt, in dem jedes Listenelement genommen wird und addiert wird
        for j in range(0, len(errungenePunkteeinzeln)):
            Punktzahl = Punktzahl + errungenePunkteeinzeln[j]  
            # Element 1 von "Punkte" ist eine Liste, warum? --> weil ein Tupel zuerst gespeichert wird; gibt es Probleme?

        #nimmt das ".dat aus dem Namen heraus"
        fahrername = fahrerliste[i].replace('.dat', '')

        #Puntgenauigkeit bis zu 9999, da die ersten Ziffern 00; soll richtig berechnen bei Sortierung
        if Punktzahl < 10:
            Punktzahl = '00' + str(Punktzahl)
        elif Punktzahl < 100:
            Punktzahl = '0' + str(Punktzahl)

        # es wird eine Liste erstellt, die aus der Punktzahl und dem Fahrernamen besteht
        PunktzahlFahrername = str(Punktzahl) + ' ' + fahrername.replace('Datenbank/Fahrer/', '')
        Rangliste.append(PunktzahlFahrername)

        # die verwendete temporäre Datei wird überschrieben, sodass nur noch 0 drin steht
        Daten.schreiben(berechnungspfad, [0, 0])

    Rangliste.sort()
    Rangliste.reverse()
    # die Liste wird nach Punktzahl sortiert

    prüfung = 0
    prüfziffer = 1

    #solange Prüfung 0 ist, teste das
    while prüfung == 0:

        # pfad wird erstellt
        speicherpfad = 'Datenbank/Meisterschaften/' + str(meisterschaft) + str(
                prüfziffer) + 'Meisterschaftsergebnisse' + '.dat'
        
        try:
            # pfad wird geöffnet --> wenn es glückt, dann existiert der Pfad schon
            platzhalter = Daten.lesen(speicherpfad)

            # eine andere Prüfziffer wird verwendet, mit ihr wird es noch mal probiert
            prüfziffer = prüfziffer + 1
        except:
            # das Programm springt aus der Schleife heraus
            prüfung = 1

    Daten.schreiben(speicherpfad, Rangliste)

    #TODO Ausgabe
    # geht auch komplizierter, mit Textverarbeitung etc.//txt und html?
    # die Liste wird wiedergegeben

    labelInfo.config(text = Rangliste)

    #zurück ins Menü   