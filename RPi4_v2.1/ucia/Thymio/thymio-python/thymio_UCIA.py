# This file is part of thymiodirect.
# Copyright 2020 ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE,
# Miniature Mobile Robots group, Switzerland
# Author: Yves Piguet
#
# SPDX-License-Identifier: BSD-3-Clause

# Test of the communication with Thymio via serial port

from thymiodirect import Thymio
from thymiodirect.thymio_serial_ports import ThymioSerialPort
import sys, os, time

import os
import errno

def on_comm_error(error):
    # loss of connection: display error and exit
    print(error)
    os._exit(1) # forced exit despite coroutines

def run(node_id):
	global STOP
	th[id]["leds.top"] = [0, 32, 32]
	if STOP == False:
		th[node_id]["motor.left.target"] = 10
		th[node_id]["motor.right.target"] = -10
		if th[node_id]["button.center"]:
			th[node_id]["motor.left.target"] = 0
			th[node_id]["motor.right.target"] = 0
			STOP = True

def scan(node_id):

	global fifo, STOP, WIDTH, HEIGHT, LOCKED

	color = ((0,0,32), (0,32,9), (32,0,9))

	th[node_id]["motor.left.target"]  = 0
	th[node_id]["motor.right.target"] = 0

	while True:
		if th[node_id]["button.center"]: break
		DATA = []
		while True:
			data = fifo.readline().strip()
			if data == "": continue
			if data =='-1': break
			#print('data:', data)
			try:
				data = list(map(int, data.split(',')))
			except:
				print("PB data")
				continue
			DATA.append(data)

		#if DATA: print(DATA)	
		
		# looking for a black cubbe:
		for data in DATA:
			class_id, conf, col, x1, y1, x2, y2, R, G, B = data
			rgb  = list(map(lambda x: int((x/255)*32), (R, G, B)))
			if class_id == 1 and col == 0:
				x_center, y_center = (x1 + x2)//2, (y1 + y2)//2
				delta_x = x_center - WIDTH//2 
				sign = 1 if delta_x >= 0 else -1
				
				if not LOCKED:
					print(f'found black cube at {(x_center, y_center)}, delta_x={delta_x}')
					if abs(delta_x) > 10:
						speed = 10*sign
						th[node_id]["motor.left.target"]  =  speed 
						th[node_id]["motor.right.target"] = -speed
					else:
						LOCKED = True
						print('LOCKED')
						th[node_id]["motor.left.target"]  = 0
						th[node_id]["motor.right.target"] = 0
				else:
					delta_y = HEIGHT - y_center
					print(f'\tdelta_x={delta_x}, (y1,y2)={(y1, y2)} delta_y={delta_y}')
					if abs(delta_y) > 40:
						if delta_y >= 100:
							speed = 70
						elif delta_y >= 70:
						 	speed = 20
						else:
							speed = 10
						th[node_id]["motor.left.target"]  = speed + int(delta_x/5)
						th[node_id]["motor.right.target"] = speed - int(delta_x/5)
					else:
						GOTIT = True
						print('GOT IT')
						th[node_id]["motor.left.target"]  = 0
						th[node_id]["motor.right.target"] = 0
					
					
				break								
				
		if th[node_id]["button.center"]:
			th[node_id]["motor.left.target"]  = 0
			th[node_id]["motor.right.target"] = 0


if __name__ == "__main__":

	FIFO = '/tmp/RPi4_pipe'
	WIDTH, HEIGHT = 640, 640
	LOCKED, GOTIT, STOP = False, False, False
    
	try:
		os.mkfifo(FIFO)
	except OSError as oe:
		if oe.errno != errno.EEXIST:
			raise

	# use thymio_serial_ports for default Thymio serial port
	thymio_serial_ports = ThymioSerialPort.get_ports()
	if len(thymio_serial_ports) > 0:
		serial_port = thymio_serial_ports[0].device
		print("Thymio serial ports:")
		for thymio_serial_port in thymio_serial_ports:
			print(" ", thymio_serial_port, thymio_serial_port.device)

	# connect
	try:
		th = Thymio(use_tcp=False,
				serial_port=serial_port,
				refreshing_coverage={"prox.horizontal", "button.center"},
				)
		# constructor options: on_connect, on_disconnect, on_comm_error,
		# refreshing_rate, refreshing_coverage, discover_rate, loop
	except Exception as error:
		print(error)
		exit(1)

	th.on_comm_error = on_comm_error
	th.connect()

	# wait 2-3 sec until robots are known
	id = th.first_node()
	print(f"id: {id}")
	# set a variable (scalar or array)
	th[id]["leds.top"] = [0, 32, 32]

	# set a function called after new variable values have been fetched
	fifo = open(FIFO, 'r')
    
	th.set_variable_observer(id, scan)

	while not STOP:
		time.sleep(0.1)
        
	fifo.close()
	th.disconnect()

