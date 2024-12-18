######################################
#   Jean-Luc.Charles@mailo.com
#   2024/12/16 - v1.1
######################################

from flask import Flask, Response
from picamera2 import Picamera2
import cv2
import numpy as np

from ultralytics import YOLO

from PIL import ImageFont, ImageDraw, Image

font1 = ImageFont.truetype("/home/ucia/.config/Ultralytics/Arial.ttf", 12)
font2 = ImageFont.truetype("/home/ucia/.config/Ultralytics/Arial.ttf", 14)

class_name  = ('Ball', 'Cube', 'Star')
main_color  = ('red', 'green', 'blue')
class_color = ((80, 145, 255, 250), (240, 150, 100, 250), (255, 255, 255, 250))
box_color   = ((80, 145, 255, 150), (240, 150, 100, 150), (255, 255, 255, 150))
label_color = ((255, 255, 255, 250), (0, 0, 0, 250), (0, 0, 0, 250))
label_width = (47, 56, 48)

app = Flask(__name__)

def generate_frames():
	
	while True:

		# Capture frame-by-frame
		img = picam2.capture_image()
		img = img.resize((640, 640))
		img_g  = img.convert("L")

		# Run YOLO inference on the frame
		results = model.predict(img_g, imgsz=640, classes=[0,1,2], conf=confidence, max_det=maxdetect)		
		boxes   = results[0].boxes

		for class_id, conf, xyxy, in zip(boxes.cls, boxes.conf, boxes.xyxy):
			class_id = int(class_id)
			name = class_name[class_id]
			label = f'{name} {conf:3.2f}' 
			# The bounding box coordinates:
			x1, y1, x2, y2  = xyxy.numpy().astype(int)
			# object center coordinates:
			cx, cy = (x1+x2)//2, (y1+y2)//2
			# mean object color around the center:
			color = np.array(img)[cy-7:cy+7, cx-7:cx++7].mean(axis=0).mean(axis=0).astype(int)
			if abs(color[0] - color[1]) < 20 and abs(color[0] - color[2]) < 20 and abs(color[1] - color[1]) < 20:
				col = 0
			else:
				col   = color.argmax() + 1
			print(class_id, int(conf*100), col, x1,y2,x2,y1, color[0], color[1], color[2])
			
			draw = ImageDraw.Draw(img, 'RGBA')
			# Draw the networh path
			draw.rectangle([(10, 30),(630, 10)], fill=(150, 100, 90))
			draw.text((10, 13), yolo_weights_path, font=font2, fill=(250, 250, 250), size=14)
			# The bounding box
			draw.rectangle([(x1, y1),(x2, y2)], outline=box_color[class_id], width=2)
			# The label inside its white rectangle:
			draw.rectangle(((x1, y1),(x1+label_width[class_id], y1-11)), fill=class_color[class_id])
			draw.text((x1, y1-12), label, font=font1, fill=label_color[class_id])
			np_img = np.array(img)[::,::,::-1]
				
		ret, buffer = cv2.imencode('.jpg', np_img)
		frame = buffer.tobytes()
		yield (b'--frame\r\n'
		b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
	return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

	from pathlib import Path
	import argparse, sys
	
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '--version', action="store", dest='version', 
		required=False, default='V1', help="'V1', 'V2' ou 'V2.1'")
	parser.add_argument('-y', '--yolo', action="store", dest='yolo_ver', 
		required=False, default='v8n', help="v8n, v8s, 11n ou 11s")
	parser.add_argument('-b', '--batch', action="store", dest='batch', 
		required=False, type=int, default='8', help="2, 4, 8, 16, ou 32")
	parser.add_argument('-e', '--epochs', action="store", dest='epochs', 
		required=False, type=int, default='100', help="20, 40, 60, 80 ou 100")
	parser.add_argument('-m', '--maxdetect', action="store", dest='maxdetect', 
		required=False, type=int, default='6', help="Nombre max d'objets à déttecter.")
	parser.add_argument('-c', '--confidence', action="store", dest='conf', 
		required=False, type=float, default='0.6', help="Seuil de confiance pour afficher une détection.")
	
	args = parser.parse_args()
	version    = args.version
	yolo_ver   = args.yolo_ver
	batch      = args.batch
	epochs     = args.epochs
	maxdetect  = args.maxdetect
	confidence = args.conf
	
	yolo_weights_path  = f'YOLO-trained-{version}/UCIA-YOLO{yolo_ver}/'
	yolo_weights_path += f'batch-{batch:02d}_epo-{epochs:03d}/weights/best_ncnn_model'
	yolo_weights = Path(yolo_weights_path)
	print(f'Inférences du réseau {yolo_weights}')

	if not yolo_weights.exists():
		print(f'fichier inexitant: <{yolo_weights}>, désolé.')
	else:
		# Initialize the Picamera2
		picam2 = Picamera2()
		picam2.preview_configuration.main.size = (640, 640)
		picam2.preview_configuration.main.format = "RGB888"
		picam2.preview_configuration.align()
		picam2.configure("preview")
		picam2.start()
		
		model = YOLO(yolo_weights, task='detect')
		
		app.run(host='0.0.0.0', port=5000)
