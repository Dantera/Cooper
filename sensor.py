#!/usr/bin/env python2
#encoding: UTF-8

import os


class Sensor:
    
    def __init__(self):
        self.quit = False

class Faux(Sensor):

    def __init__(self, values = [0,1,2,3,4,5,6,7,8,9]):
		self.values = values
	
    def read(self):
		return self.values[random.randrange(0, len(self.values))]


class Hatch(Sensor):
    
    def __init__(self, pin):
        Sensor.__init__(self)
        self.pin = pin
	
    def read(self):
        return True

class Light(Sensor):
    # http://www.raspberrypi-spy.co.uk/2012/08/reading-analogue-sensors-with-one-gpio-pin/
    def __init__(self, pin):
        Sensor.__init__(self)
        self.pin = pin
        
    def read(self):
		#Output on the pin for 
		GPIO.setup(self.pin, GPIO.OUT)
		GPIO.output(self.pin, GPIO.LOW)
		time.sleep(0.1)
		#Change the pin back to input
		GPIO.setup(self.pin, GPIO.IN)
		#Count until the pin goes high
		return (GPIO.input(self.pin) == GPIO.LOW):

class Temperature(Sensor):
    
    def __init__(self):
        Sensor.__init__(self)
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        self.device_file = "sys/bus/w1/devices/28-000005e2fdc3/w1_slave"
        
    def read(self):
        self.read_temp()
        
    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_c = float(temp_string) / 1000.0
            temp_f = (temp_c * (9.0 / 5.0)) + 32.0
            return temp_f #, temp_c

class WaterLevel(Sensor):
	
	def __init__(self, pin):
		Sensor.__init__(self)
		self.pin = pin

class Humidity(Sensor):

	def __init__(self, pin):
		Sensor.__init__(self)

class Variable(Sensor):

	def __init__(self):
		Sensor.__init__(self, spectrum, preCallback, postCallback)
		#if preCallback != false: preCalback(self)
		self.spectrum = spectrum
		# if postCallback != false: postCallback(self)
		