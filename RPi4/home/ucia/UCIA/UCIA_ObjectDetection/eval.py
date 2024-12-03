######################################
#   Jean-Luc.Charles@mailo.com
#   2024/11/21 - v1.0
######################################

from time import time, sleep
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plot = True

#yolo_trained = '../YOLO-trained/UCIA-YOLOv8n/batch-08_epo-080/weights/best.onnx'
#yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-08_epo-080/weights/best.onnx'
yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-08_epo-080/weights/best_ncnn_model'

#yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-10_epo-080/weights/best.onnx'
#yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-10_epo-080/weights/best_ncnn_model'

#yolo_trained = 'YOLO-trained/UCIA-YOLO11n/batch-16_epo-080/weights/best.onnx'
#yolo_trained = 'YOLO-trained/UCIA-YOLO11n/batch-08_epo-050/weights/best.onnx'

names  = ('balle', 'cube', 'étoile')
colors = ('red', 'green', 'blue')

t0 = time()
# Load a pretrained YOLO11n model
model = YOLO(yolo_trained, task='detect')
load_time = time() - t0
print(f"model loaded in {1000*load_time:.1f} ms")

t0 = time()
#img = Image.open("datasets/sandbox/image.jpg")
#img = Image.open("datasets/sandbox/im501.jpg")
#img = Image.open("datasets/sandbox/test.jpg")
img = Image.open("datasets/sandbox/objets3D-1001.jpg")
img = img.resize((640, 640))
img_g = img.convert("L")
print(f"image pre-processing: {1000*(time() - t0):.1f} ms")
    
t0 = time()
# Run inference on 'bus.jpg' with arguments
result = model.predict(img_g, conf=0.6, max_det=1)[0]
print(f"Inference1: {1000*(time() - t0):.1f} ms")

sleep(2)

INF_TIME = []
for _ in range(1):
	t0 = time()
	# Run inference on 'bus.jpg' with arguments
	result = model.predict(img_g, conf=0.5, max_det=12)[0]
	inf_time = time() - t0
	print(f"Inference2: {1000*inf_time:.1f} ms")

	INF_TIME.append(inf_time)
	boxes = result.boxes  # Boxes object for bounding box outputs

	if plot:

		plt.figure()
		'''
		array = result.plot()
		array[x1:x2, y1:y2]=255
		plt.imshow(array)
		#plt.plot()
		plt.show()'''
		
		np_img = np.array(img)
		plt.imshow(np_img)

		t0 = time()
		for class_id, conf, xyxy, in zip(boxes.cls, boxes.conf, boxes.xyxy):
			class_id = int(class_id)
			y1, x1, y2, x2  = xyxy.numpy().astype(int)
		
			X = [x1, x2, x2, x1, x1]
			Y = [y1, y1, y2, y2, y1]
			
			name = f'{names[class_id]:6s} '
			
			
			avRGB = np_img[x1:x2, y1:y2, :].mean(axis=0).mean(axis=0)
			if max(abs(avRGB[0] - avRGB[1]), abs(avRGB[0] - avRGB[2]), abs(avRGB[1] - avRGB[2])) < 15:
				color = "black"
			else:
				col   = avRGB.argmax()
				color = colors[col]
            
			plt.text(y1, x1-5, name + f'{conf:3.2f} ', color=color, size=6,
				backgroundcolor='white', alpha=0.5,
				bbox=dict(boxstyle="square", ec=color, fc=(1., 1, 1)))
				
			name = name + f'{color:6s}'
			print(name, f'{conf:3.2f} ', color, (y1,x2,y2,x1), tuple(avRGB.astype(int)))
			
			plt.plot(Y, X, color=color)
			plt.title('/'.join(yolo_trained.split('/')[1:]))
		print(f"Plotting: {1000*(time() - t0):.1f} ms")
		plt.show()
	
time_array = np.array(INF_TIME)
time_array_ms = [f'{t*1000:.1f} ms' for t in time_array]
print('Inferences elapsed time:', time_array_ms)

print(f'inference time mean: {1e3*time_array.mean():.1f} ms, std: {1e3*time_array.std():.1f} ms')

