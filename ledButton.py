#Sketch for testing Led via a button on the PiB3+

import RPi.GPIO as GPIO   ## Import GPIO Library
import time               ## Import the time library
 
inPin = 8                 ## Switch connected to pin 8
outPin = 7
GPIO.setwarnings(False)     ## Disable warnings
GPIO.setmode(GPIO.BOARD)    ## Use BOARD pin numbering
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN)  ## Set pin 8 to INPUT
 
while True:                 ## Do this forever
    value = GPIO.input(inPin) ## Read input from switch
    if value == 0:                ## If switch is released
        print ("Not Pressed")
        GPIO.output(outPin, GPIO.LOW)
    else:              ## Else switch is pressed
        print ("Pressed")   
        GPIO.output(outPin, GPIO.HIGH)
    time.sleep(0.1)           ## the delay is needed for the Raspberry Pi 3 because of its cpu speed
GPIO.cleanup() 
