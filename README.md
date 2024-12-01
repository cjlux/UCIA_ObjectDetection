# UCIA_ObjectDetection
Ce projet vise à exploiter sur RPi4 un réseau de neurones de la famille YOLO (**yolov8n**, **yolov8s**, **yolo11n**, **yolo11s**) entraîné à détecter dans des images trois types d’objets (sphère, cube, étoile) situés en face du robot portant la caméra, dans un rayon de 5 à 45 cm.

Le projet détaille :
- la création des images d'entraînement avec la caméra de la RPi4,
- l'annotation des images d'entraînement sur le site **roboflow**,
- l'entrainnement de réseaux YOLO (yolov8n, yolov8s, yolo11n, yolo11s) sur un PC de calcul muni d'une carte Nvidia, avec exploration des valeurs des méta-paramètre d'entraînement : **batchsize** (2, 4, 8, 16, 20) et **epochs** (20, 40, 60, 80, 100), pour trouver la combinaison donnant le meilleur rapport "temps d'inférence / performance".

Les meilleures version de YOLO entraîné sont exportées sur RPI4 aux formats ONNX et NCNN pour tester leurs temps d'inférence et leurs performances à détecter correctement les objets appris.

Les tests sur RPi4 donnent des temps d'inférence inférieurs à la secondes, avec de bons score de détection pour les réseaux, pour les configurations :
- **yolov8n** entraîné avec batchsize=8 et epochs=90,
- **yolov11n** entraîné avec batchsize=8 et epochs=100.

Ce dépôt GiHub ne contient pas les fichiers binaires des réseaux YOLO (**yolov8n**, **yolov8s**, **yolo11n**, **yolo11s**) entraînés pour les valeurs des méta-paramètres **batchsize** (2, 4, 8, 16, 20) et **epochs** (20, 40, 60, 80, 100).
Pour les construire, il faut taper `Training/train_YOLOv8.py` et `Training/train_YOLOv8.py` dans un terminal, depuis le répertoire `UCIA_ObjectDetection`. Il y a en tout 120 fichiers binaires au format ONNX et NCNN.


