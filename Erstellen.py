# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Untermenü erstellen - ermöglicht das Erstellen einer komplett neuen Meisterschaft

import time
from tkinter import *
import Daten        #Lesen, Schreiben von Dateien
import ErstelleStrecke
import ErstelleFahrer
import os

global prüfung

prüfung = 0 #bleibt 0, wenn erstellt

#generiert, für das Scrollen mit dem Mausrad, geht aber nicht
def enable_mousewheel(target_canvas, widget):
    def on_mousewheel(event):
        if os.name == 'nt':  # Windows
            target_canvas.yview_scroll(-1 * int(event.delta / 120), "units")
        elif os.name == 'posix':
            if event.num == 4:
                target_canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                target_canvas.yview_scroll(1, "units")
        return "break"

    # Statt auf widget binden, besser direkt auf canvas (target_canvas)
    target_canvas.bind("<Enter>", lambda e: target_canvas.bind("<MouseWheel>", on_mousewheel))
    target_canvas.bind("<Leave>", lambda e: target_canvas.unbind("<MouseWheel>"))

    target_canvas.bind("<Enter>", lambda e: [target_canvas.bind("<Button-4>", on_mousewheel),
                                             target_canvas.bind("<Button-5>", on_mousewheel)])
    target_canvas.bind("<Leave>", lambda e: [target_canvas.unbind("<Button-4>"),
                                             target_canvas.unbind("<Button-5>")])

def aktualisiereFenster():
    #Canvas soll die Elemente in der Liste anzeigen, mit aktualisiere die aktuelle Liste

    global schleifenliste, vorhanden

    for i in range(len(radioAnzeigeListe)):
        radioAnzeigeListe[i].destroy()

    schleifenliste = []

    if varweiter == 1:
        schleifenliste = rennkalender

    if varweiter == 2:
        schleifenliste = fahrerliste

    vorhanden = IntVar()
    vorhanden.set(0)
    for i in range (len(schleifenliste)):
        text = schleifenliste[i].replace('.dat', '')
        radioAnzeigeVorhanden = Radiobutton(master=scroll_frameVorhanden, text=f"{text}", value=i, variable=vorhanden)
        radioAnzeigeVorhanden.pack(anchor='w')
        radioAnzeigeListe.append(radioAnzeigeVorhanden)
    
    scroll_frameVorhanden.update_idletasks()

#fügt Radiobutton-Auswahl hinzu
def hinzufügen():

    global varweiter
    global fahrer       #Radiobuttons
    global strecken     #Radiobuttons
    global rennkalender
    global fahrerliste

    #holt sich die Daten und speichert sie zwischen
    if varweiter == 1:
        rennkalender.append(strecken.get())
    
    if varweiter == 2:
        fahrerliste.append(fahrer.get())

    aktualisiereFenster()

#fügt entweder neuen Fahrer oder neue Strecke ein
def neuehinzufügen():
    global varweiter
    global rennkalender
    global fahrerliste

    if varweiter == 1:
        #füge nun die Auswahl hinzu
        ErstelleStrecke.StreckeErstellen()

        fensterErstellen.wait_window(ErstelleStrecke.fensterErstellenStrecke)

        #Pfad noch zusammenbauen
        #pfad = "Datenbank/Strecken" + ErstelleStrecke.streckenname + ".dat"
        pfad = ErstelleStrecke.streckenname

        rennkalender.append(pfad)

    if varweiter == 2:
        #füge nun die Auswahl hinzu
        ErstelleFahrer.FahrerErstellen()

        fensterErstellen.wait_window(ErstelleFahrer.fensterErstellenFahrer)

        #Pfad noch zusammenbauen
        pfad = ErstelleFahrer.Fahrername

        fahrerliste.append(pfad)

    aktualisiereFenster()

def entfernen():
    global varweiter
    global fahrer       #Radiobuttons
    global strecken     #Radiobuttons
    global rennkalender
    global fahrerliste
    global schleifenliste, vorhanden

    #holt sich die Daten und entfernt diese
    if varweiter == 1:
        rennkalender.pop(vorhanden.get())
    
    if varweiter == 2:
        fahrerliste.pop(vorhanden.get())

    aktualisiereFenster()

