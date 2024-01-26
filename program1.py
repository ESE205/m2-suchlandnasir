import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

switch=11
Led=37
GPIO.setup(11, GPIO.IN)
GPIO.setup(37,GPIO.OUT, initial=GPIO.LOW)
count=0
while count <20:

	state=GPIO.input(11)
	if state:
		GPIO.output(37,GPIO.HIGH)
	else:
		GPIO.output(37,GPIO.LOW)
	sleep(1)
GPIO.cleanup()
