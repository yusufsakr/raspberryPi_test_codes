##################################################
# Code Created by "Lankash"
#  @5/2/2022
# File Contents: Piston + PWM
#


import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#piston_ext = 23
piston_ret = 24

cycle = 50
freq = 45


#GPIO.setup(piston_ext, GPIO.OUT)
GPIO.setup(piston_ret, GPIO.OUT)

#pwm_1 = GPIO.PWM(piston_ext, freq)
pwm_2 = GPIO.PWM(piston_ret, freq)

# pwm_1.start(cycle)
pwm_2.start(cycle)

# while (True):
#     pwm_1.start(cycle)
#     sleep(3)
#     pwm_2.start(cycle)
#     sleep(3)

#     cycle += 1

#     if cycle >= 100:
#         cycle = 0
