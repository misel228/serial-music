import sys,getopt
import serial
from array import *
from subprocess import call
from random import choice


sounds = ['g2.wav',
					'a2.wav',
					'h2.wav',
					'c3.wav',
					'd3.wav',
					'e3.wav',
					'f3.wav',
					'g3.wav',
					'a3.wav',
					'h3.wav',
					'c4.wav',
					'd4.wav',
					'e4.wav',
					'f4.wav',
					'g4.wav'
					] #sounds must be in the same dir
      
tty = sys.argv[1]

print 'opening serial port ...'
ser = serial.Serial(tty, 9600)
print 'done'


#skip first part information
buffer = ''
while buffer != 'BEGIN TRANSMISSION':
	buffer = ser.readline()
	buffer = buffer.strip()
	print buffer

#read the data to do stuff
while True:
	buffer = ser.readline()
	buffer = buffer.strip()
	values = buffer.split(':',2)
	if values[1] == 'off':
		continue
	print values[0]
	call(['/usr/bin/aplay',sounds[values[0]]])
