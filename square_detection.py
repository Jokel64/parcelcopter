import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#    _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
    threshold= cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx)==4 and cv2.contourArea(cnt)>=400:
            cv2.drawContours(frame, [approx], 0, (0), 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            cv2.putText(frame, "Rectangle", (x, y), font, 1, (0))



    cv2.imshow("shapes", frame)
    cv2.imshow("Threshold", threshold)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()