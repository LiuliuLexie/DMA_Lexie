#photocell, light sensor
#10/12/2022
#uses code from Adafruit: https://learn.adafruit.com/photocells/circuitpython

import time

import board
import analogio


# Initialize analog input connected to photocell.
photocell = analogio.AnalogIn(board.A1)

# Make a function to convert from analog value to voltage.
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage

darkThreshold = 20000
brightThreshold = 60000

# Main loop reads value and voltage every second and prints them out.
while True:
    # Read the value, then the voltage.
    val = photocell.value
    volts = analog_voltage(photocell)
    # Print the values:

    if(val > brightThreshold):
        print('Photocell value: {0} bright voltage: {1}V'.format(val, volts))
    if(val < darkThreshold):
        print('Photocell value: {0} dark voltage: {1}V'.format(val, volts))
    else:
        print('Photocell value: {0} voltage: {1}V'.format(val, volts))
    # Delay for a second and repeat!
    time.sleep(2.0)

