import math
import time
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width, height = unicorn.get_shape()

c = 128
i = 0.0
offset = 30
while True:
    i = i + 0.03
    # r = (math.cos((i) / 2.0) + math.cos((i) / 2.0)) * 64.0 + 128.0
    # g = (math.sin((i) / 1.5) + math.sin((i) / 2.0)) * 64.0 + 128.0
    # b = (math.sin((i) / 2.0) + math.cos((i) / 1.5)) * 64.0 + 128.0
    # r = max(0, min(255, r + offset))
    # g = max(0, min(255, g + offset))
    # b = max(0, min(255, b + offset))
    red = math.sin(i + 2) * width
    green = math.sin(i + 0) * width
    blue = math.sin(i + 4) * width

    red = max(0, min(255, red))
    green = max(0, min(255, green))
    blue = max(0, min(255, blue))

    c = (c + 1) % 255
    # c = max(0, min(255, c))
    for y in range(height):
        for x in range(width):
            # unicorn.set_pixel(x, y, int(r), int(g), int(b))
            unicorn.set_pixel(x, y, int(red), int(green), int(blue))
    unicorn.show()
    time.sleep(0.1)
