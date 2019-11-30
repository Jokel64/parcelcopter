import cv2
import numpy as np
import tkinter

from tkinter import *
from PIL import ImageTk, Image

color = [0,0,0]

thresh = 175
min = 100
Anzahl = 0
max = 100000
def button_action():
    if not(SchwarzWeiss.get() == ""):
        global thresh
        thresh = int(SchwarzWeiss.get())
        SchwarzweissText = Label(fenster, text="SchwarzWeissfilter: " + str(thresh))
        SchwarzweissText.place(x=0, y=0, width=200, height=30)
    if not(mindestgroesse.get() == ""):
        global min
        min = int(mindestgroesse.get())
        mindestgroesseText = Label(fenster, text="Mindestgroesse: " + str(min))
        mindestgroesseText.place(x=0, y=30, width=200, height=30)
    if not (maximalgroesse.get() == ""):
        global max
        max = int(maximalgroesse.get())
        maximalgroesseText = Label(fenster, text="Maximalgroesse: " + str(max))
        maximalgroesseText.place(x = 0, y = 60, width=200, height=30)

def button_ende():
    cap.release()
    cv2.destroyAllWindows()
    global LOOP_ACTIVE
    LOOP_ACTIVE = false
    fenster.quit

cap = cv2.VideoCapture(0)
blackwhite = 0
# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("Benutzeroberfläche")
fenster.geometry("300x600")

SchwarzWeiss = Entry(fenster, bd=5, width=40)
SchwarzweissText = Label(fenster, text="SchwarzWeissfilter: "+ str(thresh))
mindestgroesse = Entry(fenster, bd=5, width=40)
maximalgroesse = Entry(fenster, bd=5, width=40)
maximalgroesseText = Label(fenster, text="Maximalgroesse: "+ str(max))

change_button = Button(fenster, text="Ändern", command=button_action)
exit_button = Button(fenster, text="Beenden", command=button_ende)
Anzahl = Label(fenster, text="Anzahl erkannter Vierecke "+ str(Anzahl))


mindestgroesseText = Label(fenster, text="Mindestgroesse: " + str(min))
SchwarzWeiss.place(x = 200, y = 0, width=100, height=30)
SchwarzweissText.place(x = 0, y = 0, width=200, height=30)
mindestgroesse.place(x = 200, y = 30, width=100, height=30)
mindestgroesseText.place(x = 0, y = 30, width=200, height=30)
change_button.place(x = 0, y = 500, width=300, height=50)
exit_button.place(x = 0, y = 550, width=300, height=50)
Anzahl.place(x = 0, y = 200, width=300, height=30)
maximalgroesse.place(x = 200, y = 60, width=100, height=30)
maximalgroesseText.place(x = 0, y = 60, width=200, height=30)

LOOP_ACTIVE = True
while LOOP_ACTIVE:
    ret, frame = cap.read()

    font = cv2.FONT_HERSHEY_COMPLEX

    lower_red = np.array([100, 180, 150])
    upper_red = np.array([180, 204, 255])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_inrange = cv2.inRange(hsv, [0,115,194], [23,255,255])
    #_, bw = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    #    _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
    #threshold = cv2.adaptiveThreshold(red, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    contours, _ = cv2.findContours(hsv_inrange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    Anzahl = 0
    list = []
    #list [xkooordinate mittelpunkt, ykoordinate mittelpunkt, drehung]
    #drehung zwischen 0 und 45 0 waagerecht
    print('neu')
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4 and cv2.contourArea(cnt) >= minSize and cv2.contourArea(cnt) <= maxSize:
            xmittelpunkt = (approx.ravel()[0] + approx.ravel()[2] + approx.ravel()[4] + approx.ravel()[6]) / 4
            ymittelpunkt = (approx.ravel()[1] + approx.ravel()[3] + approx.ravel()[5] + approx.ravel()[7]) / 4
            dabei = False
            #            checke ob das Viereck schon erkannt wurde
            self.list = []
            for elm in self.list:
            if (xmittelpunkt - elm[0] <= 1 or xmittelpunkt - elm[0] >= 1 or ymittelpunkt - elm[1] <= 1 or ymittelpunkt - elm[1] >= 1):
                dabei = True
            if dabei == False:
                Anzahl = Anzahl + 1

                drehung = np.arctan(
                    (approx.ravel()[3] - approx.ravel()[1]) / (approx.ravel()[2] - approx.ravel()[0]))
                drehung = drehung / np.pi * 180
                cv2.drawContours(frame, [approx], 0, (0), 5)
                list.append([xmittelpunkt, ymittelpunkt, drehung])
                if not xmittelpunkt < 480:
                    xmittelpunkt = 479;
                if not ymittelpunkt < 480:
                    ymittelpunkt = 479;
                color = frame[int(xmittelpunkt), int(ymittelpunkt)]
                cv2.putText(frame, "B:" + str(color[0]) + " G:" + str(color[1]) + " R:" + str(color[2]),
                            (int(xmittelpunkt), int(ymittelpunkt)), font, 1, (0))
                print(list)
    cv2.imshow("red", hsv_inrange)
    cv2.imshow("shapes", frame)
    Anzahl = Label(fenster, text="Anzahl erkannter Vierecke " + str(Anzahl))
    Anzahl.place(x=0, y=200, width=300, height=30)
    fenster.update()


