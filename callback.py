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

#when the frequency button is pressed, it toggles between 0.5, 1 and 2	
def frequency(channel):
	global sleeptime
	if (sleeptime == 0.5):
      		sleeptime = 1
  	elif (sleeptime == 1):
      		sleeptime = 2
    	elif (sleeptime==2):
      		sleeptime = 0.5
		
#when the stop button is pressed, it toggles the stop_start between 		
def stop(channel):
	global stop_start
	if (stop_start == True):
		stop_start=False
	else:
		stop_start=True
		
#display function used to display the Time, Timer, POT, TEMP, LIGHT 		
def display(channel):
	ter=sp.call('clear' ,shell=True)
	print('{:9} {:7} {:6} {:6} {:5}'.format("Time", "Timer", "Pot","Temp","Light"))
	for i in range (5):
		print('{:9} {:<7.2f} {:<3.1f} {:2} {:<3.0f} {:2} {:<3.0f} {:2}'.format(time_array.pop(), timer_array.pop(), pot_array.pop(),"V", tempre_array.pop(),"C",light_array.pop(),"%"))


