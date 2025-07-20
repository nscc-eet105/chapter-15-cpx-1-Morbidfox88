# Chad Collard
# Chapter 15 cpx 1
# Main
# 7/20/2025

import adafruit_circuitplayground.express as cp
import time
from region import Region

yellow = Region((255, 255, 0), (5, 6, 7))
blue = Region((0, 0, 255), (2, 3, 4))

while True:
    yellow.all_on()
    blue.all_on()
    cp.pixels.show()
    time.sleep(0.5)

    yellow.all_off()
    blue.all_off()
    cp.pixels.show()
    time.sleep(0.5)
