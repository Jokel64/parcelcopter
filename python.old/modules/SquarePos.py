import modules.PiCam
import cv2
import modules.ConfigMan
import threading
import time

from modules.PiCam import *
from modules.ConfigMan import ConfigMan
from modules.DataModel import *
from modules.ArrayOp import *

class SquarePos(threading.Thread):
    # class to handle the different position and sort them out
    def __init__(self, threadID, name, config, DataModel):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.cam = PiCam(config)
        self.DataModel = DataModel
        self.config = config
        self.name = name

    def run(self):
        while (not self.DataModel.getexitcam()) and self.DataModel.getRunning():
            #self.cam.PosSquares()
            #print(self.cam.getPos())
            #if drone moves left square have to gio right. Square can't jump etc
            self.DataModel.setnextCoordinates(ArrayOp.addarreays(self.DataModel.getParcelPosition(), [0.5, 0.5, 2]))

        self.DataModel.setexitcam(False)
        self.cam.destroy()


