import math
import time
THRESHOLD = 85


class Action:

    def render(self):
        pass

    def _set_matrix(self, r, g, b):
        for y in range(self.height):
            for x in range(self.width):
                self.unicorn.set_pixel(x, y, r, g, b)


class Simple(Action):
    def __init__(self, unicorn, height, width, r=None, g=None, b=None):
        self.unicorn = unicorn
        self.width = width
        self.height = height
        self._set_matrix(r, g, b)

    def render(self):
        self.unicorn.show()


class Blink(Action):
    def __init__(self, unicorn, height, width, r=None, g=None, b=None):
        self.unicorn = unicorn
        self.width = width
        self.height = height
        self.r, self.g, self.b = r, g, b
        self.temp_r, self.temp_g, self.temp_b = r, g, b
        self.decrease = True
        self._set_matrix(r, g, b)

    def _increase(self):
        self.r = max(0, min(self.temp_r, self.temp_r + 1))
        self.g = max(0, min(self.temp_g, self.temp_g + 1))
        self.b = max(0, min(self.temp_b, self.temp_b + 1))
        self.temp_r += 1
        self.temp_g += 1
        self.temp_b += 1

    def _decrease(self):
        self.r = max(0, min(self.r, self.temp_r - 1))
        self.g = max(0, min(self.g, self.temp_g - 1))
        self.b = max(0, min(self.b, self.temp_b - 1))
        self.temp_r -= 1
        self.temp_g -= 1
        self.temp_b -= 1

    def render(self):
        if self.decrease:
            self._decrease()
        else:
            self._increase()
        if self.temp_r <= THRESHOLD and self.temp_g <= THRESHOLD and self.temp_b <= THRESHOLD:
            self.decrease = False
            time.sleep(0.25)
        elif self.temp_r >= self.r and self.temp_g >= self.g and self.temp_b >= self.b:
            self.decrease = True
            time.sleep(0.5)
        self._set_matrix(int(self.r), int(self.g), int(self.b))
        self.unicorn.show()


class Rainbow(Action):
    def __init__(self, unicorn, height, width, r=None, g=None, b=None):
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
        self._set_matrix(int(r), int(g), int(b))
        self.unicorn.show()
        time.sleep(0.1)


available = {
    'simple': Simple,
    'blink': Blink,
    'rainbow': Rainbow
}
