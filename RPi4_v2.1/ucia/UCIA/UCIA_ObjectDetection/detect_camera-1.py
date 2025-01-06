##########################################################################
# Program inspired from 
# https://docs.ultralytics.com/fr/guides/raspberry-pi/#inference-with-camera
#   
# Modified by Jean-Luc CHARLES (Jean-Luc.Charles@mailo.com)
# 
#   2024/12/16 - v1.1
#
##########################################################################

import cv2
from picamera2 import Picamera2

from ultralytics import YOLO

def do_infer(yolo_trained, confidence=0.6, maxdetect=6):
	''' 
		Make YOLO inferences with the given weights binary file
	'''
	
	# Initialize the Picamera2
	picam2 = Picamera2()
	picam2.preview_configuration.main.size = (640, 640)
	picam2.preview_configuration.main.format = "RGB888"
	picam2.preview_configuration.align()
	picam2.configure("preview")
	picam2.start()

	# Load the YOLO11 model
	model = YOLO(yolo_trained, task='detect')

	while True:

		# Capture frame-by-frame
		#frame = picam2.capture_array()
		img = picam2.capture_image()
		img = img.resize((640, 640))
		img_g  = img.convert("L")
		
		# Run YOLO inference on the frame
		results = model.predict(img_g, imgsz=640, classes=[0,1,2], conf=confidence, max_det=maxdetect)

		# Visualize the results on the frame
		annotated_frame = results[0].plot()

		# Display the resulting frame
		cv2.imshow(str(yolo_trained), annotated_frame)

		# Break the loop if 'q' is pressed
		if cv2.waitKey(1) == ord("q"):
			break

# Release resources and close windows
cv2.destroyAllWindows()

if __name__ == '__main__':
	
	from pathlib import Path
	import argparse, sys

	# Set options to configure program execution:
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '--version', action="store", dest='version', 
		required=False, default='V2', help="'V1' ou 'V2'")
	parser.add_argument('-y', '--yolo', action="store", dest='yolo_ver', 
		required=False, default='v8n', help="v8n, v8s, 11n ou 11s")
	parser.add_argument('-b', '--batch', action="store", dest='batch', 
		required=False, type=int, default='4', help="2, 4, 8, 16, ou 32")
	parser.add_argument('-e', '--epochs', action="store", dest='epochs', 
		required=False, type=int, default='100', help="20, 40, 60, 80 ou 100")
	parser.add_argument('-m', '--maxdetect', action="store", dest='maxdetect', 
		required=False, type=int, default='6', help="Nombre max d'objets à détecter.")
	parser.add_argument('-c', '--confidence', action="store", dest='conf', 
		required=False, type=float, default='0.6', help="Seuil de confiance pour afficher une détection.")
	
	args = parser.parse_args()
	version   = args.version
	yolo_ver  = args.yolo_ver
	batch     = args.batch
	epochs    = args.epochs
	maxdetect = args.maxdetect
	conf      = args.conf
	
	yolo_weights_path  = f'YOLO-trained-{version}/UCIA-YOLO{yolo_ver}/'
	yolo_weights_path += f'batch-{batch:02d}_epo-{epochs:03d}/weights/best_ncnn_model'
	rep = input(f'Utiliser le réseau {yolo_weights_path} [Oui]/Non ? ')

	if rep.lower() in ('', 'o', 'oui', 'y', 'yes'):
		yolo_weights = Path(yolo_weights_path)
		if not yolo_weights.exists():
			print(f'fichier inexitant: <{yolo_weights}>, désolé.')
		else:
			do_infer(yolo_weights, conf, maxdetect)
	
