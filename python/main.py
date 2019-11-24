from modules.Controller import *
from modules.PiSen import *
from modules.GUI import *
from modules.ConfigMan import *
from modules.DataModel import *
import modules.DataModel
from modules.DataRes import *
from modules.ArrayOp import *
from modules.SquarePos import *


import logging
import threading
import time

config = ConfigMan().getConfig()
data = DataModel()

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

logging.info("Main    : Programm start")
data.setCurrentPosition([0,0,0])
gui = GUI(1, "Thread-1", config, data)
gui.start()

datares = DataRes(1, "Thread-2", data)
datares.start()

cam = SquarePos(2, "cam", config, data)
con = Controller(2, "con", config, data)
#Status:
    #0. warte
    #2. steige auf
    #3 fliege zu koordinaten
    #4 Bilderkennung
    #5 sinke
    #6 greifen paket
    #7 steige
    #8 fliege zu ziel
    #9 sinke
    #10 greifer auf
    #11 steige
    #12 fliege zu nullpunkt
    #13 sinke

while data.getRunning():
    if data.getstate() == 0:
        if data.getResivedCoordinates() == True:
            data.setstate(1)
            logging.info("Main    : aufsteigen")
            data.setnextCoordinates(ArrayOp.addarreays(data.getCurrentPosition(), [0,0,2]))
            con.start()

    if data.getstate() == 1:
        if norm(ArrayOp.subarreays(data.getCurrentPosition(), data.getnextCoordinates())) <= 0.1:
            logging.info("Main    : fliege zu Paketpositon")
            data.setstate(2)
            data.setnextCoordinates(ArrayOp.addarreays(data.getParcelPosition(), [0, 0, 2]))



    if data.getstate() == 2:
        if norm(ArrayOp.subarreays(data.getCurrentPosition(), data.getnextCoordinates())) <= 0.1:
            logging.info("Main    : Suche paket")
            data.setstate(3)
            data.setnextCoordinates([0,0,0])
            cam.start()

    if data.getstate() == 3:
        if norm(ArrayOp.subarreays(data.getCurrentPosition(), data.getnextCoordinates())) <= 0.1:
            logging.info("Main    : sinke")
            data.setexitcam(True)
            cam.join()
            data.setstate(4)
            data.setnextCoordinates([data.getnextCoordinates()[0], data.getnextCoordinates()[1], 0])


    if data.getstate() == 4:
        if norm(ArrayOp.subarreays(data.getCurrentPosition(), data.getnextCoordinates())) <= 0.1:
            logging.info("Main    : Schließe Greifer")
            data.setstate(5)
            data.setclosegrap(True)

    if data.getstate() == 5:
        if data.getgrapclosed():
            logging.info("Main    : steige")
            data.setnextCoordinates([data.getnextCoordinates()[0], data.getnextCoordinates()[1], 2])
            data.setstate(6)

    if data.getstate() == 6:
        if norm(ArrayOp.subarreays(data.getCurrentPosition(), data.getnextCoordinates())) <= 0.1:
            logging.info("Main    : Fliege zu Ziel koordinaten")
            data.setstate(7)
            data.setnextCoordinates(ArrayOp.addarreays(data.getTargetPosition(), [0, 0, 2]))

    if data.getstate() == 7:
        if norm(ArrayOp.subarreays(data.getCurrentPosition(), data.getnextCoordinates())) <= 0.1:
            logging.info("Main    : Sinke")
            data.setstate(8)
            data.setnextCoordinates([data.getnextCoordinates()[0], data.getnextCoordinates()[1], 0])

    if data.getstate() == 8:
        if norm(ArrayOp.subarreays(data.getCurrentPosition(), data.getnextCoordinates())) <= 0.1:
            logging.info("Main    : open grap")
            data.setstate(9)
            data.setclosegrap(False)

    if data.getstate() == 9:
        if not data.getgrapclosed():
            logging.info("Main    : steige")
            data.setnextCoordinates([data.getnextCoordinates()[0], data.getnextCoordinates()[1], 2])
            data.setstate(10)

    if data.getstate() == 10:
        if norm(ArrayOp.subarreays(data.getCurrentPosition(), data.getnextCoordinates())) <= 0.1:
            logging.info("Main    : Fliege zu ausgangsposition")
            data.setnextCoordinates([0,0,2])
            data.setstate(11)

    if data.getstate() == 11:
        if norm(ArrayOp.subarreays(data.getCurrentPosition(), data.getnextCoordinates())) <= 0.1:
            logging.info("Main     : sinke")
            data.setnextCoordinates([0, 0, 0])
            data.setstate(12)

    if data.getstate() == 12:
        if norm(ArrayOp.subarreays(data.getCurrentPosition(), data.getnextCoordinates())) <= 0.1:
            logging.info("Main    : all Done")
            data.setRunning(False)



