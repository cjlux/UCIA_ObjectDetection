# UCIA_ObjectDetection
Ce projet vise à exploiter sur RPi4 un réseau de neurones de la famille YOLO (**yolov8n**, **yolov8s**, **yolo11n**, **yolo11s**) entraîné à détecter dans des images trois types d’objets (sphère, cube, étoile) situés en face du robot portant la caméra, dans un rayon de 5 à 45 cm.

Un première étude préliminaire (V1) est menée avec 62 images annotées contenant 10 objets chacune, obtenue avec la caméra Raspberrypy Standard.
Les objectifs sont :
- tester la faisabilité d'entraîner un réseau YOLO avec ces images,
- évaluer le temps d'inférence sur RPi4 d'un réseau YOLO entraîné à la détection des objets 3D.
À la suite de cette étude, le temps d'inférence trouvé est de l'ordre de 0.5 seconde sur RPi4, avec des détections d'objets très satisfaisante.

La deuxième étude vise à consolider l'étude préliminaire en utilisant la configuration matérielle préconisée dans le CDC du projet UCIA : Carte RPi4 équipée de la caméra RaspberryPi Grand Angle, fixée sur le robot Thymio à l'aide d'un support plexiglass. On retrouve les étapes de l'étude préliminaire :
- création de 200 images de 12 objets chacune avec la caméra "Grand Angle",
- annotation des images sur le site **roboflow**,
- entraînnement des 4 réseaux YOLO (yolov8n, yolov8s, yolo11n, yolo11s) sur un PC de calcul muni d'une carte Nvidia, avec exploration des valeurs des méta-paramètre d'entraînement :
  - **batch** (2, 4, 8, 16, 32) 
  - **epochs** (20, 40, 60, 80, 100),
  Le but est de trouver la combinaison des valeurs de **batc** et de **epchos**  donnant le meilleur rapport "temps d'inférence / performance".

Les meilleures version du réseau YOLO entraîné sont exportées sur RPI4 au formats NCNN pour tester leurs temps d'inférence et leurs performances à détecter correctement les objets appris.

Les tests sur RPi4 donnent des temps d'inférence inférieurs à la secondes, avec de très bons score de détection.

Ce dépôt GiHub ne contient pas les fichiers binaires des réseaux YOLO (**yolov8n**, **yolov8s**, **yolo11n**, **yolo11s**) entraînés pour les différentes valeurs des méta-paramètres **batchsize** (2, 4, 8, 16, 32) et **epochs** (20, 40, 60, 80, 100). Pour les construire, il faut entraîner les réseaux YOLO (si possible sur un PC muni d'une carte graphique) avec les procédures et les programmes Python décrits dans le rapport d'étude (voir dossier Doc).


