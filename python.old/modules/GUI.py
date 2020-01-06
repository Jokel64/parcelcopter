import numpy as np
import tkinter
import modules.ConfigMan
import time
import logging
import threading


from tkinter import *
from modules.ConfigMan import *
from PIL import ImageTk, Image
from modules.DataModel import *

class GUI(threading.Thread):
    def __init__(self, threadID, name, config, Data):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.config = config
        logging.info("GUI    : GUI initialisiert")
        self.Data = Data
    def run(self):
        def save():
            ConfigMan().saveConf(self.config)

        def test():
            self.config["schwarzweisfilter"] = 10

        def button_action():
            if not ((self.targetposition1.get() == "") and (self.targetposition2.get() == "") and (self.targetposition3.get() == "")):
                self.Data.setTargetPosition([int(self.targetposition1.get()), int(self.targetposition2.get()), int(self.targetposition3.get())])

            if not ((self.parcelposition1.get() == "") and (self.parcelposition2.get() == "") and (self.parcelposition3.get() == "")):
                self.Data.setParcelPosition([int(self.parcelposition1.get()), int(self.parcelposition2.get()), int(self.parcelposition3.get())])


            if not (self.SchwarzWeissWindow.get() == ""):
                self.schwarzweiss = int(self.SchwarzWeissWindow.get())
                self.config["schwarzweisfilter"] = self.schwarzweiss
                self.SchwarzweissText = Label(self.fenster, text="SchwarzWeissfilter: " + str(self.schwarzweiss))
                self.SchwarzweissText.place(x=0, y=0, width=200, height=30)
            if not (self.mindestgroesseWindow.get() == ""):
                self.minSize = int(self.mindestgroesseWindow.get())
                self.config["minSize"] = self.minSize
                self.mindestgroesseText = Label(fenster, text="Mindestgroesse: " + str(self.minSize))
                self.mindestgroesseText.place(x=0, y=30, width=200, height=30)
            if not (self.maximalgroesseWindow.get() == ""):
                self.maxSize = int(self.maximalgroesseWindow.get())
                self.config["maxSize"] = self.maxSize
                self.maximalgroesseText = Label(fenster, text="Maximalgroesse: " + str(self.maxSize))
                self.maximalgroesseText.place(x=0, y=60, width=200, height=30)

        def button_ende():
            self.Data.setRunning(False)
            self.fenster.quit

        logging.info("GUI    : GUI läuft")

        self.minSize = self.config["minSize"]
        self.maxSize = self.config["maxSize"]
        self.schwarzweiss = self.config["schwarzweisfilter"]
        self.fenster = Tk()
        self.fenster.title("Benutzeroberfläche")
        self.fenster.geometry("300x600")

        self.SchwarzWeissWindow = Entry(self.fenster, bd=5, width=40)
        self.SchwarzweissText = Label(self.fenster, text="SchwarzWeissfilter: " + str(self.schwarzweiss))
        self.mindestgroesseWindow = Entry(self.fenster, bd=5, width=40)
        self.maximalgroesseWindow = Entry(self.fenster, bd=5, width=40)
        self.maximalgroesseText = Label(self.fenster, text="Maximalgroesse: " + str(self.maxSize))

        self.targettext = Label(self.fenster, text="Target Position: ")
        self.targetposition1 = Entry(self.fenster, bd=5, width=10)
        self.targetposition2 = Entry(self.fenster, bd=5, width=10)
        self.targetposition3 = Entry(self.fenster, bd=5, width=10)

        self.parceltext = Label(self.fenster, text="Parcel Position: ")
        self.parcelposition1 = Entry(self.fenster, bd=5, width=10)
        self.parcelposition2 = Entry(self.fenster, bd=5, width=10)
        self.parcelposition3 = Entry(self.fenster, bd=5, width=10)

        self.targettext.place(x=0, y=90, width=100, height=30)
        self.targetposition1.place(x=100, y=90, width=50, height=30)
        self.targetposition2.place(x=150, y=90, width=50, height=30)
        self.targetposition3.place(x=200, y=90, width=50, height=30)

        self.parceltext.place(x=0, y=120, width=100, height=30)
        self.parcelposition1.place(x=100, y=120, width=50, height=30)
        self.parcelposition2.place(x=150, y=120, width=50, height=30)
        self.parcelposition3.place(x=200, y=120, width=50, height=30)

        self.save_button = Button(self.fenster, text="Save", command=save)
        self.change_button = Button(self.fenster, text="Ändern", command=button_action)
        self.exit_button = Button(self.fenster, text="Beenden", command=button_ende)
        self.Anzahlfenster = Label(self.fenster, text="Anzahl erkannter Vierecke " + str(self.Data.getRegSquare()))
        self.mindestgroesseText = Label(self.fenster, text="Mindestgroesse: " + str(self.minSize))
        self.CurrentPosition = Label(self.fenster, text="CurrentPosition: [" + str(self.Data.getCurrentPosition()[0]) + ", " + str(self.Data.getCurrentPosition()[1]) + ", " + str(self.Data.getCurrentPosition()[2]))
        self.mindestgroesseText = Label(self.fenster, text="Mindestgroesse: " + str(self.minSize))
        self.SchwarzWeissWindow.place(x=200, y=0, width=100, height=30)
        self.SchwarzweissText.place(x=0, y=0, width=200, height=30)
        self.mindestgroesseWindow.place(x=200, y=30, width=100, height=30)
        self.mindestgroesseText.place(x=0, y=30, width=200, height=30)
        self.save_button.place(x=0, y=450, width=300, height=50)
        self.change_button.place(x=0, y=500, width=300, height=50)
        self.exit_button.place(x=0, y=550, width=300, height=50)
        self.Anzahlfenster.place(x=0, y=200, width=300, height=30)
        self.CurrentPosition.place(x=0, y=250, width=300, height=30)
        self.maximalgroesseWindow.place(x=200, y=60, width=100, height=30)
        self.maximalgroesseText.place(x=0, y=60, width=200, height=30)

        while self.Data.getRunning():
            self.Anzahlfenster = Label(self.fenster, text="Anzahl erkannter Vierecke " + str(self.Data.getRegSquare()))
            self.Anzahlfenster.place(x=0, y=200, width=300, height=30)
            self.CurrentPosition = Label(self.fenster, text="CurrentPosition: [" + str(self.Data.getCurrentPosition()[0]) + ", " + str(self.Data.getCurrentPosition()[1]) + ", " + str(self.Data.getCurrentPosition()[2]))
            self.CurrentPosition.place(x=0, y=250, width=300, height=30)
            self.fenster.update()

        if self.Data.getRunning() == False:
            self.fenster.quit




