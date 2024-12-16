######################################
#   Jean-Luc.Charles@mailo.com
#   2024/12/16 - v1.1
######################################

import cv2
from picamera2 import Picamera2

from ultralytics import YOLO

def do_infer(yolo_trained):
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
		results = model.predict(img_g, conf=0.6, max_det=6)

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
	
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '--version', action="store", dest='version', 
		required=False, default='V1', help="'V1' ou 'V2'")
	parser.add_argument('-y', '--yolo', action="store", dest='yolo_version', 
		required=False, default='v8n', help="v8n, v8s, 11n ou 11s")
	parser.add_argument('-b', '--batch', action="store", dest='batch', 
		required=False, type=int, default='8', help="4, 8, 16, ou 32")
	parser.add_argument('-e', '--epochs', action="store", dest='epochs', 
		required=False, type=int, default='100', help="20, 40, 60, 80 ou 100")
	
	args = parser.parse_args()
	version = args.version
	yolo_version = args.yolo_version
	batch = args.batch
	epochs = args.epochs
	
	yolo_weights_path  = f'YOLO-trained-{version}/UCIA-YOLO{yolo_version}/'
	yolo_weights_path += f'batch-{batch:02d}_epo-{epochs:03d}/weights/best_ncnn_model'
	rep = input(f'Utiliser le réseau {yolo_weights_path} [Oui/Non] ? ')

	if rep.lower() in ('', 'o', 'oui', 'y', 'yes'):
		yolo_weights = Path(yolo_weights_path)
		if not yolo_weights.exists():
			print(f'fichier inexitant: <{yolo_weights}>, désolé.')
		else:
			do_infer(yolo_weights)
	

