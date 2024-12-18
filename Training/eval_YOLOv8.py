######################################
#   Jean-Luc.Charles@mailo.com
#   2024/11/18 - v1.1
######################################

from pathlib import Path
from ultralytics import YOLO
from time import sleep
import sys

def main(VER):

    BATCH = {'V1': (2, 4, 8, 10, 16, 20, 30),
             'V2': (2, 4, 8, 16, 32),
             'V2.1':  (2, 4, 8, 16, 32)
            }
    EPOCH = (20, 40, 60, 80, 100)
    YOLO_SIZE = ('n', 's')

    model_dir = Path('./Training/YOLO-pretrained')

    data_path = {'V1': "./datasets/V1.0_yolo8-50train-10val-2test_27nov2024/data.yaml",
                 'V2': "./datasets/V2.0_yolo8-163train-38val-1test_09dec2024/data.yaml",
                 'V2.1': "./datasets/V2.1_yolo8-128train-32val_12dec2024/data.yaml"
                }

    header  = '#meta-params\tpre[ms]\tinf[ms]\tloss[ms]\tpost[ms]\t'
    header += 'prec\trecall\tmAP50\tmAP50-95\tfitness\n'
    header += '#pre:preprocessing; inf:inference; post:postprocessing; prec:precision\n'

    results_dir = Path('./Training/Results')
    if not results_dir.exists():
        results_dir.mkdir()

    for size in YOLO_SIZE:
        yolo = 'YOLOv8' + size
        yolo_weights = yolo.lower() + '.pt'
        
        # load any network for the first time:, because there i son overhead in computing the first time
        model = YOLO(f"Training/YOLO-trained-{VER}/UCIA-YOLOv8{size}/batch-08_epo-020/weights/best.pt")
        metrics = model.val(batch=8, imgsz=640, data=data_path[VER], workers=0)  

        results_file = Path(results_dir, f"results_yolov8{size}-{VER}.txt")
        F_out = open(results_file, "w", encoding="utf8")
        F_out.write(header)
        
        for batch in BATCH[VER]:
            for epoch in EPOCH:
                project = f'Training/YOLO-trained-{VER}/UCIA-{yolo}' 
                name = f'batch-{batch:02d}_epo-{epoch:03d}'

                best = Path(project, name, 'weights', 'best.pt')
                print(best)

                if best.exists(): 
                    model = YOLO(best)  # load a pretrained model 
                    # Validate the model
                    metrics = model.val(batch=batch, imgsz=640, data=data_path[VER], workers=0)  
                    F_out.write(f'{name}')
                    for key in metrics.speed:
                        F_out.write(f'\t{metrics.speed[key]:.2f}')
                    for key in metrics.results_dict:
                        F_out.write(f'\t{metrics.results_dict[key]:.3f}')

                    F_out.write('\n')
                del model
        F_out.close()

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action="store", dest='version', 
                        required=True, help="Work version: 'V1', 'V2' or 'V2.1'")
    
    args = parser.parse_args()
    version = args.version

    main(version)