#zeigt jeweils das neue Fenster mit den neuen Einstellungen an
def weiter():
    global varweiter
    global textStrecke
    global textFahrer
    global meisterschaftspfad
    global strecken
    global fahrer
    global radio
    global entryNameeinfügen, labelNameeinfügen, labelJahreinfügen, entryJahreinfügen, labelTitelErstellen, fensterErstellen
    global buttonhinzufügen, buttonneuehinzufügen, buttonentfernen, rennkalender, fahrerliste, meisterschaftspfad, prüfung

    #Der Cntainer, in dem sich die Radios befinden
    global canvas, scroll_frame, scrollbar, frame_canvas, frame_canvasVorhanden, scroll_frameVorhanden

    varweiter += 1

    # Fenster 2 - Strecken hinzufügen
    if varweiter == 1:

        #Meisterschaftsdatei anlegen
        if prüfung == 0:
            meisterschaftspfad = entryNameeinfügen.get()
        #wird in fertig aufgegriffen

        #zerstören der vorigen Elemente
        labelNameeinfügen.destroy()
        labelJahreinfügen.destroy()
        #labelSerieeinfügen.destroy()
        entryJahreinfügen.destroy()
        entryNameeinfügen.destroy()
        #entrySerieeinfügen.destroy()

        buttonhinzufügen.pack()
        buttonneuehinzufügen.pack()
        buttonentfernen.pack()

        # Scrollbare Frame-Struktur erstellen
        frame_canvas = Frame(fensterErstellen)
        frame_canvas.pack(fill=BOTH, expand=True, side=LEFT)

        canvas = Canvas(frame_canvas)
        scrollbar = Scrollbar(frame_canvas, orient=VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scroll_frame = Frame(canvas)
        canvas.create_window((0, 0), window=scroll_frame, anchor='nw')
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        #enable_mousewheel(canvas, scroll_frame)

        #labelTitelErstellen.config(text = "Erstellen einer Meisterschaft - Strecken hinzufügen")
        #Hinweis: In Reihenfolge des Rennkalenders

        #listeStrecken = Daten.lesen('Datenbank/Strecken/000 - Verzeichnis Strecken.dat')
        listeStrecken = os.listdir('Datenbank/Strecken')

        strecken = StringVar()

        for i in range(len(listeStrecken)):
            textStrecke = listeStrecken[i].replace('.dat', '')
            radioStrecken = Radiobutton(master=scroll_frame, text=f"{textStrecke}", value=listeStrecken[i], variable=strecken)
            radioStrecken.pack(anchor='w')
            radio.append(radioStrecken)

        if listeStrecken:
            strecken.set(listeStrecken[-1])

        #Scrollbare Frame-Struktur erstellen
        frame_canvasVorhanden = Frame(fensterErstellen)
        frame_canvasVorhanden.pack(fill=BOTH, expand=True, side=LEFT)

        canvasVorhanden = Canvas(frame_canvasVorhanden)
        scrollbarVorhanden = Scrollbar(frame_canvasVorhanden, orient=VERTICAL, command=canvasVorhanden.yview)
        canvasVorhanden.configure(yscrollcommand=scrollbarVorhanden.set)

        scrollbarVorhanden.pack(side=RIGHT, fill=Y)
        canvasVorhanden.pack(side=LEFT, fill=BOTH, expand=True)

        scroll_frameVorhanden = Frame(canvasVorhanden)
        canvasVorhanden.create_window((0, 0), window=scroll_frameVorhanden, anchor='nw')
        scroll_frameVorhanden.bind("<Configure>", lambda e: canvasVorhanden.configure(scrollregion=canvasVorhanden.bbox("all")))
        #enable_mousewheel(canvasVorhanden, scroll_frameVorhanden)

        aktualisiereFenster()

    # Fenster 3 - Fahrer hinzufügen
    elif varweiter == 2:

        # Scroll-Struktur zerstören
        frame_canvas.destroy()
        frame_canvasVorhanden.destroy()
        radio.clear()

        if prüfung == 0:
            labelTitelErstellen.config(text="Erstellen einer Meisterschaft - Fahrer hinzufügen")
        else:
            labelTitelErstellen.config(text="Bearbeiten einer Meisterschaft - Fahrer hinzufügen")

        # Neue Scrollbare Struktur
        frame_canvas = Frame(fensterErstellen)
        frame_canvas.pack(fill=BOTH, expand=True, side=LEFT)

        canvas = Canvas(frame_canvas)
        scrollbar = Scrollbar(frame_canvas, orient=VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scroll_frame = Frame(canvas)
        canvas.create_window((0, 0), window=scroll_frame, anchor='nw')
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        #enable_mousewheel(canvas, scroll_frame)

        listeFahrer = os.listdir('Datenbank/Fahrer')
        fahrer = StringVar()

        for i in range(len(listeFahrer)):
            textFahrer = listeFahrer[i].replace('.dat', '')
            radioFahrer = Radiobutton(master=scroll_frame, text=f"{textFahrer}", value=textFahrer, variable=fahrer)
            radioFahrer.pack(anchor='w')
            radio.append(radioFahrer)

        if listeFahrer:
            fahrer.set(listeFahrer[-1])

        buttonhinzufügen.config(text="Fahrer hinzufügen")
        buttonneuehinzufügen.config(text="neuen Fahrer erstellen")
        buttonentfernen.config(text="Hinzugefügter Fahrer entfernen")

        #Scrollbare Frame-Struktur erstellen
        frame_canvasVorhanden = Frame(fensterErstellen)
        frame_canvasVorhanden.pack(fill=BOTH, expand=True, side=LEFT)

        canvasVorhanden = Canvas(frame_canvasVorhanden)
        scrollbarVorhanden = Scrollbar(frame_canvasVorhanden, orient=VERTICAL, command=canvasVorhanden.yview)
        canvasVorhanden.configure(yscrollcommand=scrollbarVorhanden.set)

        scrollbarVorhanden.pack(side=RIGHT, fill=Y)
        canvasVorhanden.pack(side=LEFT, fill=BOTH, expand=True)

        scroll_frameVorhanden = Frame(canvasVorhanden)
        canvasVorhanden.create_window((0, 0), window=scroll_frameVorhanden, anchor='nw')
        scroll_frameVorhanden.bind("<Configure>", lambda e: canvasVorhanden.configure(scrollregion=canvasVorhanden.bbox("all")))
        #enable_mousewheel(canvasVorhanden, scroll_frameVorhanden)

        aktualisiereFenster()

    # Fenster 4 - Fertig
    elif varweiter == 3:

        frame_canvas.destroy()
        frame_canvasVorhanden.destroy()
        radio.clear()

        #alle Daten sammeln und speichern

        #pfade erstellen
        if prüfung == 1:
            meisterschaftspfad = meisterschaftspfad.replace(".dat", "")
            meisterschaftspfad = meisterschaftspfad.replace("Datenbank/", "")
        meisterschaftsname = meisterschaftspfad
        meisterschaftspfad = 'Datenbank/' + str(meisterschaftsname) + '.dat'
        streckenpfad = 'Datenbank/' + str(meisterschaftsname) + 'Strecken' + '.dat'
        fahrerpfad = 'Datenbank/' + str(meisterschaftsname) + 'Fahrer' + '.dat'

        rennkalenderS = []
        #Strecken als Pfad: jedes Element als Pfad speichern
        for strecke in rennkalender:
            strecke = 'Datenbank/Strecken/' + strecke + '.dat'
            rennkalenderS.append(strecke)

        #Strecken werden gespeichert
        Daten.schreiben(streckenpfad, rennkalender)
        #fahrer als pfad

        fahrerlisteS = []
        #Fahrer als Pfad: jedes Element als Pfad speichern
        for pilot in fahrerliste:
            pilot = 'Datenbank/Fahrer/' + str(pilot) + '.dat'
            fahrerlisteS.append(pilot)

        #Fahrer werden gespeichert
        Daten.schreiben(fahrerpfad, fahrerliste)

        #Meisterschaft wird gespeichert
        Daten.schreiben(meisterschaftspfad, [streckenpfad, fahrerpfad])

        #Fertig
        fensterErstellenFertig = Toplevel()
        fensterErstellenFertig.title("Fertig - Mebe V2.0.0")
        fensterErstellenFertig.geometry("200x300")

        labelTitelErstellenFertig = Label(master=fensterErstellenFertig,
                           text="Erstellt!",
                           font=('', 15))
        labelTitelErstellenFertig.pack()

        time.sleep(2)

        varweiter = 0

        fensterErstellenFertig.destroy()

        fensterErstellen.destroy()


def erstellen():
    global entryNameeinfügen, labelNameeinfügen, labelJahreinfügen, entryJahreinfügen, labelTitelErstellen, fensterErstellen
    global buttonhinzufügen, buttonneuehinzufügen, buttonentfernen, varweiter, meisterschaftspfad, rennkalender, fahrerliste, fahrerliste, radio, radioAnzeigeListe

    #weiter 0...Pflichtdaten; weiter 1...Strecken; weiter 2...Fahrer
    varweiter = 0

    if prüfung == 0:
        meisterschaftspfad = ""
    rennkalender = []
    fahrerliste = []

    #alle Radiobuttons, damit sie hinterher auch gelöscht werden können
    radio = [] #aus Auswahl
    radioAnzeigeListe = [] #aus Anzeige

    #Fenster
    fensterErstellen = Toplevel()
    fensterErstellen.title("Erstellen - Mebe V2.0.0")
    fensterErstellen.geometry("800x600")

    labelTitelErstellen = Label(master=fensterErstellen,
                    text="Erstellen einer Meisterschaft",
                    font=('', 15))
    labelTitelErstellen.pack()

    #Entries ----------
    # Name der Meisterschaft

    labelNameeinfügen = Label(master = fensterErstellen,
                            text = "Name der Meisterschaft")
    #labelSerieeinfügen = Label(master = fensterErstellen,
    #                          text = "Serie der Meisterschaft")
    labelJahreinfügen = Label(master = fensterErstellen,
                            text = "Jahr der Meisterschaft")

    entryNameeinfügen = Entry(master = fensterErstellen)
    #entrySerieeinfügen = Entry(master = fensterErstellen)
    entryJahreinfügen = Entry(master = fensterErstellen)

    # Buttons ----------

    #fügt alle ausgewählten Strecken/Fahrer ein
    buttonhinzufügen = Button(master=fensterErstellen,
                        text="Strecken hinzufügen",
                        command=hinzufügen)

    # Rennkalender / Strecken/Fahrer hinzufügen
    buttonneuehinzufügen = Button(master=fensterErstellen,
                        text="neue Strecke erstellen",
                        command=neuehinzufügen)
    
    buttonentfernen = Button(master=fensterErstellen,
                        text="Hinzugefügte Strecke entfernen",
                        command=entfernen)

    # Fertig - wechselt zu Fahrer bzw. wieder ins Hauptmenü (Switch)
    buttonWeiter = Button(master=fensterErstellen,
                        text="Weiter",
                        command=weiter)

    # MAIN ----------

    labelNameeinfügen.pack()
    entryNameeinfügen.pack()

    #labelSerieeinfügen.pack()
    #entrySerieeinfügen.pack()

    labelJahreinfügen.pack()
    entryJahreinfügen.pack()

    buttonWeiter.pack()

    #Auswahl der Meisterschaft
    #zugehöriges Laden des Rennkalenders und der Fahrer mittels verlinkter Pfade
    #überschreiben von Rennkalender und Fahrer und zack in Erstellen-Modus

def bearbeitenStarten():
    global labelTitelErstellen
    global fensterErstellenBearbeitenAuswahl
    global fahrerliste, rennkalender
    global labelNameeinfügen
    global entryNameeinfügen
    global meisterschaftspfad

    meisterschaftsname = meisterschaft.get() #speichert Auswahl

    fensterErstellenBearbeitenAuswahl.destroy() #löscht das Fenster

    #verarbeitet die Auswahl
    meisterschaftspfad = "Datenbank/" + meisterschaftsname + ".dat"

    meisterschaftsdaten = []
    meisterschaftsdaten = Daten.lesen(meisterschaftspfad)

    erstellen() #Widgets werden erstellt

    #Widgets werden angepasst

    labelTitelErstellen.config(text="Bearbeite Meisterschaft")
    labelTitelErstellen.update_idletasks()

    fensterErstellen.title("Bearbeite Meisterschaft - Mebe V2.0.0")
    fensterErstellen.update_idletasks()

    labelNameeinfügen.destroy()
    entryNameeinfügen.destroy() #Name soll nicht änderbar sein

    #sollte irgendwann das Jahr noch mit dazu gespeichert werden, folgende Zeile auskommentieren (springt einmal vor)
    weiter()

    #Listen überschreiben
    rennkalender = Daten.lesen(meisterschaftsdaten[0])
    #Pfade noch entpacken:
    for i in range(len(rennkalender)):
        streckenelement = str(rennkalender[i])
        rennkalender[i] = streckenelement.replace('Datenbank/Strecken/', '')

    fahrerliste = Daten.lesen(meisterschaftsdaten[1])
    #Pfade noch entpacken:
    for i in range(len(fahrerliste)):
        fahrerelement = str(fahrerliste[i])
        fahrerliste[i] = fahrerelement.replace('Datenbank/Fahrer/', '')

    aktualisiereFenster()
    fensterErstellen.update_idletasks()

def bearbeiten():
    global fensterErstellenBearbeitenAuswahl, labelTitelErstellen
    global meisterschaft
    global prüfung

    prüfung += 1

    #Auswahl der Strecke
    fensterErstellenBearbeitenAuswahl = Toplevel()
    fensterErstellenBearbeitenAuswahl.title("Bearbeite Meisterschaft - Mebe V2.0.0")
    fensterErstellenBearbeitenAuswahl.geometry("800x600")

    labelTitelErstellen = Label(master=fensterErstellenBearbeitenAuswahl,
                                        text="Bearbeite Meisterschaft",
                                        font=('', 15))
    labelTitelErstellen.pack()

    buttonauswahl = Button(fensterErstellenBearbeitenAuswahl, text = "Meisterschaft bearbeiten", command = bearbeitenStarten)
    buttonauswahl.pack()

    #Auswahl der Meisterschaft

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

        radiobuttonMeisterschaft = Radiobutton(master=fensterErstellenBearbeitenAuswahl, text=f"{anzeige}", 
                                               value=anzeige, variable = meisterschaft)
        radiobuttonMeisterschaft.pack()

    meisterschaft.set(VerzeichnisMeisterschaften[0])