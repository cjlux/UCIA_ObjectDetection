######################################
#   Jean-Luc.Charles@mailo.com
#   2024/11/21 - v1.0
######################################

import cv2
import streamlit as st
from picamera2 import Picamera2

from ultralytics import YOLO

names  = ('balle', 'cube', 'étoile')
colors = ('red', 'green', 'blue')

# Initialize the Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (800, 600)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

st.header('Object Detection Web App')
st.subheader('Powered by YOLOv8')
st.write('Loading the model...')

#yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-08_epo-080/weights/best_ncnn_model'
#yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-08_epo-080/weights/best.onnx'

#yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-08_epo-100/weights/best_ncnn_model'
#yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-08_epo-100/weights/best.onnx'

#yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-04_epo-100/weights/best_ncnn_model'
#yolo_trained = 'YOLO-trained/UCIA-YOLOv8s/batch-30_epo-100/weights/best.onnx'

yolo_trained = 'YOLO-trained/UCIA-YOLO11n/batch-02_epo-100/weights/best_ncnn_model'
#yolo_trained = 'YOLO-trained/UCIA-YOLO11n/batch-02_epo-100/weights/best.onnx'

#yolo_trained = 'YOLO-trained/UCIA-YOLO11n/batch-04_epo-100/weights/best_ncnn_model'
#yolo_trained = 'YOLO-trained/UCIA-YOLO11n/batch-04_epo-100/weights/best.onnx'

#yolo_trained = 'YOLO-trained/UCIA-YOLO11n/batch-10_epo-080/weights/best_ncnn_model'
#yolo_trained = 'YOLO-trained/UCIA-YOLO11n/batch-10_epo-060/weights/best.onnx'

#yolo_trained = 'YOLO-trained/UCIA-YOLO11s/batch-30_epo-100/weights/best_ncnn_model'
#yolo_trained = 'YOLO-trained/UCIA-YOLO11s/batch-08_epo-080/weights/best_ncnn_model'

# Load the YOLO11 model
model = YOLO(yolo_trained, task='detect')



st_frame = st.empty()

while True:
    # Capture frame-by-frame
    frame = picam2.capture_array()

    # Run YOLO inference on the frame
    results = model(frame, conf=0.5, max_det=12)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the resulting frame
    st_frame.image(annotated_frame)

