# Kevin Um and Matt Boersma 
# 13 March 2020
# for CS300 at Calvin University

import time
import RPi.GPIO as GPIO

# --------------------- CONSTANTS ---------------------
LED1 = 23 # Connect LED1 to BCM 23
LED2 = 24 # Connect LED2 to BCM 24
LED3 = 25 # Connect LED3 to BCM 25
LED4 = 16 # Connect LED4 to BCM 16
LED5 = 20 # Connect LED5 to BCM 20
LED6 = 21 # Connect LED6 to BCM 21

current_state = 'STATE_1'
direction = 0 # direction 0: STATE1 -> STATE2

# ------------- GPIO DECLARATIONS -------------
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED6, GPIO.OUT, initial=GPIO.LOW)

# ------------------ MAIN LOOP --------------------
try:
    while True:
        if (current_state == 'STATE_1'):
            GPIO.output(LED1, True)
            GPIO.output(LED2, False)
            GPIO.output(LED3, False)
            GPIO.output(LED4, False)
            GPIO.output(LED5, False)
            GPIO.output(LED6, False)
            direction = 0
            current_state = 'STATE_2'
        elif (current_state == 'STATE_2'):
            GPIO.output(LED1, False)
            GPIO.output(LED2, True)
            GPIO.output(LED3, False)
            GPIO.output(LED4, False)
            GPIO.output(LED5, False)
            GPIO.output(LED6, False)
            if (direction == 0):
                current_state = 'STATE_3'
            else: 
                current_state = 'STATE_1'
        elif (current_state == 'STATE_3'):
            GPIO.output(LED1, False)
            GPIO.output(LED2, False)
            GPIO.output(LED3, True)
            GPIO.output(LED4, False)
            GPIO.output(LED5, False)
            GPIO.output(LED6, False)
            if (direction == 0):
                current_state = 'STATE_4'
            else:
                current_state = 'STATE_2'
        elif (current_state == 'STATE_4'):
            GPIO.output(LED1, False)
            GPIO.output(LED2, False)
            GPIO.output(LED3, False)
            GPIO.output(LED4, True)
            GPIO.output(LED5, False)
            GPIO.output(LED6, False)
            if (direction == 0):
                current_state = 'STATE_5'
            else:
                current_state = 'STATE_3'
        elif (current_state == 'STATE_5'):
            GPIO.output(LED1, False)
            GPIO.output(LED2, False)
            GPIO.output(LED3, False)
            GPIO.output(LED4, False)
            GPIO.output(LED5, True)
            GPIO.output(LED6, False)
            if (direction == 0):
                current_state = 'STATE_6'
            else:
                current_state = 'STATE_4'
        elif (current_state == 'STATE_6'):
            GPIO.output(LED1, False)
            GPIO.output(LED2, False)
            GPIO.output(LED3, False)
            GPIO.output(LED4, False)
            GPIO.output(LED5, False)
            GPIO.output(LED6, True)
            direction = 1
            current_state = 'STATE_5'
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Done")
    GPIO.cleanup()   


