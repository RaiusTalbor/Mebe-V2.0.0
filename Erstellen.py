# Motorsportmeisterschaftsberechner
# Mebe V2.0.0
# Untermenü erstellen - ermöglicht das Erstellen einer komplett neuen Meisterschaft

import time
from tkinter import *
import Daten        #Lesen, Schreiben von Dateien
import ErstelleStrecke
import ErstelleFahrer
import os

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
    target_canvas.bind("<Enter>", lambda e: target_canvas.bind_all("<MouseWheel>", on_mousewheel))
    target_canvas.bind("<Leave>", lambda e: target_canvas.unbind_all("<MouseWheel>"))

    target_canvas.bind("<Enter>", lambda e: [target_canvas.bind_all("<Button-4>", on_mousewheel),
                                             target_canvas.bind_all("<Button-5>", on_mousewheel)])
    target_canvas.bind("<Leave>", lambda e: [target_canvas.unbind_all("<Button-4>"),
                                             target_canvas.unbind_all("<Button-5>")])

def aktualisiereFenster():
    #Canvas soll die Elemente in der Liste anzeigen, mit aktualisiere die aktuelle Liste

    for i in range(len(radioAnzeigeListe)):
        radioAnzeigeListe[i].destroy()

    schleifenliste = []

    if varweiter == 1:
        schleifenliste = rennkalender

    if varweiter == 2:
        schleifenliste = fahrerliste

    vorhanden = StringVar()
    for i in range (len(schleifenliste)):
        radioAnzeigeVorhanden = Radiobutton(master=scroll_frameVorhanden, text=f"{schleifenliste[i]}", value=schleifenliste[i], variable=vorhanden)
        radioAnzeigeVorhanden.pack(anchor='w')
        radioAnzeigeListe.append(radioAnzeigeVorhanden)

    #Mechanik zur Auswahl

#fügt Radiobutton-Auswahl hinzu
def hinzufügen():

    global varweiter
    global Fahrer       #Radiobuttons
    global strecken     #Radiobuttons
    global rennkalender
    global fahrerliste

    #holt sich die Daten und speichert sie zwischen
    if varweiter == 1:
        rennkalender.append(strecken.get())
    
    if varweiter == 2:
        fahrerliste.append(Fahrer.get())

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
        pfad = "Datenbank/Strecken" + ErstelleStrecke.streckenname + ".dat"

        rennkalender.append(pfad)

    if varweiter == 2:
        #füge nun die Auswahl hinzu
        ErstelleFahrer.FahrerErstellen()

        fensterErstellen.wait_window(ErstelleFahrer.fensterErstellenFahrer)

        #Pfad noch zusammenbauen
        pfad = "Datenbank/Fahrer" + ErstelleFahrer.Fahrername + ".dat"

        fahrerliste.append(pfad)

    aktualisiereFenster()

#zeigt jeweils das neue Fenster mit den neuen Einstellungen an
def weiter():
    global varweiter
    global textStrecke
    global textFahrer
    global meisterschaftspfad
    global strecken
    global Fahrer
    global radio
    global entryNameeinfügen, labelNameeinfügen, labelJahreinfügen, entryJahreinfügen, labelTitelErstellen, fensterErstellen
    global buttonhinzufügen, buttonneuehinzufügen, rennkalender, fahrerliste

    #Der Cntainer, in dem sich die Radios befinden
    global canvas, scroll_frame, scrollbar, frame_canvas, frame_canvasVorhanden, scroll_frameVorhanden

    varweiter += 1

    # Fenster 2 - Strecken hinzufügen
    if varweiter == 1:

        #Meisterschaftsdatei anlegen
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
        enable_mousewheel(canvas, scroll_frame)

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
        enable_mousewheel(canvasVorhanden, scroll_frameVorhanden)

    # Fenster 3 - Fahrer hinzufügen
    elif varweiter == 2:

        # Scroll-Struktur zerstören
        frame_canvas.destroy()
        frame_canvasVorhanden.destroy()
        radio.clear()

        labelTitelErstellen.config(text="Erstellen einer Meisterschaft - Fahrer hinzufügen")

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
        enable_mousewheel(canvas, scroll_frame)

        listeFahrer = os.listdir('Datenbank/Fahrer')
        Fahrer = StringVar()

        for i in range(len(listeFahrer)):
            textFahrer = listeFahrer[i].replace('.dat', '')
            radioFahrer = Radiobutton(master=scroll_frame, text=f"{textFahrer}", value=textFahrer, variable=Fahrer)
            radioFahrer.pack(anchor='w')
            radio.append(radioFahrer)

        if listeFahrer:
            Fahrer.set(listeFahrer[-1])

        buttonhinzufügen.config(text="Fahrer hinzufügen")
        buttonneuehinzufügen.config(text="neuen Fahrer erstellen")

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
        enable_mousewheel(canvasVorhanden, scroll_frameVorhanden)

    # Fenster 4 - Fertig
    elif varweiter == 3:

        frame_canvas.destroy()
        frame_canvasVorhanden.destroy()
        radio.clear()

        #alle Daten sammeln und speichern

        #pfade erstellen
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
    global buttonhinzufügen, buttonneuehinzufügen, varweiter, meisterschaftspfad, rennkalender, fahrerliste, fahrerliste, radio, radioAnzeigeListe

    #weiter 0...Pflichtdaten; weiter 1...Strecken; weiter 2...Fahrer
    varweiter = 0

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