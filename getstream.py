import numpy as np
import cv2
type = 0
#0...orginal, 1...grau
def draw_lines(img, lines, color=[255, 0, 0], thickness=10):
    # If there are no lines to draw, exit.
    if lines is None:
        return img

    img = np.copy(img)
    # Create a blank image that matches the original in size.
    line_img = np.zeros(
        (
            img.shape[0],
            img.shape[1],
            3
        ),
        dtype=np.uint8,
    )
    # Loop over all lines and draw them on the blank image.
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)
    # Merge the image with the lines onto the original.
    img = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)
    # Return the modified image.
    return img

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    img = frame# Our operations on the frame come here
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    lines = cv2.HoughLinesP(edges, rho=6,theta=np.pi / 30, threshold=400,  lines=np.array([]), minLineLength=50, maxLineGap=50)

    print(lines)

    both = draw_lines(img,lines)
    cv2.imshow('grau', gray)
    cv2.imshow('edges',both)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
