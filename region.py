# Chad Collard
# Chapter 15 cpx 1&2
# Region class
# 7/20/2025
from adafruit_circuitplayground import cp


class Region:
    def __init__(
        self,
        color,
        leds,
        tone,
    ):
        self.color = color
        self.leds = leds
        self.tone = tone

    def set_color(self, color):
        self.color = color

    def set_leds(self, leds):
        self.leds = leds

    def set_tone(self, tone):
        self.tone = tone

    def get_color(self):
        return self.color

    def get_leds(self):
        return self.leds

    def get_tone(self):
        return self.tone

    def all_on(self):
        for led_index in self.leds:
            cp.pixels[led_index] = self.color

    def all_off(self):
        for led_index in self.leds:
            cp.pixels[led_index] = (0, 0, 0)

    def play_tone(self):
        cp.start_tone(self.tone)

    def stop_tone(self):
        cp.stop_tone()
