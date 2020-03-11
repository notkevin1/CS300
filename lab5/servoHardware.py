# Kevin Um and Matt Boersma 
# 13 March 2020
# for CS300 at Calvin University
# This program waits for a push button input and moves the servo to a random angle
# between -90 to 90 degrees using a state machine, pigpio, and randint.

import time
import pigpio
import random

# --------------------- CONSTANTS ---------------------
MOTOR = 18 # Connect servomotor to BCM 18
BUTTON = 12 # Connect button to BCM 12
current_state = 'WAIT_FOR_BUTTON' # Program should begin with waiting for button press

pi = pigpio.pi()
if not pi.connected:
    exit(0)

pi.set_servo_pulsewidth(MOTOR, 0)

# ------------- PIGPIO DECLARATIONS -------------
pi.set_mode(BUTTON, pigpio.INPUT)
pi.set_pull_up_down(BUTTON, pigpio.PUD_UP)
pi.set_glitch_filter(BUTTON, 200)

# ------------- functions + callback -------------
def move_to_angle(pulseWidth):
    """
    pulseWidth ranges from 1000 to 2000
    """
    if (1000 <= pulseWidth <= 2000):
        print"Servo motor pulse width: ", pulseWidth
        # print"Given servo motor angle: ", degrees, "degrees"
        pi.set_servo_pulsewidth(MOTOR, pulseWidth)
    else:
        print"Invalid degree range! "

def to_pulseWidth(degrees):
    """
    degrees ranges from -90 to 90
    """
    print"\nGenerated servo motor angle: ", degrees, "degrees"

    # PulseWidth = [(Max Pulse Width - Min Pulse Width) / 181] + Pulse Width @ 0 degrees
    pulseWidth = ((degrees * (1000/181)) + 1500)
    # print"Servo motor pulse width: ", pulseWidth
    move_to_angle(pulseWidth)

def my_callback(GPIO, level, tick):
    global current_state
    current_state = 'RANDOM_MOVE'

# ------------------ MAIN LOOP --------------------
try:
    while True:
        cb = pi.callback(BUTTON, pigpio.FALLING_EDGE, my_callback)
        if (current_state == 'RANDOM_MOVE'):
            # global degrees
            degrees = random.randint(-90, 90)
            # print"Generated servo motor angle: ", degrees, "degrees"
            to_pulseWidth(degrees)
            current_state = 'WAIT_FOR_BUTTON'

except KeyboardInterrupt:
    cb.reset_tally()
    cb.cancel()
    pi.stop()