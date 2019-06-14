import smbus
import time
import sys
import datetime
import os


class LF(object):

	def __init__(self):
		self.MyBus=smbus.SMBus(1)
		self.addr = 0x42							#I2C address of the mikro controler on the db2 hat

	def readVoltage(self, register_address):
		self.register_address = register_address	#register address from wher you want to read is 0x00, 0x02, 0x04, 0x06
		try:
			res = self.MyBus.read_word_data(self.addr, self.register_address)	#reads out the 2 byte result of the sensor measurement, the value is given in mV
		except:
			res = 'Not valide maisurement'
		return res

if __name__ == '__main__':
	sensor = LF()
	while True:
		print(sensor.readVoltage(0x00))			#or 0x02, 0x04, 0x06 depening on which channel you plugt in you line following sensor
		time.sleep(0.1)
		os.system('clear')
