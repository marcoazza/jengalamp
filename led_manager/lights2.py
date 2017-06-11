import time
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width, height = unicorn.get_shape()

THRESHOLD = 85
r, g, b = 255, 0, 0
temp_r, temp_g, temp_b = r, g, b
decrease = True
while True:
    if decrease:
        r = max(0, min(r, temp_r - 1))
        g = max(0, min(g, temp_g - 1))
        b = max(0, min(b, temp_b - 1))
        temp_r -= 1
        temp_g -= 1
        temp_b -= 1
    else:
        r = max(0, min(temp_r, temp_r + 1))
        g = max(0, min(temp_g, temp_g + 1))
        b = max(0, min(temp_b, temp_b + 1))
        temp_r += 1
        temp_g += 1
        temp_b += 1
    if temp_r <= THRESHOLD and temp_g <= THRESHOLD and temp_b <= THRESHOLD:
        decrease = False
        time.sleep(0.25)
    elif temp_r >= r and temp_g >= g and temp_b >= b:
        decrease = True
        time.sleep(0.5)
    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x, y, int(r), int(g), int(b))
    unicorn.show()
    # time.sleep(0.002)
