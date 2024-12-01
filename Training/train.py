!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="Ny9NMZSMmx8SPGINFx31")
project = rf.workspace("ucia").project("ucia-ia-object-detection")
version = project.version(1)
dataset = version.download("yolov8")
                
# curl version
#curl -L "https://app.roboflow.com/ds/xYKXRBKJIS?key=UI54bi3N17" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip

# raw URL
# https://app.roboflow.com/ds/xYKXRBKJIS?key=UI54bi3N17
