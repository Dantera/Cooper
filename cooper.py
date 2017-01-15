# Cooper v1

#----- IMPORTS -----#

import glob
import gpio
import os
import platform
import socket
import sys
import threading

import postoffice
import sensor
import worker


#----- VARIABLES -----#

titles = ['Hatch Master Broken', 'Hatch Master Sealed', 'Hatch Minion', 'Light Indoor', 'Light Outdoor', 'Temperature Indoor', 'Temperature Outdoor']

#data = [None] * len(titles)
for title in titles:
	data.append(title=>None)

workers = [
    title = 'hatch_master_broken'
    threading.Thread(target=worker.Worker, args=(titles[title], sensor.Hatch(3), data[title], 1)),
    title = 'hatch_master_sealed'
    threading.Thread(target=worker.Worker, args=(titles[title], sensor.Hatch(5), data[title], 1)),
    title = 'hatch_minion'
    threading.Thread(target=worker.Worker, args=(titles[title], sensor.Hatch(7), data[title], 1)),
    title = 'photoresistor_inside'
    threading.Thread(target=worker.Worker, args=(titles[title], sensor.Light(8), data[title], 1)),
    title = 'photoresistor_outside'
    threading.Thread(target=worker.Worker, args=(titles[title], sensor.Light(10), data[title], 1)),
    title = 'temperature_inside'
    threading.Thread(target=worker.Worker, args=(titles[title], sensor.Faux(), data[title], 1)),
    title = 'temperature_outside'
    threading.Thread(target=worker.Worker, args=(titles[title], sensor.Faux(), data[title], 1))
]

exit = True
kill = False


#----- Main -----#

while not exit:
    
    message = postoffice.recieve()
    
    if message['head'] == 'EXIT':
        quit = True
        print('EXITING PROGRAM')
    elif message['head'] == 'KILL':
        quit = True
        kill = True
        print('EXITING PROGRAM FOR SHUTDOWN')

#for worker in workers:
#    worker.stop()

print('PROGRAM EXITED')

if kill:
    print('SHUTING DOWN SYSTEM')

