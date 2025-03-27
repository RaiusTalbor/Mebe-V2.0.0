# Motorsportmeisterschaftsberechner
# Mebe V2.0.0

import pickle
import random
import time
from tkinter import *


# ----------Hauptmenüknopffunktionen

# Idee: Knopf soll einen Stream öffnen, bei der alle hinterlegten Dateien gespeichert sind. Er soll alle anzeigen
# Über ein weiteres Menü Auswahl zur Bearbeitung, neu erstellen, neue Meisterschaft, Meisterschaften

# ----------Test

def test():
    pass

#----------RunMebe1

Anzeigenspeicher = ["Willkommen in Mebe V1! Dies ist die alte Version.",
                    "Sie ist kompatibel mit Deinen alten Dateien.",
                    "Kopiere sie in die richtigen Ordner, damit das Programm ordnungsgemäß funktioniert.",
                    "Viel Spaß!"]

def RunMebe1():
    # Mebe 2 hat Mebe 1 implementiert, was bedeutet, dass Mebe 1 in Mebe 2 integriert und unabhängig funktioniert
    # die alten Daten und das vereinfachte Programm können verwendet werden

    #global Warte
    Warte=0

    fensterMebe1 = Tk()
    fensterMebe1.title("Running Mebe V1.0.0")
    fensterMebe1.geometry("1000x800")

    labelFensterMebe1 = Label(master=fensterMebe1,
                              width=300, height=20)

    entryMebe1=Entry(master=fensterMebe1)

    def Wartenbeenden():
        global Warte
        Warte=1
        return Warte

    knopfentry=Button(master=fensterMebe1, text="Eingabe", command=Wartenbeenden)

    def drucken(text):
        
        global Anzeigenspeicher
        
        AnzeigenspeicherMax=4
        Anzeigenspeicher.append(text)

        if Anzeigenspeicher[AnzeigenspeicherMax] != None:
            Anzeigenspeich=Anzeigenspeicher[0]
            Anzeigenspeicher.remove(Anzeigenspeich)

        Labeltextfinal=""
        for i in range(len(Anzeigenspeicher)):
            Zeilenumbruch="\n"
            Labeltextfinal = str(Labeltextfinal) + str(Anzeigenspeicher[i]) + str(Zeilenumbruch)

        labelFensterMebe1.config(text=Labeltextfinal)

    def eingabe(text):
        drucken(text)
        global Warte
        while Warte==0:
            pass
        Warte=0
        NeueEingabe=entryMebe1.get()

        return NeueEingabe

    labelFensterMebe1.pack()
    entryMebe1.pack()
    knopfentry.pack()

