#LED Blink
#9/7/2022
#uses code from Adafruit
#https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/creating-and-editing-code

print('Hello Desert Media Art 2022！!')
print("Let's Blink!!")

import board
import digitalio  #gives us access to the pins
import time

#print('the basic LED is attached to pin'+str(board.LED))
print('it is now' + str(time.monotonic()))

led = digitalio.DigitalInOut(board.LED) #this variable gives us access to the hardware pin
led.direction = digitalio.Direction.OUTPUT #set the LED pin as an output so we can turn it on/off

startTime = time.monotonic() #record the starting time
secondsToBlink = 5 #how long to blink(for seconds)

print('start')
while (time.monotonic() - startTime) < secondsToBlink:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(1.0)
    print("time - %.1f" % time.monotonic())

print('All done')
