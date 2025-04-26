# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Menü zur Erstellung einer Strecke

import time
from tkinter import *
import Daten    #Lesen, Schreiben von Dateien
import os

# sammelt alle Daten ein, erstellt die Strecke und schließt das Fenster
def StreckeFertig():
    global entryAuswählen #Rekordhalter
    global fensterErstellenStrecke
    global entryName
    global streckentyp
    global scaleSchwierigkeit
    global labelInfo
    global streckenname

    streckendaten = []
    streckendaten.append(entryAuswählen.get())
    streckendaten.append(int(streckentyp.get()))
    streckendaten.append(scaleSchwierigkeit.get())

    streckenname = entryName.get()

    pfad = "Datenbank/Strecken/" + streckenname + ".dat"
    
    Daten.schreiben(pfad, streckendaten)

    #TODO Fehler abfangen

    #gibt Info, dass Strecke erstellt wurde
    labelInfo.config(text = "Strecke wird erstellt...")
    labelInfo.update_idletasks()

    time.sleep(0.5)

    #zerstören
    fensterErstellenStrecke.destroy()

    #fensterErstellenStrecke.wait_window()

# fügt Fahrer in Entry aus fensterErstellenStrecke ein --> Name ist definitiv richtig; zerstört danach fensterErstellenStreckeFahrerauswählen
def fügeFahrerein():
    global Fahrer
    global entryAuswählen
    global fensterErstellenStreckeFahrerauswählen

    ausgewählterFahrer = Fahrer.get()

    #vielleicht vorher leeren
    entryAuswählen.insert(0, ausgewählterFahrer)

    fensterErstellenStreckeFahrerauswählen.destroy()

# erstellt Fenster, in dem alle Fahrer angezeigt werden. Mit Radiobuttons Auswahl des Fahrers aus Datenbank möglich
def FahrerAuswählen():
    global Fahrer
    global fensterErstellenStreckeFahrerauswählen

    fensterErstellenStreckeFahrerauswählen = Toplevel()
    fensterErstellenStreckeFahrerauswählen.title("Fahrer auswählen - Mebe V2.0.0")
    fensterErstellenStreckeFahrerauswählen.geometry("800x600")

    labelTitelErstellenStrecke = Label(master=fensterErstellenStreckeFahrerauswählen,
                                        text="Wähle Fahrer aus",
                                        font=('', 15))
    labelTitelErstellenStrecke.pack()

    Fahrer = StringVar()

    #listeFahrer = Daten.lesen('Datenbank/Fahrer/000 - Verzeichnis Fahrer.dat')
    listeFahrer = os.listdir('Datenbank/Fahrer')

    buttonauswählen = Button(master = fensterErstellenStreckeFahrerauswählen, text = "Fahrer auswählen", command = fügeFahrerein)
    buttonauswählen.pack()

    #für jedes Element der Liste (also alle Fahrer) wird ein Radiobutton erzeugt
    for i in range(0, len(listeFahrer)):

        #formated String in Radiobutton wird gesetzt
        textFahrer = listeFahrer[i]
        textFahrer = textFahrer.replace('.dat', '')

        radioFahrer = Radiobutton(master = fensterErstellenStreckeFahrerauswählen, text = f"{textFahrer}", 
                                  value = str(textFahrer), variable = Fahrer)
        radioFahrer.pack()

    Fahrer.set(textFahrer)

def StreckeErstellen():
    global entryAuswählen
    global fensterErstellenStrecke
    global entryName
    global streckentyp
    global scaleSchwierigkeit
    global labelInfo

    fensterErstellenStrecke = Toplevel()
    fensterErstellenStrecke.title("Erstelle Strecke - Mebe V2.0.0")
    fensterErstellenStrecke.geometry("800x600")

    labelTitelErstellenStrecke = Label(master=fensterErstellenStrecke,
                                        text="Erstelle Strecke",
                                        font=('', 15))
    labelTitelErstellenStrecke.pack()

    labelName = Label(master = fensterErstellenStrecke, text = "Name der Strecke:")
    labelName.pack()

    entryName = Entry(master = fensterErstellenStrecke)
    entryName.pack()

    labelRekordhalter = Label(master = fensterErstellenStrecke, text = "Wer ist der Rekordhalter?")
    labelRekordhalter.pack()

    #Radiobuttons zu lang?
    #askopenfilename? Entry? --> Mit Warnung ob existiert?

    entryAuswählen = Entry(master = fensterErstellenStrecke)
    entryAuswählen.pack()

    buttonAuswählen = Button(master = fensterErstellenStrecke, text = "Fahrer aus Datenbank auswählen...", command = FahrerAuswählen)
    buttonAuswählen.pack()

    labelStreckentyp = Label(master = fensterErstellenStrecke, text = "Auswahl des Streckentyps:")
    labelStreckentyp.pack()

    streckentyp = StringVar()
    kurvig = Radiobutton(master = fensterErstellenStrecke, text = "Kurvige Strecke", value = 1, variable = streckentyp)
    ausgeglichen = Radiobutton(master = fensterErstellenStrecke, text = "Ausgeglichene Strecke", value = 2, variable = streckentyp)
    schnell = Radiobutton(master = fensterErstellenStrecke, text = "Schnelle Strecke", value = 3, variable = streckentyp)
    kurvig.select()

    kurvig.pack()
    ausgeglichen.pack()
    schnell.pack()

    labelSchwierigkeit = Label(master = fensterErstellenStrecke, text = "Auswahl der Schwierigkeit:")
    labelSchwierigkeit.pack()

    scaleSchwierigkeit = Scale(master = fensterErstellenStrecke, from_= 1, to = 10, orient=HORIZONTAL)
    scaleSchwierigkeit.pack()

    buttonerstellen = Button(master = fensterErstellenStrecke, text = "Strecke erstellen", command = StreckeFertig)
    buttonerstellen.pack()

    labelInfo = Label(master=fensterErstellenStrecke, text='', font=('', 15))
    labelInfo.pack()