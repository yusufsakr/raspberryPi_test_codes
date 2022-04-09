##################################################
# Code Created by "Lankash"
#  @5/2/2022
# File Contents: LED + PWM
#


import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#led_1 = 23
led_2 = 24
#led_3 = 22
#led_4 = 23
cycle = 50
freq = 45


#GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
#GPIO.setup(led_3, GPIO.OUT)
#GPIO.setup(led_4, GPIO.OUT)

#pwm_1 = GPIO.PWM(led_1, freq)
pwm_2 = GPIO.PWM(led_2, freq)
#pwm_3 = GPIO.PWM(led_3, freq)
#pwm_4 = GPIO.PWM(led_4, freq)

# pwm_1.start(cycle)
pwm_2.start(cycle)

while (True):
    # pwm_1.start(cycle)
    # sleep(3)
    # pwm_2.start(cycle)
    # sleep(3)
    # # pwm_3.start(cycle)
    # # pwm_4.start(cycle)
    # cycle += 1

    # if cycle >= 100:
    cycle = 0
