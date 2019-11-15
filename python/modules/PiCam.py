import cv2
import logging
import time
import numpy as np
import ConfigMan

class PiCam:
    def __init__(self):
        self.id = 0
        self.usbConf = cv2.VideoCapture(0)
        config = ConficMan.getDict()
        self.lowerRed = confic["lowerRed"]
        self.upperRed = confic["upperRed"]
        self.minSize = confic["minSize"]
        self.maxSize = confic["maxSize"]

    def PosSquares():
        # Capture frame-by-frame
        ret, frame = usbConf.read()
        font = cv2.FONT_HERSHEY_COMPLEX
        red = cv2.inRange(frame, lowerRed, upperRed)
        cv2.imshow("red", red)
        contours, _ = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        Anzahl = 0
        list = []
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
            if len(approx) == 4 and cv2.contourArea(cnt) >= minSize and cv2.contourArea(cnt) <= maxSize:
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

                    drehung = np.arctan(
                        (approx.ravel()[3] - approx.ravel()[1]) / (approx.ravel()[2] - approx.ravel()[0]))
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
        cv2.imshow("shapes", frame)

    usbConf.release()
    cv2.destroyAllWindows()