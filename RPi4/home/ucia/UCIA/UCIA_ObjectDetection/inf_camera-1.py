######################################
#   Jean-Luc.Charles@mailo.com
#   2024/11/21 - v1.0
######################################

import cv2
from picamera2 import Picamera2

from ultralytics import YOLO

# Initialize the Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (800, 600)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

#yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-08_epo-080/weights/best_ncnn_model'
#yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-08_epo-080/weights/best.onnx'

yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-08_epo-100/weights/best_ncnn_model'
#yolo_trained = 'YOLO-trained/UCIA-YOLOv8n/batch-08_epo-100/weights/best.onnx'

#yolo_trained = 'YOLO-trained/UCIA-YOLO11n/batch-10_epo-080/weights/best_ncnn_model'
#yolo_trained = 'YOLO-trained/UCIA-YOLO11n/batch-10_epo-060/weights/best.onnx'

#yolo_trained = 'YOLO-trained/UCIA-YOLOv8s/batch-30_epo-100/weights/best_ncnn_model'
#yolo_trained = 'YOLO-trained/UCIA-YOLOv8s/batch-30_epo-100/weights/best.onnx'
#yolo_trained = 'YOLO-trained/UCIA-YOLO11s/batch-10_epo-060/weights/best_ncnn_model'

# Load the YOLO11 model
model = YOLO(yolo_trained, task='detect')

while True:
    # Capture frame-by-frame
    frame = picam2.capture_array()

    # Run YOLO inference on the frame
    results = model.predict(frame, conf=0.6, max_det=6)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the resulting frame
    cv2.imshow("Camera", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources and close windows
cv2.destroyAllWindows()