#----------Mebe1
    MENÜ = '''
    MENÜ
    --------------------------------------
    Meisterschaft berechnen (1)
    Meisterschaft öffnen (WIP!!!) (2)
    Meisterschaft erstellen (3)
    Meisterschaft bearbeiten (4)
    Programm beenden :( (5)
    '''

    # Unterprogramme der Hauptmenüfunktionen

    def strecken_einfügen():
        # aus erstellen

        # elegantere Lösung durch Dialogfeldauswahl? Dass ich im Dialogfeld die Strecken auswähle?
        # Ansicht, welche Strecken überhaupt zur Verfügung stehen?
        # Möglichkeit der Kopie?

        meisterschaftsstrecken = []
        # in meisterschaftsstrecken wird die Liste der Strecken gespeichert

        stopp = 0

        while stopp != 'e':

            pfad = eingabe('Strecke hinzufügen:')
            pfad += '.dat'
            pfad = 'Datenbank/Strecken/' + pfad

            try:
                # sucht die Strecke im Verzeichnis. Ansonsten wird sie neu angelegt.

                f = open(pfad, 'rb')
                platzhalter = pickle.load(f)
                f.close()
                Versuch = 0

            except:
                drucken('Strecke existiert noch nicht!')
                Versuch = 1

            if Versuch == 1:
                # wenn es fehlgeschlagen ist, wird eine neue Strecke angelegt

                f = open(pfad, 'wb')

                drucken('Es wird eine neue Strecke angelegt!')

                streckeneigenschaften = []

                streckeneigenschaften.append(eingabe('Wer fuhr die Rekordzeit?'))
                streckeneigenschaften.append(
                    int(eingabe('Welcher Streckentyp (zwischen 1 und 3)? Je höher, desto schneller ist die Strecke.')))
                streckeneigenschaften.append(int(eingabe('Wie hoch ist die Schwierigkeit (zwischen 1 und 10)?')))

                pickle.dump(streckeneigenschaften, f)
                f.close()

            meisterschaftsstrecken.append(pfad)

            stopp = eingabe('Eine weitere Strecke hinzufügen? Wenn nicht, dann drücke "e"!')

        return meisterschaftsstrecken

    def fahrer_einfügen():
        # aus erstellen

        # elegantere Lösung durch Dialogfeldauswahl? Dass ich im Dialogfeld die Fahrer auswähle?
        # Ansicht, welche Fahrer überhaupt zur Verfügung stehen?
        # Möglichkeit der Kopie aus anderer Meisterschaft?

        meisterschaftsfahrer = []
        # in meisterschaftsfahrer wird die Liste der Fahrer gespeichert

        stopp = 0

        while stopp != 'e':

            Pilotenname = eingabe('Name des Piloten? Denke an den Namenszusatz, wenn Du sein Profil mit einer Meisterschaft verknüpft hast!')
            pfad = Pilotenname + '.dat'
            pfad = 'Datenbank/Fahrer/' + pfad

            try:
                # sucht den Piloten im Verzeichnis. Ansonsten wird er neu angelegt.

                f = open(pfad, 'rb')
                platzhalter = pickle.load(f)
                f.close()
                Versuch = 0

            except:
                drucken('Fahrer existiert noch nicht!')
                Versuch = 1

            if Versuch == 1:
                # wenn es fehlgeschlagen ist, wird ein neuer Fahrer angelegt

                f = open(pfad, 'wb')

                drucken('Es wird ein neues Fahrerprofil angelegt!')

                fahrereigenschaften = []

                fahrereigenschaften.append(int(eingabe('In welchem Jahr wurde der Pilot geboren?')))
                fahrereigenschaften.append(int(eingabe('In welchem Jahr fuhr der Fahrer das erste Mal?')))
                fahrereigenschaften.append(
                    int(eingabe('Wie aggressiv fährt der Pilot (Wert zw. 1 und 10)? Je höher, desto aggressiver.')))
                fahrereigenschaften.append(
                    int(eingabe('Wie geschickt fährt der Fahrer (Wert zw. 1 und 10)? Je höher, desto geschickter.')))
                fahrereigenschaften.append(int(eingabe(
                    'Wie hoch ist das Grundkönnen des Fahrers (Wert zw. 1 und 100 im Vergleich zum besten Fahrer nach eigener Einschätzung)? Je höher, desto besser.')))
                z = (int(eingabe('Hat der Fahrer eine Vorliebe für schnelle Strecken? Wenn ja, drücke "2"')))
                if z != 2:
                    z = 1
                fahrereigenschaften.append(z)
                fahrereigenschaften.append(
                    int(eingabe('Wie ist die Durchschnittliche Platzierung des Fahrers? Achtung, Ganzzahlen!')))
                fahrereigenschaften.append(eingabe('Mit welchem Fahrzeug fährt der Fahrer?'))  # auswählen lassen???
                fahrereigenschaften.append(int(eingabe(
                    'Seit welchem Jahr fährt er sein Fahrzeug (wenn er die Jahre zuvor mit derselben Marke gefahren ist, zählt es dazu)?')))
                fahrereigenschaften.append(Pilotenname)

                pickle.dump(fahrereigenschaften, f)
                f.close()

            meisterschaftsfahrer.append(pfad)

            stopp = eingabe('Einen weiteren Piloten hinzufügen? Wenn nicht, dann drücke "e"!')

        return meisterschaftsfahrer

    def fahrzeuge_einfügen():
        # aus erstellen

        # dies dient nur zur Absicherung für die Piloten, dass alle Fahrzeuge existieren, die die Piloten fahren soll; wird nicht bei der Meisterschaft gespeichert!

        # elegantere Lösung durch Dialogfeldauswahl? Dass ich im Dialogfeld die Fahrzeuge auswähle?
        # Ansicht, welche Fahrzeuge überhaupt zur Verfügung stehen?
        # Möglichkeit der Kopie?

        stopp = 0
        meisterschaftsfahrzeuge = []

        while stopp != 'e':

            pfad = eingabe(
                'Name des Fahrzeugs? Hast Du keine Typbezeichnung, nutze den Markennamen und die Meisterschaft als Name.')
            pfad += '.dat'
            pfad = 'Datenbank/Fahrzeuge/' + pfad

            try:
                # sucht das Fahrzeug im Verzeichnis. Ansonsten wird es neu angelegt.

                f = open(pfad, 'rb')
                platzhalter = pickle.load(f)
                f.close()
                Versuch = 0

            except:
                drucken('Fahrzeug existiert noch nicht!')
                Versuch = 1

            if Versuch == 1:
                # wenn es fehlgeschlagen ist, wird ein neuer Fahrer angelegt

                f = open(pfad, 'wb')

                drucken('Es wird ein neues Fahrzeug angelegt!')

                fahrzeugeigenschaften = []

                fahrzeugeigenschaften.append(int(eingabe(
                    'Wie ist die Leistung im Vergleich zu den anderen Fahrzeugen (zw. 1 bis 3)? Je höher, desto besser.')))
                fahrzeugeigenschaften.append(int(eingabe(
                    'Wie ist die Wendigkeit im Vergleich zu den anderen Fahrzeugen (zw. 1 bis 3)? Je höher, desto besser.')))

                pickle.dump(fahrzeugeigenschaften, f)
                f.close()

            meisterschaftsfahrzeuge.append(pfad)

            stopp = eingabe('Ein weiteres Fahrzeug hinzufügen? Wenn nicht, dann drücke "e"!')

    def strecke_berechnen(streckendaten_moment, fahrerdaten):  # , fahrzeugdaten):

        Ergebnisliste = []

        for i in range(0, len(fahrerdaten)):

            pfad = fahrerdaten[i]

            f = open(pfad, 'rb')
            fahrerdaten_aktuell = pickle.load(f)
            f.close()

            name = fahrerdaten_aktuell[9]

            pfadfahrzeuge = 'Datenbank/Fahrzeuge/' + fahrerdaten_aktuell[7] + '.dat'

            f = open(pfadfahrzeuge, 'rb')
            fahrzeug = pickle.load(f)
            f.close()

            zufallszahl1 = random.randint(0, 101)
            zufallszahl2 = random.randint(0, 101)

            Alter = time.localtime()
            Alter = Alter.tm_year
            Alter = Alter - fahrerdaten_aktuell[0]
            # wie alt

            FahrerSeit = time.localtime()
            FahrerSeit = FahrerSeit.tm_year
            FahrerSeit = FahrerSeit - fahrerdaten_aktuell[1]
            # wie lange Fahrer

            FährtAutoSeit = time.localtime()
            FährtAutoSeit = FährtAutoSeit.tm_year
            FährtAutoSeit = FährtAutoSeit - fahrerdaten_aktuell[8]
            # wie lange fährt schon Auto

            Grunderfahrung = Alter + FahrerSeit

            Grundstärke = Grunderfahrung + fahrerdaten_aktuell[4] + FährtAutoSeit * 2

            if streckendaten_moment[0] in pfad:
                Streckenbonus = 5
            else:
                Streckenbonus = 0

            if fahrerdaten_aktuell[5] == 2:
                if streckendaten_moment[1] == 3:
                    Vorliebe = 5
                else:
                    Vorliebe = 0
            else:
                if streckendaten_moment[1] == 1:
                    Vorliebe = 5
                else:
                    Vorliebe = 0
            # Hat der Fahrer eine Vorliebe für schnelle Strecken, so wird geprüft, ob die Strecke schnell ist.
            # Hat der Fahrer sie nicht, wird geprüft, ob die Strecke kurvig ist. Passen hier auch die Werte zusammen, gibt es die Punkte

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
            # Eine schnelle Strecke verlangt ein leistungsstarkes, aber nicht wendiges Fahrzeug (stabile Fahrt)
            # Eine kurvige Strecke hingegen ein leistungsschwaches, aber wendiges Fahrzeug (darf nicht aus den Kurven geschleudert werden)
            # ausgeglichene Fahrzeuge haben weder Vorteile noch Nachteile
            # i.d.R. schließen sich Leistung und Wendigkeit gegenseitig aus

            if zufallszahl2 > 98:
                Glückstag = 50
            elif zufallszahl2 < 4:
                Glückstag = -50
            else:
                Glückstag = 0

            if zufallszahl1 + zufallszahl2 < fahrerdaten_aktuell[2] * 2:
                Strafe = -20
            else:
                Strafe = 0

            Wetter = random.randint(1, 6)
            # 1-3: sonnig; 3-4: nass; 5-6: Regen

            if zufallszahl2 / 10 + fahrerdaten_aktuell[3] < Wetter + Wetter / 2.5:
                Dreher = -40
            else:
                Dreher = 0
            # experimentelle Werte

            if zufallszahl1 == 1 and (
                    streckendaten_moment[1] * fahrerdaten_aktuell[2] * streckendaten_moment[2]) - Grunderfahrung > 190:
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

            if Unfall == -70 and zufallszahl1 == 1:
                SchwererUnfall = -100
            else:
                SchwererUnfall = 0

            if SchwererUnfall == -100 and random.randint(0, 101) < 11:
                Aus = -500
            else:
                Aus = 0
            # hat der schwere Unfall zu einem Aus oder einer Disqualifikation geführt, dann ist der Fahrer Letzter

            # Neustartschance mit einbauen?
            # Wenn jemand einen schweren Unfall hatte, derjenige aber nicht rausgeflogen ist
            Neustart = 0

            Rennergebnis = zufallszahl1 + Grundstärke + Streckenbonus + Vorliebe + Wagenvorteil + zufallszahl2 + Glückstag + Strafe + Dreher + Unfall + Boxenfehler + SchwererUnfall + Aus + Neustart

            Rennergebnis = Rennergebnis * 100000 + Grundstärke  # falls zwei Fahrer exakt die selben Errechnungspunkte erreicht hat, entscheidet die Grundstärke, wer gewinnt

            zusammenführung = [Rennergebnis, name]

            Ergebnisliste.append(zusammenführung)

        return Ergebnisliste  # , Unfall, Rennergebnis?

    # Hauptmenüfunktionen

    def berechnen():

        eingabe = eingabe('''
    Welche Meisterschaft soll geladen werden?
    ''')

        drucken('''
    Meisterschaft wird berechnet...
    ''')

        pfad = 'Datenbank/' + eingabe + '.dat'

        f = open(pfad, 'rb')
        meisterschaftsdaten = pickle.load(f)  # Meisterschaftsdaten werden gelesen
        f.close()

        f = open(meisterschaftsdaten[0], 'rb')
        streckendaten = pickle.load(f)
        f.close()
        # Liste der Strecke wird geladen

        f = open(meisterschaftsdaten[1], 'rb')
        fahrerdaten = pickle.load(f)
        f.close()
        # Liste der Fahrer wird geladen

        for i in range(0, len(streckendaten)):
            pfad = streckendaten[i]

            f = open(pfad, 'rb')
            streckendaten_moment = pickle.load(f)
            f.close()

            Ergebnis = strecke_berechnen(streckendaten_moment, fahrerdaten)  # , fahrzeugdaten)
            # Ergebnisliste wird wiedergegeben

            Ergebnis.sort()
            Ergebnis.reverse()
            # Rangfolge berechnen, kleinste zuerst!!
            # Problem: Die Punkte sind immer noch drin als Name

            # nimm Element der Liste und ordne den richtigen Punktewert hinzu; vorgeschriebenes Punktesystem
            for e in range(0, len(Ergebnis)):
                zwischenspeicher = Ergebnis[e]

                if e == 0:
                    zwischenspeicher[0] = 20
                elif e == 1:
                    zwischenspeicher[0] = 18
                elif e == 2:
                    zwischenspeicher[0] = 15
                elif e == 3:
                    zwischenspeicher[0] = 14
                elif e == 4:
                    zwischenspeicher[0] = 12
                elif e == 5:
                    zwischenspeicher[0] = 10
                elif e == 6:
                    zwischenspeicher[0] = 8
                elif e == 7:
                    zwischenspeicher[0] = 5
                elif e == 8:
                    zwischenspeicher[0] = 4
                elif e == 9:
                    zwischenspeicher[0] = 2
                elif e == 10:
                    zwischenspeicher[0] = 1
                else:
                    zwischenspeicher[0] = 0
                # Es sind noch die Berechnungswerte drin, sie werden jetzt mit den vom Punktesystem vorgesehenen Punkten ausgetauscht
                Ergebnis[e] = zwischenspeicher
                # neue Werte werden wieder eingefügt
            # Idee: ein Element wird herausgenommen, dann wird der Name und die Punktzahl extrahiert, zugeordnet und temporär (wegen Benennung) gespeichert?

            Streckenergebnis = []

            for m in range(0, len(Ergebnis)):
                Punkte = []

                Listendatei = Ergebnis[m]

                ListendateiName = Listendatei[1]
                # Name nun einzeln

                Punkte.append(Listendatei[0])
                # Punkte nun einzeln

                Streckenergebnis.append(ListendateiName)
                temporärerPfad = 'temporäre Dateien/' + ListendateiName + '.dat'

                try:
                    f = open(temporärerPfad, 'rb')
                    Datenlesen = pickle.load(f)
                    f.close()

                except:
                    f = open(temporärerPfad, 'wb')
                    pickle.dump([0, 0], f)
                    f.close()

                f = open(temporärerPfad, 'rb')
                Datenlesen = pickle.load(f)
                f.close()

                for p in range(0, len(Datenlesen)):
                    Punkte.append(Datenlesen[p])

                f = open(temporärerPfad, 'wb')
                pickle.dump(Punkte, f)
                f.close()
                # eine Liste wird mit der Punktzahl gespeichert

                # jeder Fahrer hat nun unter temporäre Dateien eine Liste mit seinen errungenen Punkten. Sie muss nur noch zusammengezählt werden

            # Abspeichern und Auswerten:

            prüfung = 0
            prüfziffer = 1

            # Schleife soll herausfinden, ob es eine solche Datei schon gibt, denn ältere Dateien sollen nicht überschrieben werden:
            while prüfung == 0:
                try:
                    rennpfad = 'Datenbank/Meisterschaften/' + str(eingabe) + str(prüfziffer) + 'Rennergebnisse' + \
                               streckendaten[i].replace('Datenbank/Strecken/', '')
                    # pfad wird erstellt
                    f = open(rennpfad, 'rb')
                    # pfad wird geöffnet --> wenn es glückt, dann existiert der Pfad schon
                    platzhalter = pickle.load(f)
                    prüfziffer = prüfziffer + 1
                    # eine andere Prüfziffer wird verwendet, mit ihr wird es noch mal probiert
                    f.close()
                except:
                    prüfung = 1
                    rennpfad = 'Datenbank/Meisterschaften/' + str(eingabe) + str(prüfziffer) + 'Rennergebnisse' + \
                               streckendaten[i].replace('Datenbank/Strecken/', '')
                    # das Programm springt aus der Schleife heraus

            f = open(rennpfad, 'wb')
            pickle.dump(Ergebnis, f)
            f.close()
            # Streckenergebnis wird mit Punkten gespeichert
            # txt-Datei anlegen, unter selben Namen speichern, oder gleich html? über s.format/Platzhalter; zur Not Zugriff auf temporäre Dateien?

        # Ergebnisse werden gelesen und die Meisterschaft wird ausgewertet

        Rangliste = []
        for i in range(0, len(fahrerdaten)):
            berechnungspfad = 'temporäre Dateien/' + fahrerdaten[i].replace('Datenbank/Fahrer/', '')
            f = open(berechnungspfad, 'rb')
            errungenePunkteeinzeln = pickle.load(f)
            f.close()
            # die temporären Dateien werden gelesen, dort ist für jeden Fahrer eine Datei mit seinen errungenen Punkten gespeichert

            Punktzahl = 0
            for m in range(0, len(errungenePunkteeinzeln)):
                Punktzahl = Punktzahl + errungenePunkteeinzeln[m]  # Element 1 von "Punkte" ist eine Liste, warum?
            # die Gesamtpunktzahl des Fahrers wird ermittelt, in dem jedes Listenelement genommen wird und addiert wird

            fahrername = fahrerdaten[i].replace('.dat', '')
            if Punktzahl < 10:
                Punktzahl = '00' + str(Punktzahl)
            elif Punktzahl < 100:
                Punktzahl = '0' + str(Punktzahl)
            Append = str(Punktzahl) + ' ' + fahrername.replace('Datenbank/Fahrer/', '')
            Rangliste.append(Append)
            # es wird eine Liste erstellt, die aus der Punktzahl und dem Fahrernamen besteht

            f = open(berechnungspfad, 'wb')
            pickle.dump([0, 0], f)
            f.close()
            # die verwendete temporäre Datei wird überschrieben, sodass nur noch 0 drin steht

        Rangliste.sort()
        Rangliste.reverse()
        # die Liste wird nach Punktzahl sortiert
        1  # über 100 Punkte erkennt er fasch...

        prüfung = 0
        prüfziffer = 1
        while prüfung == 0:
            try:
                speicherpfad = 'Datenbank/Meisterschaften/' + str(eingabe) + str(
                    prüfziffer) + 'Meisterschaftsergebnisse' + '.dat'
                # pfad wird erstellt
                f = open(speicherpfad, 'rb')
                # pfad wird geöffnet --> wenn es glückt, dann existiert der Pfad schon
                platzhalter = pickle.load(f)
                prüfziffer = prüfziffer + 1
                # eine andere Prüfziffer wird verwendet, mit ihr wird es noch mal probiert
                f.close()
            except:
                prüfung = 1
                speicherpfad = 'Datenbank/Meisterschaften/' + str(eingabe) + str(
                    prüfziffer) + 'Meisterschaftsergebnisse' + '.dat'
                # das Programm springt aus der Schleife heraus

        f = open(speicherpfad, 'wb')
        pickle.dump(Rangliste, f)
        f.close()

        print(Rangliste)  # geht auch komplizierter, mit Textverarbeitung etc.//txt und html?
        # die Liste wird wiedergegeben

        Menü()

    def erstellen():

        meisterschaftspfad = eingabe('Wie soll die Meisterschaft heißen? Schreibe ggf. auch die Jahreszahl dazu!')
        meisterschaftsname = meisterschaftspfad
        meisterschaftspfad = 'Datenbank/' + meisterschaftspfad + '.dat'
        # Datei für die Meisterschaft wird angelegt

        strecken = strecken_einfügen()

        fahrzeuge_einfügen()

        fahrer = fahrer_einfügen()
        # Elemente werden erstellt

        streckenpfad = 'Datenbank/' + meisterschaftsname + 'Strecken' + '.dat'
        fahrerpfad = 'Datenbank/' + meisterschaftsname + 'Fahrer' + '.dat'

        # jeweilige Listen werden einem Speichernamen zugeordnet, um die Unterordner zu minimieren und trotzdem Übersicht in der Datenbank zu wahren

        f = open(streckenpfad, 'wb')
        pickle.dump(strecken, f)
        f.close()

        f = open(fahrerpfad, 'wb')
        pickle.dump(fahrer, f)
        f.close()

        # f=open(fahrzeugpfad, 'wb')
        # pickle.dump(fahrzeuge, f)
        # f.close()
        # Listen werden gespeichert

        meisterschaftsdetails = [streckenpfad, fahrerpfad]
        # Pfade werden in Liste gespeichert

        f = open(meisterschaftspfad, 'wb')
        pickle.dump(meisterschaftsdetails, f)
        f.close()
        # in der Meisterschaftsdatei sind quasi nur noch die Pfade gespeichert, wo die Daten zu finden sind

        drucken('Abgeschlossen!')

        Menü()

    def bearbeiten():

        auswahl = eingabe('''
    (S)trecke bearbeiten
    (F)ahrer bearbeiten
    (A)uto/Fahrzeug bearbeiten
    (M)eisterschaft bearbeiten (WIP!!!)
    ''')

        if auswahl.lower() == 's':
            pfad = 'Datenbank/Strecken/'

        elif auswahl.lower() == 'f':
            pfad = 'Datenbank/Fahrer/'

        elif auswahl.lower() == 'a':
            pfad = 'Datenbank/Fahrzeuge/'

        elif auswahl.lower() == 'm':
            # pfad='Datenbank/'
            drucken('Work in Process! Diese Funktion ist in weiteren Updates geplant, bitte habe Geduld...')
            Menü()

        else:
            drucken('Fehler bei der Eingabe!')
            Menü()

        # bessere Menüzurückführung mit Sicherungsvariable??

        #BUG!!!
        #Der Pfad muss für jedes Element einzeln abgefragt werden, d.h., dass es jeweils in die IF gehört
        #Im jetzigen Zustand wird diese Frage IMMER gestellt, egal, was ich ausgewählt habe
        Pilotenname = eingabe(
            'Name der Strecke?')
        pfad = Pilotenname + '.dat'
        pfad = 'Datenbank/Fahrer/' + pfad

        eingabe_neu = eingabe('Wenn Du den Index des Wertes weißt, dann gebe ihn an. Ansonsten tippe (w)eiter.')

        try:
            platzhalter = eingabe_neu + 300  # prüfung, ob eingabe_neu eine Zahl ist  #funktioniert nicht!
        except:
            platzhalter = 1  # wenn es keine Zahl ist

        if platzhalter == 1:

            drucken('Eine Neudefinition ist nötig.')

            if auswahl == 's':  # wird sich erinnert, was geändert werden soll. Dann werden die Daten einfach überschrieben

                f = open(pfad, 'wb')

                streckeneigenschaften = []
                streckeneigenschaften.append(eingabe('Wer fuhr die Rekordzeit?'))
                streckeneigenschaften.append(
                    int(eingabe('Welcher Streckentyp (zwischen 1 und 3)? Je höher, desto schneller ist die Strecke.')))
                streckeneigenschaften.append(int(eingabe('Wie hoch ist die Schwierigkeit (zwischen 1 und 10)?')))

                pickle.dump(streckeneigenschaften, f)
                f.close()

            elif auswahl == 'a':

                f = open(pfad, 'wb')

                fahrzeugeigenschaften = []
                fahrzeugeigenschaften.append(int(eingabe(
                    'Wie ist die Leistung im Vergleich zu den anderen Fahrzeugen (zw. 1 bis 3)? Je höher, desto besser.')))
                fahrzeugeigenschaften.append(int(eingabe(
                    'Wie ist die Wendigkeit im Vergleich zu den anderen Fahrzeugen (zw. 1 bis 3)? Je höher, desto besser.')))

                pickle.dump(fahrzeugeigenschaften, f)
                f.close()

            elif auswahl == 'f':

                f = open(pfad, 'wb')

                fahrereigenschaften = []
                fahrereigenschaften.append(int(eingabe('In welchem Jahr wurde der Pilot geboren?')))
                fahrereigenschaften.append(int(eingabe('In welchem Jahr fuhr der Fahrer das erste Mal?')))
                fahrereigenschaften.append(
                    int(eingabe('Wie aggressiv fährt der Pilot (Wert zw. 1 und 10)? Je höher, desto aggressiver.')))
                fahrereigenschaften.append(
                    int(eingabe('Wie geschickt fährt der Fahrer (Wert zw. 1 und 10)? Je höher, desto geschickter.')))
                fahrereigenschaften.append(int(eingabe(
                    'Wie hoch ist das Grundkönnen des Fahrers (Wert zw. 1 und 100 im Vergleich zum besten Fahrer nach eigener Einschätzung)? Je höher, desto besser.')))
                z = (int(eingabe('Hat der Fahrer eine Vorliebe für schnelle Strecken? Wenn ja, drücke "2"')))
                if z != 2:
                    z = 1
                fahrereigenschaften.append(z)
                fahrereigenschaften.append(int(eingabe('Wie ist die Durchschnittliche Platzierung des Fahrers?')))
                fahrereigenschaften.append(eingabe('Mit welchem Fahrzeug fährt der Fahrer?'))
                fahrereigenschaften.append(int(eingabe(
                    'Seit welchem Jahr fährt er sein Fahrzeug (wenn er die Jahre zuvor mit derselben Marke gefahren ist, zählt es dazu)?')))
                fahrereigenschaften.append(Pilotenname)

                pickle.dump(fahrereigenschaften, f)
                f.close()

        else:
            f = open(pfad, 'wb')
            daten = f.read()  # Daten werden gelesen
            neuerWert = eingabe('Wie ist der neue Wert der zu verändernden Stelle?')
            eingabe_neu = int(eingabe_neu)
            daten[
                eingabe_neu] = neuerWert  # daten wird an vorhin eingegebener Stelle verändert, wie es in neuerWert eingegeben wurde
            pickle.dump(daten, f)  # veränderten Daten überschreiben die anderen Daten
            f.close

        drucken('Abgeschlossen!')

        Menü()

    def Menü():

        drucken(MENÜ)

        auswahl = int(eingabe('Was soll durchgeführt werden?'))

        if auswahl == 1:
            berechnen()
        elif auswahl == 2:
            drucken('Diese Option ist derzeit nicht verfügbar!')
            Menü()
        elif auswahl == 3:
            erstellen()
        elif auswahl == 4:
            bearbeiten()
        elif auswahl == 5:
            drucken('''
    Bis bald! :D

    Mebe V1.0.0''')
        else:
            drucken('Eine falsche Auswahl wurde angegeben!')
            Menü()

    Menü()

    fensterMebe1.mainloop()


