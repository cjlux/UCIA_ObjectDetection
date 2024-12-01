######################################
#   Jean-Luc.Charles@mailo.com
#   2024/11/14 - v1.0
######################################

from pathlib import Path
from ultralytics import YOLO
from time import sleep

#
# this programm must be run from the UCIA_ObjectDetection directory
#

BATCH = (2, 4, 8, 10, 16, 20, 30)
EPOCH = (20, 40, 60, 80, 100)
YOLO_SIZE = ('n', 's')

model_dir = Path('./Training/YOLO-pretrained')

data_path = "./datasets/yolo8-50train-10val-2test_27nov2024/data.yaml"
for size in YOLO_SIZE:

    yolo = 'YOLOv8' + size
    yolo_weights = yolo.lower() + '.pt'

    for batch in BATCH:
        for epoch in EPOCH:
            project = f'Training/YOLO-trained/UCIA-{yolo}' 
            name = f'batch-{batch:02d}_epo-{epoch:03d}'

            best = Path(project, name, 'weights', 'best.pt')
            print(f'{best}')
            if not best.exists(): 
                model = YOLO(model_dir / yolo_weights)  # load a pretrained model 
                model.train(data=data_path, 
                            epochs=epoch, 
                            imgsz=640, 
                            batch=batch, 
                            patience=100, 
                            cache=False,
                            workers=0,
                            project=project, 
                            name=name, 
                            exist_ok=True, 
                            pretrained=True,
                            optimizer='auto', 
                            seed=1234)

            print(f'looking for <best.onnx>... ')            
            best_onnx = Path(project, name, 'weights', 'best.onnx')
            if not best_onnx.exists():
                print('\t exporting <best.pt> to <best.onnx>...', end="")
                model = YOLO(best)  # load a custom trained model
                model.export(format="onnx", int8=True, data=data_path)
                print(" done.")

            print(f'looking for <best_ncnn_model>... ')            
            best_ncnn_model = Path(project, name, 'weights', 'best_ncnn_model')
            if not best_ncnn_model.exists():
                print('\t exporting <best.pt> to <best_ncnn_model>...', end="")
                model = YOLO(best)  # load a custom trained model
                model.export(format="ncnn", int8=True, data=data_path)
                print(" done.")
                
            sleep(1)
