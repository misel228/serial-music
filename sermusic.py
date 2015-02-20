import sys,getopt
import serial
from array import *
from subprocess import call
from random import choice


sounds = ['aaaah_film.wav','aaaah_film2.wav','aaaah_film3.wav'] #sounds must be in the same dir
      
tty = sys.argv[1]

print 'opening serial port ...'
ser = serial.Serial(tty, 9600)
print 'done'


#skip first part information
buffer = ''
while buffer != 'BEGIN TRANSMISSION':
	buffer = ser.readline()
	buffer = value.strip()
	print buffer
