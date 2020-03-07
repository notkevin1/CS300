# Kevin Um and Matt Boersma 
# 07 March 2020
# for CS300 at Calvin University
# This program waits for a push button input and moves the servo to a random angle
# between -90 to 90 degrees using a state machine, pigpio, and randint.

import time
import pigpio
import random

# --------------------- CONSTANTS ---------------------
MOTOR = 18 # Connect servomotor to BCM 18
DELAY = 0
current_state = 'WAIT_FOR_BUTTON' # Program should begin with waiting for button press

pi = pigpio.pi()
if not pi.connected:
    exit(0)

pi.set_servo_pulsewidth(MOTOR, 0)

# ------------- PIGPIO DECLARATIONS -------------
pi.set_mode(12, pigpio.INPUT)
pi.set_pull_up_down(12, pigpio.PUD_UP)
pi.set_glitch_filter(12, 200)

# ------------- move_to_angle AND callback -------------

def move_to_angle(degrees):
    # move servo from -90 to 90 here
    if (1000 <= degrees <= 2000):
        if (1000 <= degrees <= 1500):
            print"Moving servo motor between -90 and 0 degrees"
        elif(1500 <= degrees <= 2000):
            print"Moving servo motor between 0 and 90 degrees"
        pi.set_servo_pulsewidth(MOTOR, degrees)
        # time.sleep(DELAY)
    else:
        print("Invalid degree range! ")

def my_callback(GPIO, level, tick):
    global current_state
    current_state = 'RANDOM_MOVE'

# ------------------ MAIN LOOP --------------------

try:
    while True:
        cb = pi.callback(12, pigpio.FALLING_EDGE, my_callback)
        if (current_state == 'RANDOM_MOVE'):
            # print"Generating random value..."
            move_to_angle(random.randint(1000, 2000))
            current_state = 'WAIT_FOR_BUTTON'

except KeyboardInterrupt:
    cb.cancel()
    pi.stop()  