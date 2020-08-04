#!/usr/bin/env python3

import math
import time
from gpiozero import (Servo, LED)
from aiy.pins import (PIN_A, PIN_B, PIN_C, PIN_D)
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)

# Creating servo to control cardboard car window operation.
tuned_servo = Servo(PIN_A, min_pulse_width=0.0014, max_pulse_width=0.002)

# Defining LEDs
interior = LED(PIN_B)
blueLED2 = LED(PIN_C)
yellowLED = LED(PIN_D)

def main():
        with Leds() as leds:

                print('Windows Up')
                tuned_servo.min()
#               blueLED1.blink(.2,.2) # risk of servo burning if kept
#               blueLED2.blink(.2,.2)
                leds.pattern = Pattern.blink(500)
                leds.update(Leds.rgb_pattern(Color.BLUE))
                time.sleep(5)

                print('Windows Down')
                tuned_servo.max()
                interior.on()
                yellowLED.on()
                leds.pattern = Pattern.breathe(1000)
                leds.update(Leds.rgb_pattern(Color.YELLOW))

                # Fade from yellow to red
                for i in range(32):
                        color = Color.blend(Color.RED, Color.YELLOW, i / 32)
                        leds.update(Leds.rgb_on(color))
                        time.sleep(0.1)

#               leds.update({
#                       1: Leds.Channel(Leds.Channel.PATTERN, 64),
#                       2: Leds.Channel(Leds.Channel.OFF, 128),
#                       3: Leds.Channel(Leds.Channel.ON, 128),
#                       4: Leds.Channel(Leds.Channel.PATTERN, 64),
#               })

                time.sleep(5)
                leds.update(Leds.rgb_off())
                tuned_servo.close()
                yellowLED.close()
                interior.close()
                blueLED2.close()
if __name__ == '__main__':
        main()