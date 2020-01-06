import logging
import time
import threading
from modules.DataModel import *

class DataRes(threading.Thread):
    def __init__(self, threadID, name, Data):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.DataModel = Data
        logging.info("DataRes    : Resiver Runs")

    def run(self):
        while self.DataModel.getRunning():
            if not self.DataModel.getResivedCoordinates():
                self.checkCoordinates()

    def checkCoordinates(self):
        if not (self.DataModel.getParcelPosition() == [0,0,0] and self.DataModel.getTargetPosition() == [0,0,0]):
            logging.info("DataRes    : Resived Coordinates")
            self.DataModel.setResivedCoordinates(True)
