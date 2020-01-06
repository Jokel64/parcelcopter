import logging
import time
import threading
from modules.DataModel import *
from numpy.linalg import norm
from modules.ArrayOp import *

class Controller(threading.Thread):
    def __init__(self, threadID, name, config, Data):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.config = config
        self.speed = [0, 0, 0]
        self.flightaltitude = config["flightaltitude"]
        self.DataModel = Data
        self.exit = False
    def run(self):
        logging.info("Controller    : Controler Runns")
        while self.DataModel.getRunning():
            self.Regler(self.DataModel)
            i = 0
            time.sleep(1)
            currentposition = self.DataModel.getCurrentPosition()
            while i < 3:
                currentposition[i] = self.DataModel.getCurrentPosition()[i] - self.speed[i]
                i = i + 1
            self.DataModel.setCurrentPosition(currentposition)

            if self.DataModel.getclosegrap() == True and self.DataModel.getgrapclosed() == False:
                logging.info("Controller    : Grap closed")
                self.DataModel.setgrapclosed(True)

            if self.DataModel.getclosegrap() == False and self.DataModel.getgrapclosed() == True:
                logging.info("Controller    : Grap open")
                self.DataModel.setgrapclosed(False)

    def Regler(self, DataModel):
        i = 0
        self.OnCoordinates = True
        while i < 3:
            self.speed[i] = (DataModel.getCurrentPosition()[i] - DataModel.getnextCoordinates()[i])/20
            i = i+1
            DataModel.setCurrentSpeed = self.speed
        print(norm(ArrayOp.subarreays(DataModel.getCurrentPosition(), DataModel.getnextCoordinates())))
