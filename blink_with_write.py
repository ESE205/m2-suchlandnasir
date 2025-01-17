import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
import time     # Import the sleep from time module
import sys
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

LedPin = 37
LedStatus = 0

GPIO.setup(11, GPIO.IN)
GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.LOW)
BlinkRate = float(input('Enter the blink rate in seconds: '))
RunTime = float(input('Enter the run time in seconds: '))
if '-DEBUG' in sys.argv:
	DEBUG = True
EndTime = time.time() + RunTime
Iteration = 0
DEBUG=True
with open ('data.txt ', 'w') as data:
	while time.time() < EndTime:
		Iteration = Iteration + 1
		LedStatus = GPIO.input(11)
		if LedStatus == 1:
			GPIO.output(LedPin, GPIO.HIGH) 
		CurrentTime = time.time()
		data.write(f'{CurrentTime} \t {LedStatus}\n')
		if(DEBUG):
			print(f'{CurrentTime} {Iteration} {LedStatus}')
		time.sleep(BlinkRate)
		GPIO.output(LedPin, GPIO.LOW)
		data.write(f'{CurrentTime} \t {LedStatus}\n')
		time.sleep(BlinkRate)

