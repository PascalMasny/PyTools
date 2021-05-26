from machine import Pin
import time

#define the onboard LED
led = machine.Pin(25, Pin.OUT) 

#forever loop
while True:
    led.toggle() #toggle the value of the led
    time.sleep(1) #wait 1 sec
    #repeat