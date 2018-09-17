def init_pushbuttons():
	GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
