
from imutils.video import VideoStream
from pyzbar import pyzbar
import datetime
import imutils
import time
import cv2


vs = VideoStream(src=0).start()
time.sleep(2.0)
found = set()

# loop over the frames from the video stream
while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=720)
	barcodes = pyzbar.decode(frame) #for finding qrcode or barcode

	for barcode in barcodes:
		
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

		
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type

		
		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
 
	
	if key == ord("q"):
		break


cv2.destroyAllWindows()
vs.stop()