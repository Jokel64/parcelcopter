import cv2
import logging
import threading
import time
import numpy as np
import tkinter

from tkinter import *
from PIL import ImageTk, Image

LOOP_ACTIVE = True
variables = {}
Anzahl = 0
def gui(name):
    def speichern():
        f = open('variables.txt', 'w')
        for var in variables:
            f.write(var+"\n")
            f.write(str(variables[var])+"\n")

    def button_action():
        if not (SchwarzWeiss.get() == ""):
            variables["schwarzweißfilter"] = int(SchwarzWeiss.get())
            SchwarzweissText = Label(fenster, text="SchwarzWeissfilter: " + str(variables["schwarzweißfilter"]))
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
        global LOOP_ACTIVE
        LOOP_ACTIVE = False
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

    save_button = Button(fenster, text="Speichern", command=speichern)
    change_button = Button(fenster, text="Ändern", command=button_action)
    exit_button = Button(fenster, text="Beenden", command=button_ende)
    Anzahlfenster = Label(fenster, text="Anzahl erkannter Vierecke " + str(Anzahl))

    mindestgroesseText = Label(fenster, text="Mindestgroesse: " + str(variables["min_Groesse"]))
    SchwarzWeiss.place(x=200, y=0, width=100, height=30)
    SchwarzweissText.place(x=0, y=0, width=200, height=30)
    mindestgroesse.place(x=200, y=30, width=100, height=30)
    mindestgroesseText.place(x=0, y=30, width=200, height=30)
    save_button.place(x=0, y=450, width=300, height=50)
    change_button.place(x=0, y=500, width=300, height=50)
    exit_button.place(x=0, y=550, width=300, height=50)
    Anzahlfenster.place(x=0, y=200, width=300, height=30)
    maximalgroesse.place(x=200, y=60, width=100, height=30)
    maximalgroesseText.place(x=0, y=60, width=200, height=30)
    global LOOP_ACTIVE
    while LOOP_ACTIVE:
        Anzahlfenster = Label(fenster, text="Anzahl erkannter Vierecke " + str(Anzahl))
        Anzahlfenster.place(x=0, y=200, width=300, height=30)
        fenster.update()

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
            liste = lines[i + 1].split(" ")
            list = []
            for eintrag in liste:
                if not eintrag=="":
                    list.append(int(eintrag))
            variables.update({lines[i]: np.asarray(list)})
        i = i + 2
    logging.info("Thread %s: Variablen initialisiert", name)

def warten(name):
    logging.info("Thread %s: starting", name)
    logging.info("Thread %s: warten", name)
    time.sleep(5)
    logging.info("Thread %s: GPS Signale Empfangen", name)


def aufsteigen(name):
   logging.info("Thread %s: starting", name)

    # motoren an
    # h_akt = 0 # in Metern
    # if(h_akt = h_soll)

def GoTo_coordinates(name):
    logging.info("Thread %s: Fliege zu Koordinaten", name)

def Finde_paket(name):
    cap = cv2.VideoCapture(0)
    logging.info("Thread %s: Fliege zu Paket...", name)

    while LOOP_ACTIVE:
        # Capture frame-by-frame
        ret, frame = cap.read()

        font = cv2.FONT_HERSHEY_COMPLEX
        red = cv2.inRange(frame, variables["lower_red"], variables["upper_red"])
        cv2.imshow("red", red)
        contours, _ = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        Anzahl = 0
        list = []
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
            if len(approx) == 4 and cv2.contourArea(cnt) >= variables["min_Groesse"] and cv2.contourArea(cnt) <= variables["max_Groesse"]:
                xmittelpunkt = (approx.ravel()[0] + approx.ravel()[2] + approx.ravel()[4] + approx.ravel()[6]) / 4
                ymittelpunkt = (approx.ravel()[1] + approx.ravel()[3] + approx.ravel()[5] + approx.ravel()[7]) / 4
                dabei = False
                #            checke ob das Viereck schon erkannt wurde
                for elm in list:
                    if (xmittelpunkt - elm[0] <= 1 or xmittelpunkt - elm[0] >= 1 or ymittelpunkt - elm[
                        1] <= 1 or ymittelpunkt - elm[1] >= 1):
                        dabei = True
                if dabei == False:
                    Anzahl = Anzahl + 1

                    drehung = np.arctan((approx.ravel()[3] - approx.ravel()[1]) / (approx.ravel()[2] - approx.ravel()[0]))
                    drehung = drehung / np.pi * 180
                    cv2.drawContours(frame, [approx], 0, (0), 5)
                    list.append([xmittelpunkt, ymittelpunkt, drehung])
                    print(approx.ravel())
                    if not xmittelpunkt < 480:
                        xmittelpunkt = 479;
                    if not ymittelpunkt < 480:
                        ymittelpunkt = 479;
                    color = frame[int(xmittelpunkt), int(ymittelpunkt)]
                    cv2.putText(frame, "B:" + str(color[0]) + " G:" + str(color[1]) + " R:" + str(color[2]),
                                (int(xmittelpunkt), int(ymittelpunkt)), font, 1, (0))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.imshow("shapes", frame)
    cap.release()
    cv2.destroyAllWindows()

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

x = threading.Thread(target=starten, args=('starten',))
x.start()
x.join()

interface = threading.Thread(target=gui, args=('gui',))
interface.start()

x = threading.Thread(target=warten, args=('warten',))
x.start()
x.join()

x = threading.Thread(target=Finde_paket, args=('Finde_Paket',))
x.start()



interface.join()
logging.info("Main    : all done")