#----------Fenster

fenster = Tk()
fenster.title("Mebe V2.0.0")
fenster.geometry("1000x800")

# ----------Hauptmenü

labelTitel = Label(master=fenster,
                   text="Mebe V2.0.0",
                   font=('', 18))
labelTitel.pack()

buttonSerien = Button(master=fenster,
                      text="Serien",
                      command=test)
buttonSerien.pack()

buttonMeisterschaften = Button(master=fenster,
                               text="Meisterschaften",
                               command=test)
buttonMeisterschaften.pack()

buttonStrecken = Button(master=fenster,
                        text="Strecken",
                        command=test)
buttonStrecken.pack()

buttonFahrzeuge = Button(master=fenster,
                         text="Fahrzeuge",
                         command=test)
buttonFahrzeuge.pack()

buttonFahrer = Button(master=fenster,
                      text="Fahrer",
                      command=test)
buttonFahrer.pack()

buttonErstellen = Button(master=fenster,
                         text="Erstellen",
                         command=test)
buttonErstellen.pack()

buttonBerechnen = Button(master=fenster,
                         text="Berechnen",
                         command=test)
buttonBerechnen.pack()

buttonHilfe = Button(master=fenster,
                     text="Hilfe",
                     command=test)
buttonHilfe.pack()

buttonMebe1 = Button(master=fenster,
                       text="Mebe 1",
                       command=RunMebe1)
buttonMebe1.pack()

buttonBeenden = Button(master=fenster,
                       text="Beenden",
                       command=test)
buttonBeenden.pack()

# ----------

fenster.mainloop()
