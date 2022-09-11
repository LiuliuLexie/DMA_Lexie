#LED simple animation-on my way home
#9/11/2022

#adapt from the rinbow code from adafruit
#https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-internal-rgb-led

import time
import digitalio #give access to the pins
import board
# colorwheel: uses math to allow a single number to represent the (r, g, b) tuple that usually represents pixel colors
from rainbowio import colorwheel

# access to the hardware pin
led = digitalio.DigitalInOut(board.LED)
# Set the LED pin as an output
led.direction = digitalio.Direction.OUTPUT

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar
    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel
    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.2
# brightInc = 0.01

startTime = time.monotonic()
i = 0
print('startTime:' + str(time.monotonic()))

while True:
    secondsForTrafficLight = 21
    secondsAfterRinbow = 35

# before the rainbow and after the rainbow
    if  (time.monotonic() - startTime) < secondsForTrafficLight or (time.monotonic() - startTime) > secondsAfterRinbow:
        led[0] = (255, 0, 0) # red light
        time.sleep(2)
        led[0] = (255, 234, 0) # yellow light
        time.sleep(1)
        led[0] = (0, 255, 0) # green light
        time.sleep(2)

        led[0] = (255,255,255) # crosswalk
        time.sleep(0.5)
        led[0] = (0)
        time.sleep(0.5)
        led[0] = (255,255,255)
        time.sleep(0.5)
        led[0] = (0)
        time.sleep(0.5)
        led[0] = (255,255,255)
        time.sleep(0.5)
        led[0] = (0)
        time.sleep(0.5)
        led[0] = (255,255,255)
        time.sleep(0.5)
        led[0] = (0)
        time.sleep(0.5)
        led[0] = (255,255,255)
        time.sleep(0.5)
        led[0] = (0)
        time.sleep(1)

        led[0] = (255, 0, 0) # red light
        time.sleep(2)
        led[0] = (255, 234, 0) # yellow light
        time.sleep(1)
        led[0] = (0, 255, 0) # green light
        time.sleep(2)

        led[0] = (255,255,255) # crosswalk
        time.sleep(0.5)
        led[0] = (0)
        time.sleep(0.5)
        led[0] = (255,255,255)
        time.sleep(0.5)
        led[0] = (0)
        time.sleep(0.5)
        led[0] = (255,255,255)
        time.sleep(0.5)
        led[0] = (0)
        time.sleep(0.5)
        led[0] = (255,255,255)
        time.sleep(0.5)
        led[0] = (0)
        time.sleep(0.5)
        led[0] = (255,255,255)
        time.sleep(0.5)
        led[0] = (0)
        time.sleep(1)

    else: # rainbow
        i = (i + 1) % 256  # run from 0 to 255
        # bright += brightInc # I wanna try to let the brightness of the rainbow increasing, but failed
        led.fill(colorwheel(i))
        time.sleep(0.05)

print('All done')
