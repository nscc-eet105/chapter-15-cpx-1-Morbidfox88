# Chad Collard
# Chapter 15 cpx 1&2
# Main
# 7/20/2025

from adafruit_circuitplayground import cp
import time
from region import Region

REGION_DATA = {
    "yellow": {"color": (255, 255, 0), "leds": (5, 6, 7), "tone": 252},
    "blue": {"color": (0, 0, 255), "leds": (2, 3, 4), "tone": 209},
    "red": {"color": (255, 0, 0), "leds": (7, 8, 9), "tone": 310},
    "green": {"color": (0, 255, 0), "leds": (0, 1, 2), "tone": 415},
}

regions = [
    Region(data["color"], data["leds"], data["tone"]) for data in REGION_DATA.values()
]

while True:
    for region in regions:
        region.all_on()
        region.play_tone()
        cp.pixels.show()
        time.sleep(0.5)

        region.all_off()
        region.stop_tone()
        cp.pixels.show()
        time.sleep(0.5)
