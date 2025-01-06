sudo raspi-config 
mkdir UCIA
cd UCIA/
python -m venv --system-site-packages vision
source vision/bin/activate
python -m venv --system-site-packages vision
ls
rm -rf vision/
deactivate 
python -m venv --system-site-packages vision
source vision/bin/activate
pip install ultralytics, onnx, annxruntime
pip install ultralytics
pip install onnx
pip install onnxruntime
sync
df -h
cd UCIA/
cd UCIA_ObjectDetection/
ls
vim eval_YOLOv8-onnx.py 
!
ls -lart
rm .eval_YOLOv8-onnx.py.swp 
vim eval_YOLOv8-onnx.py 
cd UCIA/UCIA_ObjectDetection/
python inference_camera.py 
cd ..
du -sh vision/
ls
cd UCIA_ObjectDetection/
ls
ls -l
ls runs/
ls runs/detect/
ls runs/detect/val
rm -rf runs/
ls -l
mv inference_camera.py inf_camera-1.py
mv inference_camera-2.py inf_camera-2.py

python inf_camera-1.py 
python inf_camera-2.py 
ifconfig 
dmesg 
ifconfig 
cd /var/lod
ls /var/
cd /var/log/
ls -lrt
cat lastlog 
dmesg 
ps axu|grep ssh
systemctl status ssh
top
sudo raspi-config 
q
ifconfig 
dmesg 
systemctl status vnc
systemctl status vncserver
systemctl status vncserver-virtuald.service 
systemctl status vncserver-x11-serviced.service 
ps axu
ps axu|grep vnc
pwd
top
pwd
ls -lrt
top
ps axu
cd UCIA/
top
exit
geany
echo $DISPLAY
exit
ifconfig 
top
cd UCIA/
cd UCIA_ObjectDetection/
ls
python inf_camera-1.py
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py
iwconfig
systemctl status hostapd
systemctl status hostapd.service
ps axu
ps axu|grep hostap
ps axu
ifconfig 
geany
ps axu
ifconfig 
geany
python inf_camera-2.py
python eval.py 
python inf_camera-2.py
ifconfig 
cd YOLO-trained/
ls
cd UCIA-YOLO11n/
ls
mv ~/02-04.tgz .
tar tvzf 02-04.tgz 
tar xvzf 02-04.tgz 
rm 02-04.tgz 
cd ../..
ls
python inf_camera-2.py
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py 
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py 
ifconfig -a
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py 
pip insstall simple jpeg
pip install simple jpeg
pip install simplejpeg
python server.py 
sudo raspi-config 
ps axu
ps axu|grep vnc
ls /usr/sbin/*vnc*
sudo raspi-config 
sudo reboot
sudo apt install xrdp
udo service xrdp start
sudo service xrdp start
sudo service xrdp status
pwd
cd UCIA//UCIA_ObjectDetection/
python inf_camera-2.py 
cd
cd Desktop/
ls
ls -a
history
sudo systemctl status xrdp
dpkg -l |grep rdp
sudo apt purge xrdp
dpkg -l |grep rdp
sudo  /etc/xrdp/xrdp.ini
df
sudo umount $HOME/thinclient_drives
sudo systemctl status xrdp
sudo systemctl stop xrdp
history 
cd
ls
cd Téléchargements/
wget https://download.teamviewer.com/download/linux/teamviewer-host_armhf.deb
sudo apt install ./teamviewer-host_armhf.deb 
cp ./teamviewer-host_armhf.deb /tmp
sudo apt install /tmp/teamviewer-host_armhf.deb 
sudo apt autoremove
sudo teamviewer setup 
sudo teamviewer info 
sudo systemctl teamviewer
sudo systemctl teamviewerd.service
sudo systemctl teamviewerd
sudo systemctl status teamviewerd
sudo teamviewer info 
sudo systemctl status teamviewerd
dmesg 
wget https://download.nomachine.com/download/7.7/Raspberry/nomachine_7.7.4_1_armhf.deb
sudo apt install ./nomachine_7.7.4_1_armhf.deb 
wget https://download.nomachine.com/download/7.7/Raspberry/nomachine_7.7.4_1_armhf.deb
uname -a
cd
cd Téléchargements/
ls -lrt
sudo apt install ./nomachine_8.14.2_1_arm64.deb 
dems
dmesg 
ifconfig 
systemctl status nxserver.service 
d;es
top
sudo systemctl stop nxserver.service 
dpkg -l |grep nx
dpkg -l |grep NX
dpkg -l |grep nom
sudo apt purge nomachine
dpkg -l |grep team
sudo apt purge teamviewer-host:armhf
dpkg -l |grep team
sudo apt install streamlit
pip install streamlit
pip install idlex
idlex
bg
cd UCIA/UCIA_ObjectDetection/
streamlit run inf_camera-3.py 
python
streamlit run inf_camera-3.py 
top
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py 
streamlit run inf_camera-3.py 
python
streamlit run inf_camera-3.py 
streamlit --help
streamlit run inf_camera-3.py 
python
streamlit run inf_camera-3.py 
ifconfig 
pwd
cd UCIA/
cd UCIA_ObjectDetection/
ls
python take_image.py 
vim take_image.py 
python take_image.py 
ls -lrt
python take_image.py 
vim take_image.py 
python take_image.py 
vim take_image.py 
python take_image.py 
geany take_image.py 
python take_image.py 
geany take_image.py 
python take_image.py 
ifconfig 
cd UCIA/UCIA_ObjectDetection/
git status
ls
tar cvzf images_objets3D_8dec2024.tgz *.jpg
ls
ls datasets/
ls datasets/images/
mkdir datasets/images/8dec2024
mv *.jpg datasets/images/8dec2024/
ls -lart
mv images_objets3D_8dec2024.tgz datasets/images/
cd datasets/
ls -lart
cd images/
ls
ls -l
mkdir 14nov2024
ls
mv objets3D-0*.jpg 14nov2024/
ls
ls -l
mv 8dec2024/ 08dec2024/
mv images_objets3D_8dec2024.tgz images_objets3D_08dec2024.tgz 
cd ..
ls
tar tvf datasets.tar 
mv datasets.tar datasets_v1_50-10-2.tar 
ls
ls -l
ls images/
ls sandbox/
cd ..
ls
ls -lrt
cd datasets/
ls -l
cd images/
ls
ls -l 14nov2024/
ls
ls 14nov2024/
ifconfig 
ls
tar xvzf h.tgz 
rm h.tgz 
cd HOTSPOT/
ls -l
unzip -l rpi3-hotspot.zip 
ls
ls rpi3-hotspot
ls rpi3-hotspot/boot/
ls rpi3-hotspot/etc
cd rpi3-hotspot/
ls
cat install.sh 
cat README.md 
sudo -s
top
cd UCIA/UCIA_ObjectDetection/
python take_image.py 
ls
top
ls
python inf_camera-2.py 
rpicam-hello 
rpicam-still 
cd UCIA/UCIA_ObjectDetection/
python take_image.py 
ifconfig 
ifconfig eth0
sudo systemctl status rpi-access-point
sudo apt install iptables
sudo systemctl status rpi-access-point
sudo systemctl stop rpi-access-point
sudo systemctl status rpi-access-point
ifconfig eth0
cat /etc/networks 
cat /etc/network/interfaces 
sudo vim /etc/network/interfaces 
sudo vim /etc/dhcpcd.conf 
ifconfig 
ifconfig -a
service --status-all
sudo systemctl stop dnsmasq
service --status-all
ifconfig -a
sudo ifconfig eth0 up
ifconfig -a
sudo vim /etc/dhcpcd.conf 
service --status-all
sudo systemctl enable networking
sudo systemctl list
sudo systemctl -h
sudo systemctl list-unit
sudo systemctl list-units
service networmanager status
service NetworkManager.service status
sudo systemctl status NetworkManager
sudo systemctl restart NetworkManager
sudo systemctl status NetworkManager
ifconfig eth0
sudo ifconfig eth0 up
sudo ifconfig -h
sudo ifconfig eth0 up 192.168.1.17
ifconfig eth0
sudo apt install iptables
sudo sytemctl status rpi-access-point
sudo sytemctrl status rpi-access-point
sudo systemctrl status rpi-access-point
sudo systemctl status rpi-access-point
sudo apt install ifup
sudo apt install ifupdown
sudo systemctrl restart rpi-access-point
sudo systemctl restart rpi-access-point
sudo systemctl status rpi-access-point
ifconfig -a
history
cd
cd UCIA/UCIA_ObjectDetection/
python take_image.py 
sudo nmtui
cd
cd HOTSPOT/
cd ho
ls
cd rpi3-hotspot/
ls
cat README.md 
sudo systemctl stop rpi-access-point
sudo systemctl disable rpi-access-point
sudo rm /etc/systemd/system/rpi-access-point.service /usr/bin/rpi-access-point
sudo systemctl daemon-reload
sudo apt install networkmanager
dpkg -l |grep net
sudo apt install -U network-manager
sudo apt install --U network-manager
sudo apt install -h
sudo apt reinstall network-manager
route -n
route add -n 192.168.1.1 gateway
route add -net 192.168.1.1 gateway
route add -net 192.168.1.1 gw
route add -net 192.168.1.1 gw netmask 192.168.0.0
ifconfig 
ifup etho
sudo ifconfig eth0 up 192.168.1.17
ifconfig 
route add -net 192.168.1.1 gw netmask 192.168.0.0
ping 192.168.1.1
route -h
route add -h
route add -net 0.0.0. 192.168.1.1 gw netmask 192.168.0.0
route add -net 0.0.0.0 gw 192.168.1.1 netmask 192.168.0.0
route add -net 0.0.0.0 gw 192.168.1.1
sudo route add -net 0.0.0.0 gw 192.168.1.1
route -n
sudo raspi-config
sudo nmcli con add con-name hotspot ifname wlan0 type wifi ssid "RPi4-UCIA"
sudo nmcli con modify hotspot wifi-sec.key-mgmt wpa-psk
sudo nmcli con modify hotspot wifi-sec.psk 'poppy!station'
sudo nmcli con modify hotspot 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared
sudo apt purge network-manager
sufo rm -rf /etc/NetworkManager/system-connections
sudo rm -rf /etc/NetworkManager/system-connections
sudo apt install network-manager
history 
ifconfig 
sudo apt purge hostapd
sudo rm -rf /etc/hostapd/
sudo apt purge dnsq
cd HOTSPOT/
ls
cat make_hostSpot.sh 
cd rpi3-hotspot/
ls
cat README.md 
cat install.sh 
sudo apt purge dnsmasq
sudo apt purge iptables
sudo rm -rf /etc/dnsmasq.d/
sudo apt purge ifupdown
sudo apt purge network-manager
sudo apt install network-manager
mv /etc/network/interfaces./tmp
mv /etc/network/interfaces /tmp
sudo mv /etc/network/interfaces /tmp
sudo apt purge network-manager
sudo apt install network-manager
ifconfig 
sudo sytemctl status NetworkManager
sudo systemctl status NetworkManager
sudo systemctl rsetart NetworkManager
sudo systemctl restart NetworkManager
sudo systemctl status NetworkManager
nmtui -v
nmcli -v
ifconfig -a
sudo systemctl restart NetworkManager
dmesg 
ifconfig -a
sudo systemctl restart NetworkManager
dmesg 
top
cat ~/.bashrc 
ps axu
sudo systemctl restart NetworkManager
ps axu
top
sudo systemctl restart NetworkManager
top
systemctl status vnc
systemctl status vncserver-x11-serviced.service 
dpkg -l |grep vnc
ps axu|grep vnc
sudo apt purge realvnc-vnc-server
ps axu|grep vnc
sudo raspi-config 
dmesg 
python take_image.py 
cd UCIA/UCIA_ObjectDetection/
python take_image.py 
ls -lrt
free
top
cd 
cd HOTSPOT/
cd rpi3-hotspot/
vim install.sh 
ls
cd etc/
ls
cd network/
ls
vim interfaces 
cd ..
vim install.sh 
sudo apt purge networkManager
sudo apt purge NetworkManager
sudo apt purge Network-Manager
sudo apt purge network-manager
vim install.sh 
ls boot/
cat boot/hotspot.txt.example 
sudo boot/hotspot.txt.example /boot/
sudo cp boot/hotspot.txt.example /boot/
sudo vim /boot/hotspot.txt
ls /boot/
rm /boot/hotspot.txt.example 
sudo rm /boot/hotspot.txt.example 
cat boot/hotspot.txt.example 
sudo vim /boot/hotspot.txt 
sudo ./install.sh 
vim install.sh 
sudo ./install.sh 
systemctl status dnsmasq
systemctl status dhcpd
systemctl status dhcpcd
systemctl status rpièaccess-point
systemctl status rpi-access-point
top
ifconfig 
rpicam-hello 
rpicam-hello -h
rpicam-hello --list-cameras
rpicam-hello -p 0,0,640,480
rpicam-hello -h
rpicam-hello --width 640
rpicam-hello --width 640 __height 640
rpicam-hello --width 640 --height 640
sudo ifconfig eth0 up 192.168.1.17
sudo apt reinstall picamera2
deactivate
rpicam-hello --width 640 --height 640
pdpkg -l|grep camer
dpkg -l|grep camer
sudo apt reinstall python3-picamera2
rpicam-hello --width 640 --height 640
su apt update
sudo apt update
apt list --updradable
apt list --upgradable
sudo apt upgrade
rpicam-hello --width 640 --height 640
sudo apt purge network-manager
ls /etc/NetworkManager/system-connections
rm -rf /etc/NetworkManager
sudo rm -rf /etc/NetworkManager
rpicam-hello --width 640 --height 640
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py 
rpicam-hello --width 640 --height 640
python inf_camera-2.py 
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py 
python inf_camera-3.py 
ls -lrt
vim inf_camera-3.py 
python inf_camera-3.py 
streamlit run inf_camera-3.py
streamlit run -h
streamlit run --help
streamlit run inf_camera-3.py --server.headless 1
rpicam-hello 
cd UCIA/UCIA_ObjectDetection/
streamlit run inf_camera-3.py --server.headless 1
top
streamlit run inf_camera-3.py 
cd UCIA/UCIA_ObjectDetection/
streamlit run inf_camera-3.py 
vim inf_camera-3.py 
streamlit run inf_camera-3.py 
cd UCIA/UCIA_ObjectDetection/
streamlit run inf_camera-3.py 
vim inf_camera-3.py 
ls
vim server-obj-detection.py 
vim server.py 
python server.py 
ls -lrt
vim inf_camera-3.py 
streamlit run inf_camera-3.py 
sudo ifconfig eth0 up 192.168.1.17
ifconfig -a
route -n
sudo route add -net 0.0.0.0 gw 192.168.1.1
route -n
exit
cd UCIA/UCIA_ObjectDetection/
streamlit run inf_camera-3.py 
cd UCIA/UCIA_ObjectDetection/
vim inf_camera-3.py 
streamlit run inf_camera-3.py 
rpicam-hello 
rpicam-still 
rpicam-still -h
rpicam-still -t 1000000
streamlit run inf_camera-3.py 
python eval.py 
python inf_camera-2.py 
vim inf_camera-3.py 
streamlit run inf_camera-3.py --server.headless 1
vim inf_camera-3.py 
streamlit run inf_camera-3.py
vim inf_camera-3.py 
streamlit run inf_camera-3.py 2> /dev/null
rpicam-hello 
python server-flask.py 
python inf_camera-3.py 
deactivate
sudo apt install python3-opencv python3-flask python3-picamera2
sudo apt install python3-flask python3-picamera2
sudo apt autoremove
vim server-flask.py
python server-flask.py 
top
ls -lart
ls -lart .local/
ls -lart .config/
ls -lart .config/geany/
vim .config/geany/geany.conf 
geany 
vim .config/geany/geany.conf 
rm .config/geany/geany.conf 
geany 
cd UCIA/UCIA_ObjectDetection/
python inf_camera-3.py 
cd UCIA/UCIA_ObjectDetection/
python inf_camera-3.py 
python test_flack.py 
python inf_camera-3.py 
python inf_camera-3.py -version 2
python inf_camera-3.py
python inf_camera-3.py --v V1
python inf_camera-3.py -vv V1
python inf_camera-3.py -v V1
ls OLO-trained-V1/UCIA-YOLOv8n/batch-04_epo-100/weights/best_ncnn_model
ls YOLO-trained-V1/UCIA-YOLOv8n/batch-04_epo-100/weights/best_ncnn_model
python inf_camera-3.py -v V1 -b 8
python inf_camera-3.py -v V1 -b 8 2> /dev/null
python inf_camera-3.py -v V1 -b 8 1> /dev/null
python test_flack.py 
vim index.html
python test_flack.py 
cat index.html 
python test_flack.py 
mkdir templates
mv index.html templates/
python test_flack.py 
python inf_camera-3.py -v V1 -b
python inf_camera-3.py -v V1 -b 2
python inf_camera-3.py -v V1 -b 8
python inf_camera-3.py -v V1 -y 11n -b 2
python inf_camera-3.py 
cd UCIA/UCIA_ObjectDetection/
python inf_camera-3.py 
vim inf_camera-3.py 
python inf_camera-3.py 
python inf_camera-3.py  -h
python inf_camera-3.py 
python inf_camera-3.py -u 11n -b 2
python inf_camera-3.py -y 11n -b 2
sudo sync
sudo shutdown
sudo shutdown -h now
top
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py 
python take_image.py 
ls -lrt
ssh jlc@king
ls -lrt
cd
ls -lrt
tar tvf V2.tar 
mv V2.tar UCIA/UCIA_ObjectDetection/
cd UCIA/UCIA_ObjectDetection/
ls
tar tvf V2.tar 
tar xvf V2.tar 
ls
python inf_camera-2.py 
vim inf_camera-2.py 
python inf_camera-2.py 
python inf_camera-2.py -v V2
vim inf_camera-2.py 
python inf_camera-2.py -v V2
python inf_camera-2.py -v V2 -b 4 -e 100
python inf_camera-2.py -v V2 -b 4 -e 20
python inf_camera-2.py -v V2 -b 32 -e 20
python inf_camera-2.py -v V1 -b 4 -e 20
python inf_camera-2.py -v V1 -y 11n -b 4 -e 20
python inf_camera-2.py -v V1 -y 11s -b 8 -e 20
python inf_camera-2.py -v V1
python inf_camera-2.py -v V1 -y 11s -b 8 -e 20
python inf_camera-2.py -v V2 -y 8n -b 8 -e 100
python inf_camera-2.py -v V2 -y v8n -b 8 -e 100
python inf_camera-2.py -v V2 -y v8s -b 8 -e 100
python inf_camera-2.py -v V2 -y v8s -b 4 -e 100
python inf_camera-2.py -v V2 -y v8s -b 16 -e 100
python inf_camera-2.py -v V2 -y v8s -b 16 -e 20
python inf_camera-2.py -v V2 -y v8s -b 32 -e 20
python inf_camera-2.py -v V2 -y v8s -b 32 -e 40
python inf_camera-2.py -v V2 -y v8s -b 32 -e 60
python inf_camera-2.py -v V2 -y v8s -b 32 -e 80
python inf_camera-2.py -v V2 -y v8s -b 32 -e 100
python inf_camera-2.py -v V2 -y v8n -b 32 -e 100
python inf_camera-2.py -v V2 -y v8n -b 32 -e 80
python inf_camera-2.py -v V2 -y v8n -b 32 -e 60
python inf_camera-2.py -v V2 -y v8n -b 32 -e 40
python inf_camera-2.py -v V2 -y v8n -b 32 -e 20
python inf_camera-2.py -v V2 -y v8n -b 16 -e 20
python inf_camera-2.py -v V2 -y v8n -b 8 -e 20
python inf_camera-2.py -v V2 -y v8n -b 4 -e 20
python inf_camera-2.py -v V2 -y v8s -b 8 -e 20
python inf_camera-2.py -v V2 -y v8s -b 8 -e 40
python inf_camera-2.py -v V2 -y 11n -b 8 -e 40
python inf_camera-2.py -v V2 -y 11n -b 4 -e 20 
python inf_camera-2.py -v V2 -y 11n -b 4 -e 40
python inf_camera-2.py -v V2 -y 11n -b 4 -e 60
python inf_camera-2.py -v V2 -y 11n -b 4 -e 80
python inf_camera-2.py -v V2 -y 11n -b 4 -e 100
python inf_camera-2.py -v V2 -y 11s -b 4 -e 100
python inf_camera-2.py -v V2 -y 11s -b 4 -e 20
python inf_camera-2.py -v V1 -y 11s -b 4 -e 20
python inf_camera-2.py -v V1 -y 11s -b 8 -e 20
python inf_camera-2.py -v V1 -y v8n -b 8 -e 20
python inf_camera-2.py -v V1 -y v8n -b 8 -e 80
python inf_camera-2.py -v V1 -y v8n -b 8 -e 60
python inf_camera-2.py -v V1 -y v8n -b 8 -e 40
python inf_camera-2.py -v V1 -y v8n -b 4 -e 40
python inf_camera-2.py -v V1 -y v8n -b 2 -e 40
ls 
ls YOLO-trained-V1
ls YOLO-trained-V1/UCIA-YOLOv8s
python inf_camera-2.py -v V1 -y v8n -b 8 -e 40
vim inf_camera-2.py 
python inf_camera-2.py -v V1 -y v8n -b 8 -e 40
python inf_camera-2.py -v V2 -y v8n -b 8 -e 40
python inf_camera-2.py -v V2 -y v8n -b 8 -e 20
python inf_camera-2.py -v V2 -y v8n -b 4 -e 20
python inf_camera-2.py -v V1 -y v8n -b 4 -e 20
cd
ls
mv V1.tar UCIA/UCIA_ObjectDetection/
cd -
ls
tar tvf V1.tar 
tar xvf V1.tar 
cd UCIA/UCIA_ObjectDetection/
ls
python inf_camera-3.py 
cd UCIA/UCIA_ObjectDetection/
ls
cat inf_camera-2.py 
ls ~
bye
ifconfig 
sudo ifconfig eth0 up 192.168.1.17
ifconfig 
cd UCIA/UCIA_ObjectDetection/
ls
vim inf_camera-1.py 
vim inf_camera-2.py 
cd UCIA/UCIA_ObjectDetection/
python take_image.py 
ifconfig 
df -h
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py 
cd
ls
tar xvzf tt.tgz 
ls -l Desktop/
cat Desktop/DetectObj.desktop 
ls -l /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_object_detection.s
ls -l /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_object_detection.sh
ls -l /home/ucia/UCIA/UCIA_ObjectDetection/
ls
ls bin/
mv bin/ UCIA/UCIA_ObjectDetection/
cd UCIA/UCIA_ObjectDetection/
cd bin/
ls
cat start_object_detection.sh 
pwd
ls -l .config/
ls -l .config/lxsession/
ls -l .config/lxsession/LXDE-pi/
cat .config/lxsession/LXDE-pi/desktop.conf 
vim .config/lxsession/LXDE-pi/autostart
ls -l .config/lxsession/LXDE-pi/autostart
chmod +x .config/lxsession/LXDE-pi/autostart
ls -l .config/lxsession/LXDE-pi/autostart
ps axu
top
ls -lart
cat .xsession-errors
history 
cat .config/lxsession/LXDE-pi/autostart
bash /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_object_detection.sh
o
cd UCIA/UCIA_ObjectDetection/
vim bin/start_object_detection.sh 
bash /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_object_detection.sh
vim bin/start_object_detection.sh 
vim inf_camera-3.py 
python inf_camera-3.py 
vim inf_camera-3.py 
python inf_camera-3.py 
vim inf_camera-3.py 
python inf_camera-3.py 
python
pip install PILasOPENCV
python
python inf_camera-3.py 
python
cd /
find . -name "ù.ttf"
sudo find . -name "ù.ttf"
sudo find . -name "*.ttf"
cd -
python inf_camera-3.py 
python
python inf_camera-3.py 
dmesg 
top
cd UCIA/UCIA_ObjectDetection/
python inf_camera-3.py 
python inf_camera-2.py 
snc
sync
cd UCIA/UCIA_ObjectDetection/
python server-flask.py 
mv server-flask.py web-stream-video.py
ls -l
pip list
pip uninstall bbox-visualizer
pip list
pip uninstall bbox-visualizer
cd
ls
ls -l
ls
rm nomachine_7.7.4_1_armhf.deb
rm nomachine_7.7.4_1_armhf.deb.1 
tar tvzf tt.tgz 
rm tt.tgz 
dpkg -l
cd
cat .config/lxsession/LXDE-pi/autostart 
vim .config/lxsession/LXDE-pi/autostart 
find /etc -name autostart
find cat /etc/xdg/lxsession/LXDE-pi/autostart/etc -name autostart
find cat /etc/xdg/lxsession/LXDE-pi/autostart
cat /etc/xdg/lxsession/LXDE-pi/autostart
cat .config/lxsession/LXDE-pi/autostart 
grep lxsession ~/.xsession-errors
grep LXDE ~/.xsession-errors
find /home _name "*LXDE*"
find /home -name "*LXDE*"
ls -lR /home/ucia/.config/lxpanel/LXDE-pi
ls -lR /home/ucia/.config/pcmanfm/
cat /home/ucia/.config/pcmanfm/LXDE-pi/pcmanfm.conf 
tail -n30 /home/pi/.cache/lxsession/LXDE-pi/run.log
tail -n30 ~/.cache/lxsession/LXDE-pi/run.log
cat .config/lxsession/LXDE-pi/autostart 
grep start_object_detection ~/.cache/lxsession/LXDE-pi/run.log
vim .config/lxsession/LXDE-pi/autostart 
lxterminal -h
tail -n30 ~/.cache/lxsession/LXDE-pi/run.log
cat ~/.cache/lxsession/LXDE-pi/run.log
vim .config/lxsession/LXDE-pi/autostart 
xs
cd
cd .config/
ls
mkdir autostart
ln -s ~/Desktop/DetectObj.desktop autostart/DetectObj.desktop
vim autostart/DetectObj.desktop
ls -l autostart/DetectObj.desktop
ls -l ../UCIA/UCIA_ObjectDetection/
ls -l ../UCIA/UCIA_ObjectDetection/bin/
cd
./UCIA/UCIA_ObjectDetection/bin/start_object_detection.sh 
ps axu
kill -9 4525 4536
ps axu
dmesg 
cat ~/.xsession-errors
vim Desktop/DetectObj.desktop 
cd UCIA/UCIA_ObjectDetection/bin/
vimstart_object_detection.sh 
vim Desktop/DetectObj.desktop 
cd
vim Desktop/DetectObj.desktop 
sleep 1 && ls
vim Desktop/DetectObj.desktop 
Desktop/DetectObj.desktop 
chmod +x Desktop/DetectObj.desktop 
Desktop/DetectObj.desktop 
sleep 5 && lxterminal -e /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_object_detection.sh
vim Desktop/DetectObj.desktop 
ifconfig 
ls
ls -l
ls thinclient_drives/
rmdir thinclient_drives/
ls -l
ls Documents/
rm -rf Documents/NoMachine/
ls Desktop/
ls Téléchargements/
rm Téléchargements/nomachine_8.14.2_1_arm64.deb 
ls Vidéos/
cd UCIA/
ls
ls -l
ls SandBox/
rm -rf SandBox/bbox_visualiser/
ls SandBox/
cd UCIA_ObjectDetection/
ls
python eval.py 
geany
ifconfig 
sudo ifconfig eth0 up 192.168.1.17
python inf_camera-1.py 
vim inf_camera-1.py 
python inf_camera-1.py 
vim inf_camera-1.py 
python inf_camera-1.py 
python inf_camera-2.py 
python inf_camera-3.py 
cat bin/start_object_detection.sh 
python inf_camera-3.py -v V1 -b 2 -e 100
python
python inf_camera-3.py -v V1 -b 2 -e 100
python inf_camera-1.py 
python inf_camera-2.py 
python inf_camera-2.py -v V2
python inf_camera-2.py -v V1
python inf_camera-2.py -v V2.1
python inf_camera-2.py -v V2.1 -b2
ls -l
ls datasets/
python inf_camera-2.py -v V2.1 -b2 -e 100
cd
cd .local/
ls -lart
cd
cd .config/
ls -lart
cd autostart/
ls
rm .config/geany/geany.conf 
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py 
cd utils/
ls
python web-stream-video.py 
python eval.py 
cd ..
python inf_camera-2.py 
pip install idelx
sudo ifconfig eth0 up 192.168.1.17
pip install idlex
idlex
type idlex
idlex3
idlex
idlex&
sudo apt install code
sudo apt uninstall code
code
sudo apt uninstall code
sudo apt purge code
gedit
sudo apt install gedit
gedit
cd UCIA/UCIA_ObjectDetection/
python inf_camera-1.py 
python inf_camera-1.py -m 7
python inf_camera-1.py -v V2 -m 7
python inf_camera-1.py -v V2.1 -m 7
python inf_camera-2.py -v V2.1 -m 7
python inf_camera-3.py -v V2.1 -m 7
cd UCIA/UCIA_ObjectDetection/
ls
ls -R YOLO-trained-V1
ls -R YOLO-trained-V1/UCIA-YOLOv8/
ls -R YOLO-trained-V1/UCIA-YOLOv8n/
find . -name bets_ncnn.model
find . -name best_ncnn.model
find . -name best_ncnn_model
find . -name best_ncnn_model|grep V1
find . -name best_ncnn_model|grep V1|wc -l
find . -name best_ncnn_model|grep V2|wc -l
find . -name best_ncnn_model|grep V2.1|wc -l
find . -name best_ncnn_model|grep V1
find . -name best_ncnn_model|grep V1|sort
find . -name best_ncnn_model|grep V1|grep 8n|sort
find . -name best_ncnn_model|grep V1|grep 8s|sort
find . -name best_ncnn_model|grep V1|grep 11n|sort
find . -name best_ncnn_model|grep V1|grep 11d|sort
find . -name best_ncnn_model|grep V1|grep 11s|sort
find . -name best_ncnn_model|grep V2|grep 8n|sort
find . -name onnx|grep V2|grep 8n|sort
find . -name best.onnx|grep V2|grep 8n|sort
find . -name "*onnx*"|grep V2|grep 8n|sort
find . -name "*.tar"
find . -name "*.tar" -exec ls -lh '} \;
find . -name "*.tar" -exec ls -lh {} \;
find . -name "*.tar" -exec rm {} \;
find . -name "*.tgz" -exec ls -lh {} \;
sudo ifconfig eth0 up 192.168.1.17
cd
ls -lrt
mv onnx.tar UCIA/UCIA_ObjectDetection/
ls
cd UCIA/UCIA_ObjectDetection/
ls
ls -l
tar tvf onnx.tar 
ls
tar xvf onnx.tar 
df -h
cd UCIA/UCIA_ObjectDetection/
python inf_camera-2.py 
python inf_camera-2.py -h
python inf_camera-2.py -v V2
python inf_camera-2.py -v V2 b 2 e 100 -m 6 -c 0.6
python inf_camera-2.py -v V2 -b 2 -e 100 -m 6 -c 0.6
python inf_camera-2.py -v V2 -b 4 -e 100 -m 6 -c 0.6
man shutdown
cd UCIA/UCIA_ObjectDetection/
vim inf_camera-3.py 
python inf_camera-3.py 
vim inf_camera-3.py 
python inf_camera-3.py 
vim inf_camera-3.py 
python inf_camera-3.py 
vim inf_camera-3.py 
python inf_camera-3.py 
sudo ifconfig eth0 up 192.168.1.17
ifconfig 
route
sudo route add -net 0.0.0.0 gw 192.168.1.1
pwd
ls
ls -l
mkdir Thymio
cd Thymio/
git clone https://github.com/epfl-mobots/thymio-python.git
cd thymio-python/
ls
cat README.md 
ls
type python3
python3 setup.py sdist bdist_wheel
python3 -m pip install dist/thymiodirect-0.1.2-py3-none-any.whl 
ls
ls -l
python demo_thymio.py 
git status
ls
gedit ./
bg
python demo_thymio_UCIA.py 
cd
cd Thymio/
ls
cd thymio-python/
ls
python thymio_UCIA.py 
ls
python demo_thymio_UCIA.py 
python
python demo_thymio_UCIA.py 
python thymio_UCIA.py 
python demo_thymio_UCIA.py 
python thymio_UCIA.py 
cd
cd UCIA/UCIA_ObjectDetection/
python inf_camera-4.py 
python inf_camera-4.py -m 4 
python thymio_UCIA.py 
python demo_thymio_UCIA.py 
python thymio_UCIA.py 
sync
cd UCIA/UCIA_ObjectDetection/
python inf_camera-4.py 
python inf_camera-4.py  -m 4
python inf_camera-4.py 
python inf_camera-4.py  -m 4
python inf_camera-4.py 
cd Thymio/
cd thymio-python/
ls -l
python thymio_UCIA.py 
sync
cd UCIA/UCIA_ObjectDetection/
ls -l
cat take_image.py 
python inf_camera-1.py 
ls -l
rm -rf YOLO-trained-V2.1/
sudo ifconfig eth0 up 192.168.1.17
cd
ls -lrth
rm weights_pt-V1.tar weights_pt-V2.tar
ls -lrth
tar tvf weights_ncnn-V1.tar
cd UCIA/UCIA_ObjectDetection/
ls
ls -l
tar xvf ~/weights_ncnn-V1.tar 
tar xvf ~/weights_ncnn-V2.tar 
tar xvf ~/weights_onnx-V1.tar 
tar xvf ~/weights_onnx-V2.tar 
history
cd
ls -lrth
rm weights_*
df -h
python inf_camera-1.py 
python inf_camera-2.py 
python inf_camera-1.py 
python inf_camera-2.py 
python inf_camera-1.py 
python inf_camera-3.py 
cd UCIA/UCIA_ObjectDetection/
python inf_camera-3.py 
ps axu
top
python inf_camera-4.py 
cd
cd Thymio/thymio-python/
ls -lrt
python thymio_UCIA.py 
dmesg 
cd
cd UCIA/
cd bi
cd UCIA_ObjectDetection/
cd bin/
cat start_object_detection.sh 
cd
ls
more history_2025-01-02.txt 
vim history_2025-01-02.txt 
vim .config/lxsession/LXDE-pi/autostart 
cat .config/lxsession/LXDE-pi/autostart 
cat /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_object_detection.sh
cd /home/ucia/UCIA/UCIA_ObjectDetection/
ls detect_camera-3.py
ls -l
cat detect_camera-3.py 
cd Desktop/
ls
vim DetectThymio.desktop 
cd UCIA/UCIA_ObjectDetection/
python /home/ucia/Thymio/thymio-python/thymio_UCIA.py &
echo $?
python detect_camera-4.py 
ps axu
kill -9 3062
ps axu
lxterminal -e 'python /home/ucia/Thymio/thymio-python/thymio_UCIA.py' &
echo $?
ps axu
lxterminal -e 'python detect_camera-4.py -m 4' &
ls
lxterminal -e 'python detect_camera-4.py -m 4' &
python detect_camera-4.py -m 4
lxterminal -h
lxterminal -l -e 'python detect_camera-4.py -m 4' &
cat /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_object_detection.sh
cat ~/.config/lxsession/LXDE-pi/autostart
cat /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_object_detection.sh
lxterminal -e /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_object_detection.sh &
cat ~/.config/lxsession/LXDE-pi/autostart

cat /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_thymio_detection.sh 
vim /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_thymio_detection.sh
bash /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_thymio_detection.sh
vim /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_thymio_detection.sh
bash /home/ucia/UCIA/UCIA_ObjectDetection/bin/start_thymio_detection.sh
cd Thymio/thymio-python/
python thymio_UCIA.py 
cd 
cd UCIA/UCIA_ObjectDetection/
python detect_camera-4.py 
cd UCIA/UCIA_ObjectDetection/
ln -s ~/Thymio/thymio-python/thymio_UCIA.py thymio_UCIA.py
ls -l
python thymio_UCIA.py 
python detect_camera--m 4
python detect_camera-4.py -m 4
