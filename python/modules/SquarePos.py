import PiCam
import cv2
import ConfigMan
from ConfigMan import ConfigMan


class SquarePos:
    # class to handle the different position and sort them out

    def __init__(self):
        self.cam = PiCam.PiCam()
        while True:
            self.cam.PosSquares()
            print(self.cam.getPos())
            #if drone moves left square have to gio right. Square can't jump etc


            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.cam.destroy()
                config = ConfigMan().saveConf()
                break

