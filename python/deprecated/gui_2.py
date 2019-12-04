import cv2
import numpy as np

minSize = 100
maxSize = 1000000
cap = cv2.VideoCapture(0)

LOOP_ACTIVE = True
while LOOP_ACTIVE:
    ret, frame = cap.read()

    font = cv2.FONT_HERSHEY_COMPLEX

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_inrange = cv2.inRange(hsv, np.array([159, 87, 149]), np.array([179, 224, 255]))
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
        if len(approx) == 4 and cv2.contourArea(cnt) >= minSize:
            xmittelpunkt = (approx.ravel()[0] + approx.ravel()[2] + approx.ravel()[4] + approx.ravel()[6]) / 4
            ymittelpunkt = (approx.ravel()[1] + approx.ravel()[3] + approx.ravel()[5] + approx.ravel()[7]) / 4
            dabei = False
            #            checke ob das Viereck schon erkannt wurde
            list = []
            for elm in list:
                if (xmittelpunkt - elm[0] <= 1 or xmittelpunkt - elm[0] >= 1 or ymittelpunkt - elm[1] <= 1 or ymittelpunkt - elm[1] >= 1):
                    dabei = True
            if dabei == False:
                Anzahl = Anzahl + 1
                drehung = np.arctan((approx.ravel()[3] - approx.ravel()[1]) / (approx.ravel()[2] - approx.ravel()[0]))
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
    #cv2.imshow("frame", frame)
    #cv2.imshow("result", hsv_inrange)

    key = cv2.waitKey(1)
    if key == 27:
        break

