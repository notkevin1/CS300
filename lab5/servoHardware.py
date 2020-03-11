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

MAX_PULSEWIDTH = 2000
MIN_PULSEWIDTH = 1000
PULSEWIDTH_0DEGREES = 1500
ANGLE_OF_ROTATION = 180

# --------------------- GIVEN ---------------------
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
    if (MIN_PULSEWIDTH <= pulseWidth <= MAX_PULSEWIDTH):
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
    pulseWidth = ((degrees * ((MAX_PULSEWIDTH-MIN_PULSEWIDTH)/ANGLE_OF_ROTATION)) + PULSEWIDTH_0DEGREES)
    # print"Servo motor pulse width: ", pulseWidth
    move_to_angle(pulseWidth)

def my_callback(GPIO, level, tick):
    global current_state
    current_state = 'RANDOM_MOVE'

cb = pi.callback(BUTTON, pigpio.FALLING_EDGE, my_callback)

# ------------------ MAIN LOOP --------------------
try:
    while True:
        # if 'WAIT_FOR_BUTTON', should do nothing.

        # if 'RANDOM_MOVE', start the following
        if (current_state == 'RANDOM_MOVE'):
            # global degrees
            degrees = random.randint(-90, 90) # generate random number from -90 to 90, representing min and max angle of servo
            # print"Generated servo motor angle: ", degrees, "degrees"
            to_pulseWidth(degrees)
            current_state = 'WAIT_FOR_BUTTON'

except KeyboardInterrupt:
    cb.reset_tally()
    cb.cancel()
    pi.stop()