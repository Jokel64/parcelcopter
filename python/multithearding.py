import cv2
import logging
import threading
import time
import numpy as np
import tkinter

from tkinter import *
from PIL import ImageTk, Image

variables = {}
Anzahl = 0

def gui(name):
    def button_action():
        if not (SchwarzWeiss.get() == ""):
            variables["schwarzweißfilter"]) = int(SchwarzWeiss.get())
            SchwarzweissText = Label(fenster, text="SchwarzWeissfilter: " + str(variables["schwarzweißfilter"])))
            SchwarzweissText.place(x=0, y=0, width=200, height=30)
        if not (mindestgroesse.get() == ""):
            global min
            variables["min_Groesse"] = int(mindestgroesse.get())
            mindestgroesseText = Label(fenster, text="Mindestgroesse: " + str(variables["min_Groesse"]))
            mindestgroesseText.place(x=0, y=30, width=200, height=30)
        if not (maximalgroesse.get() == ""):
            variables["max_Groesse"] = int(maximalgroesse.get())
            maximalgroesseText = Label(fenster, text="Maximalgroesse: " + str(variables["max_Groesse"]))
            maximalgroesseText.place(x=0, y=60, width=200, height=30)

    def button_ende():
        cap.release()
        cv2.destroyAllWindows()
        global LOOP_ACTIVE
        LOOP_ACTIVE = false
        fenster.quit

    fenster = Tk()
    # Den Fenstertitle erstellen
    fenster.title("Benutzeroberfläche")
    fenster.geometry("300x600")

    SchwarzWeiss = Entry(fenster, bd=5, width=40)
    SchwarzweissText = Label(fenster, text="SchwarzWeissfilter: " + str(variables["schwarzweißfilter"]))
    mindestgroesse = Entry(fenster, bd=5, width=40)
    maximalgroesse = Entry(fenster, bd=5, width=40)
    maximalgroesseText = Label(fenster, text="Maximalgroesse: " + str(variables["max_Groesse"]))

    change_button = Button(fenster, text="Ändern", command=button_action)
    exit_button = Button(fenster, text="Beenden", command=button_ende)
    Anzahl = Label(fenster, text="Anzahl erkannter Vierecke " + str(Anzahl))

    mindestgroesseText = Label(fenster, text="Mindestgroesse: " + str(variables["min_Groesse"]))
    SchwarzWeiss.place(x=200, y=0, width=100, height=30)
    SchwarzweissText.place(x=0, y=0, width=200, height=30)
    mindestgroesse.place(x=200, y=30, width=100, height=30)
    mindestgroesseText.place(x=0, y=30, width=200, height=30)
    change_button.place(x=0, y=500, width=300, height=50)
    exit_button.place(x=0, y=550, width=300, height=50)
    Anzahl.place(x=0, y=200, width=300, height=30)
    maximalgroesse.place(x=200, y=60, width=100, height=30)
    maximalgroesseText.place(x=0, y=60, width=200, height=30)

    LOOP_ACTIVE = True
    while LOOP_ACTIVE:

def starten(name):
    f = open('variables.txt', 'r+')
    lines = f.read().splitlines()
    f.close()
    i = 0
    while i < len(lines):
        if '[' not in lines[i + 1]:
            variables.update({lines[i]: int(lines[i + 1])})
        else:
            lines[i + 1] = lines[i + 1].replace("[", "")
            lines[i + 1] = lines[i + 1].replace("]", "")
            liste = lines[i + 1].split(", ")
            list = []
            for eintrag in liste:
                list.append(int(eintrag))
            variables.update({lines[i]: np.asarray(list)})
        i = i + 2
    logging.info("Thread %s: Variablen initialisiert", name)

def warten(name):
    logging.info("Thread %s: starting", name)
    empfangen = False

    while not empfangen:
        empfangen = True
        logging.info("Thread %s: warten", name)

    logging.info("Thread %s: GPS Signale Empfangen", name)


def aufsteigen(name):
   logging.info("Thread %s: starting", name)

    # motoren an
    # h_akt = 0 # in Metern
    # if(h_akt = h_soll)

def GoTo_coordinates(name):
    logging.info("Thread %s: Fliege zu Koordinaten", name)

def Finde_paket(name):
    logging.info("Fliege zu Paket...", name)


def Sinken(name):
    looging.info("Gelandet", name)

def Greifer_zu(name):
    looging.info("Greifer geschlossen", name)

def Greifer_auf(name):
    looging.info("Greifer offen", name)


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

logging.info("Main    : Programm starten")
interface = threading.Thread(target=gui, args=('gui',))
interface.start()
x = threading.Thread(target=starten, args=('starten',))
x.start()
x.join()
x = threading.Thread(target=warten, args=('warten',))
x.start()
x.join()
logging.info("Main    : all done")


