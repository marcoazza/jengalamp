import math
import time


class Action:

    def render(self):
        pass


class Simple(Action):
    def __init__(self, unicorn, height, width):
        self.unicorn = unicorn
        self.width = width
        self.height = height
        for y in range(self.height):
            for x in range(self.width):
                self.unicorn.set_pixel(x, y, 255, 0, 255)

    def render(self):
        self.unicorn.show()


class Blink(Action):
    def __init__(self, unicorn, height, width):
        self.unicorn = unicorn
        self.width = width
        self.height = height
        for y in range(self.height):
            for x in range(self.width):
                self.unicorn.set_pixel(x, y, 255, 0, 255)

    def render(self):
        self.unicorn.show()


class Rainbow(Action):
    def __init__(self, unicorn, height, width):
        self.unicorn = unicorn
        self.width = width
        self.height = height
        self.i = 0.0
        self.offset = 30

    def render(self):
        self.i = (self.i + 0.3) % math.pi
        r = (math.cos((self.i) / 2.0) + math.cos((self.i) / 2.0)) * 64.0 + 128.0
        g = (math.sin((self.i) / 1.5) + math.sin((self.i) / 2.0)) * 64.0 + 128.0
        b = (math.sin((self.i) / 2.0) + math.cos((self.i) / 1.5)) * 64.0 + 128.0
        r = max(0, min(255, r + self.offset))
        g = max(0, min(255, g + self.offset))
        b = max(0, min(255, b + self.offset))
        for y in range(self.height):
            for x in range(self.width):
                self.unicorn.set_pixel(x, y, int(r), int(g), int(b))
        self.unicorn.show()
        time.sleep(0.1)


available = {
    'simple': Simple,
    'blink': Blink,
    'rainbow': Rainbow
}
