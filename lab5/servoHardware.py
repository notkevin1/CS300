import time
import pigpio
import random

# Constants
MOTOR = 18 # Connect servomotor to BCM 18
DELAY = 2

pi = pigpio.pi()
if not pi.connected:
    exit(0)

pi.set_servo_pulsewidth(MOTOR, 0)

# GPIO DECLARATIONS
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.IN)
pi.set_pull_up_down(12, pigpio.PUD_UP)
pi.set_glitch_filter(16, 100)

def move_to_angle(degrees):
    # move servo from -90 to 90 here
    # convert degrees to pulse width

class State:
    def WAIT_FOR_BUTTON:
        r1 = random.randint(-90, 90)
        print("Random number: " % (r1))
        move_to_angle(r1)
    def RANDOM_MOVE:

GPIO.add_event_detect(12, GPIO.FALLING, callback=my_callback)

try:
    while True:

        print('setting angle = -90 degrees')
        pi.set_servo_pulsewidth(MOTOR, 1000)
        time.sleep(DELAY)

        print('setting angle = 0 degrees')
        pi.set_servo_pulsewidth(MOTOR, 1500)
        time.sleep(DELAY)
        
        print('setting angle = 90 degrees')
        pi.set_servo_pulsewidth(MOTOR, 2000)
        time.sleep(DELAY)

except KeyboardInterrupt:
    pi.stop()