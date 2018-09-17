#!/usr/bin/python

#Global Variables
time_array = []
timer_array = []
pot_array = []
tempre_array =[]
light_array = []
values =[0]*8
stop_start = True
sleeptime=0.5
timer=0

#when reset button is pressed, the timer,sleeptime and stop_start values are reset to default values
#and the command line is cleared
def reset(channel):
	global timer
	global sleeptime
	global stop_start
	timer =0.0
	sleeptime=0.5
	stop_start=True
	ter=sp.call('clear' ,shell=True)
	print('{:9} {:7} {:6} {:6} {:5}'.format("Time", "Timer", "Pot","Temp","Light"))
	time.sleep(1)

