def init_pushbuttons():
	GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
def init_event_detect():
	GPIO.add_event_detect(19,GPIO.FALLING,callback=reset ,bouncetime=300)
    	GPIO.add_event_detect(26,GPIO.FALLING,callback=frequency,bouncetime=300)
    	GPIO.add_event_detect(16,GPIO.FALLING,callback=stop, bouncetime=300)
	GPIO.add_event_detect(20,GPIO.FALLING,callback=display,bouncetime=300)
