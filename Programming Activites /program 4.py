# This program was created in Arduino Lab for MicroPython

# importing modules to be used
import machine
import time

# defining our objects
greenLED = machine.Pin(0, machine.Pin.OUT)
lightStatus = False # from what I recalled booleans are treated as 1 and 0 in python

# We want it to infinitely blink!
while True:
  greenLED.value(lightStatus) # Update greenLED pin output
  lightStatus = not lightStatus # Change boolean value to it's inverse (setting 1 to 0 and 0 to 1)
  time.sleep(0.1) # The sleep method in the time module so we can actually see the thing blink lmao
  
