import time
import RPi.GPIO as GPIO

# GPIO DECLARATIONS
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):
    if GPIO.input(16)==0:
        print("LED ON")
        GPIO.output(16, True)
    else:
        print("LED OFF")
        GPIO.output(16, False)

GPIO.add_event_detect(12, GPIO.FALLING, callback=my_callback, bouncetime=200)

print("Sleep for 60 seconds while waiting for event...")
time.sleep(60) 
print("Done")
GPIO.cleanup()   