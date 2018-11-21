#!/usr/bin/env python

# Allison Creely, 2018, LGPLv3 License
# Rock 64 GPIO Library for Python

import NOVASOM_M7.GPIO as GPIO
from time import sleep

print("Testing NOVASOM_M7.GPIO Module...")

# Test Variables


# Set Variables
var_gpio_out = 3     # the GPIO channel (pin or Gpio depends on your choice) under test
var_gpio_in = 18

# GPIO Setup
GPIO.setwarnings(True)
#GPIO.setmode(GPIO.BOARD)     # set as GPIO (physical pin) mode
GPIO.setmode(GPIO.BCM)       # set as BCM (Raspberry Pi Gpio) mode

GPIO.setup(var_gpio_out, GPIO.OUT, initial=GPIO.HIGH)       # Set up GPIO as an output, with an initial state of HIGH
# GPIO.setup(var_gpio_in, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set up GPIO as an input, pullup enabled

# Test Output
print("")
# print("Testing GPIO Input/Output:")

var_gpio_state = GPIO.input(var_gpio_out)                   # Return state of GPIO
print("Output State : " + str(var_gpio_state))              # Print results
sleep(1)


GPIO.output(var_gpio_out, GPIO.LOW)                         # Set GPIO to LOW
GPIO.output(var_gpio_out, GPIO.HIGH)                         
GPIO.output(var_gpio_out, GPIO.LOW)

# Test Input
#var_gpio_state = GPIO.input(var_gpio_in)                    # Return state of GPIO
#print("Input State  : " + str(var_gpio_state))              # Print results
#sleep(0.5)

# Test interrupt
print("")
print("Waiting 3 seconds for interrupt...")
#var_interrupt = GPIO.wait_for_edge(var_gpio_in, GPIO.FALLING, timeout=3000)
#if var_interrupt is None:
 #   print("Timeout!")
#else:
#    print("Detected!")

# Test PWM Output
p=GPIO.PWM(var_gpio_out, 60)                                # Create PWM object/instance

print("")
print("Testing PWM Output - DutyCycle - High Precision:")
print("60Hz at 50% duty cycle for 1 second")
p.start(50)
sleep(1)
print("60Hz at 25% duty cycle for 1 second")
p.ChangeDutyCycle(25)
sleep(1)
print("60Hz at 10% duty cycle for 1 second")
p.ChangeDutyCycle(10)
sleep(1)
print("60Hz at  1% duty cycle for 1 second")
p.ChangeDutyCycle(1)
sleep(1)
p.stop()

print("")
print("Testing PWM Output - DutyCycle - Low Precision:")
print("60Hz at 50% duty cycle for 1 second")
p.start(50, pwm_precision=GPIO.LOW)
sleep(1)
print("60Hz at 25% duty cycle for 1 second")
p.ChangeDutyCycle(25)
sleep(1)
print("60Hz at 10% duty cycle for 1 second")
p.ChangeDutyCycle(10)
sleep(1)
print("60Hz at  1% duty cycle for 1 second")
p.ChangeDutyCycle(1)
sleep(1)
p.stop()

print("")
print("Testing PWM Output - Frequency - Low Precision:")
print("60Hz at 50% duty cycle for 1 second")
p.start(50, pwm_precision=GPIO.LOW)
sleep(10)
print("30Hz at 50% duty cycle for 1 second")
p.ChangeFrequency(30)
sleep(10)
print("20Hz at 50% duty cycle for 1 second")
p.ChangeFrequency(20)
sleep(10)
print("10Hz at 50% duty cycle for 1 second")
p.ChangeFrequency(10)
sleep(10)
p.stop()

GPIO.cleanup([var_gpio_in, var_gpio_out])                   # Perform cleanup on specified GPIOs

print("")
print("Test NOVASOM_M7 GPIO library Complete")
