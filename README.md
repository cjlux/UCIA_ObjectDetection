# UCIA_ObjectDetection
Ce projet vise à exploiter sur RPi4 un réseau de neurones de la famille YOLO (**yolov8n**, **yolov8s**, **yolo11n**, **yolo11s**) entraîné à détecter dans des images trois types d’objets (sphère, cube, étoile) situés en face du robot portant la caméra, dans un rayon de 5 à 45 cm.

Le projet détaille :
- la création des images d'entraînement avec la caméra de la RPi4,
- l'annotation des images d'entraînement sur le site **roboflow**,
- l'entraînnement de réseaux YOLO (yolov8n, yolov8s, yolo11n, yolo11s) sur un PC de calcul muni d'une carte Nvidia, avec exploration des valeurs des méta-paramètre d'entraînement : **batchsize** (2, 4, 8, 16, 20, 30) et **epochs** (20, 40, 60, 80, 100), pour trouver la combinaison donnant le meilleur rapport "temps d'inférence / performance".

Les meilleures version du réseau YOLO entraîné sont exportées sur RPI4 aux formats ONNX et NCNN pour tester leurs temps d'inférence et leurs performances à détecter correctement les objets appris.

Les tests sur RPi4 donnent des temps d'inférence inférieurs à la secondes, avec de bons score de détection pour les réseaux.

Ce dépôt GiHub ne contient pas les fichiers binaires des réseaux YOLO (**yolov8n**, **yolov8s**, **yolo11n**, **yolo11s**) entraînés pour les différentes valeurs des méta-paramètres **batchsize** (2, 4, 8, 16, 20, 30) et **epochs** (20, 40, 60, 80, 100). Pour les construire, il faut entraîner les réseaux YOLO (si possible sur un PC muni d'une carte graphique) avec les procédures et les programmes Python décrits dans le rapport d'étude (voir dossier Doc).


