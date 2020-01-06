# USAGE
# python.old webstreaming.py --ip 0.0.0.0 --port 8000

# import the necessary packages
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2
import numpy as np



minSize = 100
maxSize = 100000

font = cv2.FONT_HERSHEY_COMPLEX


# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful for multiple browsers/tabs
# are viewing tthe stream)
outputFrame = None
lock = threading.Lock()

# initialize a flask object
app = Flask(__name__)

# initialize the video stream and allow the camera sensor to
# warmup
#vs = VideoStream(usePiCamera=1).start()
vs = VideoStream(src=0).start()
time.sleep(2.0)

@app.route("/")
def index():
	# return the rendered template
	return render_template("index.html")

def detect_motion(frameCount):
	# grab global references to the video stream, output frame, and
	# lock variables
	global vs, outputFrame, lock

	# initialize the motion detector and the total number of frames
	# read thus far
	
	# loop over frames from the video stream
	while True:
		# read the next frame from the video stream, resize it,
		# convert the frame to grayscale, and blur it
		frame = vs.read()
		frame = imutils.resize(frame, width=400)
		
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		hsv_inrange = cv2.inRange(hsv, np.array([159, 87, 149]), np.array([179, 224, 255]))
    
		# if the total number of frames has reached a sufficient
		# number to construct a reasonable background model, then
		# continue to process the frame
		
		contours, _ = cv2.findContours(hsv_inrange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		Anzahl = 0
		list = []
		#list [xkooordinate mittelpunkt, ykoordinate mittelpunkt, drehung]
		#drehung zwischen 0 und 45 0 waagerecht
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
		
		

		# acquire the lock, set the output frame, and release the
		# lock
		with lock:
			outputFrame = frame.copy()
		
def generate():
	# grab global references to the output frame and lock variables
	global outputFrame, lock

	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if outputFrame is None:
				continue

			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

			# ensure the frame was successfully encoded
			if not flag:
				continue

		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

# check to see if this is the main thread of execution
if __name__ == '__main__':
	# construct the argument parser and parse command line arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--ip", type=str, required=True,
		help="ip address of the device")
	ap.add_argument("-o", "--port", type=int, required=True,
		help="ephemeral port number of the server (1024 to 65535)")
	ap.add_argument("-f", "--frame-count", type=int, default=32,
		help="# of frames used to construct the background model")
	args = vars(ap.parse_args())

	# start a thread that will perform motion detection
	t = threading.Thread(target=detect_motion, args=(
		args["frame_count"],))
	t.daemon = True
	t.start()

	# start the flask app
	app.run(host=args["ip"], port=args["port"], debug=True,
		threaded=True, use_reloader=False)

# release the video stream pointer
vs.stop()