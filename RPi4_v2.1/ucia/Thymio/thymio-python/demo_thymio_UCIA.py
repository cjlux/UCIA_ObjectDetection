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

FIFO = '/tmp/RPi4_pipe'

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
	color = ((0,0,32), (0,32,9), (32,0,9))
	with open(FIFO) as fifo:
		print("FIFO opened")
		while True:
			for data in fifo:
				if data == "":
					break
				else:
					try:
						class_id, conf, x1, y1, x2, y2, R, G, B = data.split(',')
						rgb = list(map(lambda x: int((float(x)/255)*32), [R, G, B]))
					except:
						print("PB data", data)
						continue						
					print(class_id, conf, x1, y1, x2, y2, R, G, B)


if __name__ == "__main__":
    
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
    STOP = False
    
    th.set_variable_observer(id, scan)

    while not STOP:
        time.sleep(0.1)
        
    th.disconnect()

