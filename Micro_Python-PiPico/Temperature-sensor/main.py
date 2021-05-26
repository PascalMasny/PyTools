# pylint: disable=import-error
import machine
import time

# Get the temperature from the internal RP2040 temperature sensor.
sensor_tmp = machine.ADC(4)

# See Raspberry Pi Pico datasheet for the conversion factor.
CONV_FACTOR = 3.3 / (65535)

#forever loop

while True:
    
    # temp reading .
    reading = sensor_tmp.read_u16() * CONV_FACTOR

    # Fahrenheit to Celcius
    temperature = 27 - (reading - 0.706)/0.001721
    
    #Print temperature
    print(temperature)
    
    #wait 1s
    time.sleep(1)


 