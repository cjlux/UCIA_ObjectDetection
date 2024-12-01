# UCIA_ObjectDetection
Ce projet vise à exploiter sur RPi4 un réseau de neurones de la famille YOLO (**yolov8n**, **yolov8s**, **yolo11n**, **yolo11s**) entraîné à détecter dans des images trois types d’objets (sphère, cube, étoile) situés en face du robot portant la caméra, dans un rayon de 5 à 45 cm.

Le projet détaille :
- la création des images d'entraînement avec la caméra de la RPi4,
- l'annotation des images d'entraînement sur le site **roboflow**,
- l'entrainnement de réseaux YOLO (yolov8n, yolov8s, yolo11n, yolo11s) sur un PC de calcul muni d'une carte Nvidia, avec exploration des valeurs des méta-paramètre d'entraînement : **batchsize** (2, 4, 8, 16, 20) et **epochs** (20, 40, 60, 80, 100), pour trouver la combinaison donnant le meilleur rapport "temps d'inférence / performance".

Les meillieures version de réseaux YOLO entraînés sont exportés sur RPI4 aux formats .onnx et .cncnn pour tester leur temps d'inférence et leurs performances à détecter correctemet les objets appris.

Les tests sur RPi4 donnent des temps d'inférence inférieurs à la secondes, avec de bons score de détection pour les réseaux :
- yolov8n entraîné avec batchsize=8 et epochs=90,
- yolov11n entraîné avec batchsize=8 et epochs=90.

Ce dépôt GiHub ne contient pas les fichiers binaires des réseaux YOLO (**yolov8n**, **yolov8s**, **yolo11n**, **yolo11s**) entrainnés pour les valeurs des méta-paramètre d'entraînement : **batchsize** (2, 4, 8, 16, 20) et **epochs** (20, 40, 60, 80, 100), ce qui donne 120 fichiers binaires au format ONNX et NCNN.
Pour les construire, il faut taper `Training/train_YOLOv8.py` et `Training/train_YOLOv8.py' dans un terminal, depuis le répertoire `UCIA_ObjectDetection/Training/`.


