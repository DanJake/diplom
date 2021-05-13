from PIL import Image

im = Image.open('./Pictures/etalon.jpg')

red = 0
black = 0

for pixel in im.getdata():
    if pixel == (0, 0, 0):
        black += 1
    elif pixel == (240, 0, 0):
        red += 1
print('black=' + str(black)+', red='+str(red))
----------------------------------------------------------------------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('./Pictures/etalon.jpg')

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)


hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
mask = cv2.inRange(hsv_image, light_orange, dark_orange)
result = cv2.bitwise_and(image, image, mask=mask)

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result)
plt.show()
-----------------------------------------------------------------------------------------------

import math


def convert_K_to_RGB(colour_temperature):
    """
    Converts from K to RGB, algorithm courtesy of
    http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/
    """
    maxTemp = 100;
    minTemp = 0;



    tmp_internal = colour_temperature
    redVal = 255 / (maxTemp - minTemp) * (tmp_internal - minTemp);
    blueVal = 255 / (maxTemp - minTemp) * (maxTemp - tmp_internal);
    # red


    return redVal, 0, blueVal


if __name__ == "__main__":
    print("Preview requires matplotlib")
    from matplotlib import pyplot as plt

    step_size = 10
    for i in range(45, 100, step_size):
        color = list(map(lambda div: div / 255.0, convert_K_to_RGB(i))) + [1]
        print(color)
        plt.plot((i, i), (0, 1), linewidth=step_size / 2.0, linestyle="-", color=color)

    plt.show()
--------------------------------------------------------------------------------------
pixel_jpg = list(im.getdata())
f = open('text.txt', 'w')
for index in pixel_jpg:
    f.write(str(index))