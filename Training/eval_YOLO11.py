######################################
#   Jean-Luc.Charles@mailo.com
#   2024/11/14 - v1.0
######################################

from pathlib import Path
from ultralytics import YOLO
from time import sleep
import sys

data_path = "./datasets/yolo11-50train-10val-2test_27nov2024/data.yaml"

BATCH = (2, 4, 8, 10, 16, 20, 30)
EPOCH = (20, 40, 60, 80, 100)
YOLO_SIZE = ('n', 's')

header  = '#meta-params\tpre[ms]\tinf[ms]\tloss[ms]\tpost[ms]\t'
header += 'prec\trecall\tmAP50\tmAP50-95\tfitnessi\n'
header += '#pre:preprocessing; inf:inference; post:postprocessing; prec:precision\n'

for size in YOLO_SIZE:
    yolo = 'YOLO11' + size
    yolo_weights = yolo.lower() + '.pt'

    # load any network for the first time:, because there i son overhead in computing the first time
    model = YOLO(f"Training/YOLO-trained/UCIA-YOLO11{size}/batch-08_epo-020/weights/best.pt")
    metrics = model.val(batch=8, imgsz=640, data=data_path, workers=0)  

    results_file = f"results_yolo11{size}.txt"
    F_out = open(results_file, "w", encoding="utf8")
    F_out.write(header)

    for batch in BATCH:
        for epoch in EPOCH:
            project = f'Training/YOLO-trained/UCIA-{yolo}' 
            name = f'batch-{batch:02d}_epo-{epoch:03d}'

            best = Path(project, name, 'weights', 'best.pt')
            print(best)
        
            if best.exists(): 
                model = YOLO(best)  # load a pretrained model 
                # Validate the model
                metrics = model.val(batch=batch, imgsz=640, data=data_path, workers=0)  
                F_out.write(f'{name}')
                for key in metrics.speed:
                    F_out.write(f'\t{metrics.speed[key]:.2f}')
                for key in metrics.results_dict:
                    F_out.write(f'\t{metrics.results_dict[key]:5.3f}')

                F_out.write('\n')
            del model
F_out.close()
