from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy.interpolate import interp1d
import cv2


class Temperature:

    def __init__(self,
                 temperature,
                 minRange,
                 maxRange):
        self.temperature = temperature
        self.minRange = minRange
        self.maxRange = maxRange


def control_table():
    control_list = []
    control_list.append(Temperature(40, (70, 0, 80), (85, 5, 120)))
    control_list.append(Temperature(42, (40, 0, 120), (85, 5, 185)))
    control_list.append(Temperature(44, (0, 0, 185), (40, 5, 240)))
    control_list.append(Temperature(46, (0, 0, 200), (8, 50, 220)))
    control_list.append(Temperature(48, (0, 20, 125), (8, 132, 235)))
    control_list.append(Temperature(50, (0, 105, 80), (5, 165, 130)))
    control_list.append(Temperature(52, (0, 200, 0), (36, 240, 35)))
    control_list.append(Temperature(54, (36, 120, 0), (120, 225, 5)))
    control_list.append(Temperature(56, (120, 60, 0), (180, 120, 5)))
    control_list.append(Temperature(58, (180, 0, 0), (255, 70, 5)))
    control_list.append(Temperature(60, (230, 0, 0), (255, 20, 5)))
    control_list.append(Temperature(62, (235, 40, 0), (250, 100, 5)))
    control_list.append(Temperature(64, (235, 100, 0), (252, 160, 5)))
    control_list.append(Temperature(66, (235, 160, 0), (250, 220, 5)))
    control_list.append(Temperature(68, (235, 210, 0), (250, 235, 50)))
    control_list.append(Temperature(70, (240, 240, 50), (255, 255, 240)))
    return control_list


def sort_pixels(image):
    control_list = control_table()

    pixels_dictionary = {}
    for i in control_list:
        pixels_dictionary[i.temperature] = 0

    for pixel in image.getdata():
        for i in control_list:
            if i.minRange[0] < pixel[0] < i.maxRange[0] and i.minRange[1] < pixel[1] < i.maxRange[1] and i.minRange[2] < pixel[2] < i.maxRange[2]:
                pixels_dictionary[i.temperature] += 1

    return pixels_dictionary


def draft_graphic(list_1, list_2=[]):

    x = np.linspace(40, 70, num=16, endpoint=True)
    y_first = []
    xnew = np.linspace(40, 70, num=150, endpoint=True)

    for i in list_1:
        y_first.append(list_1[i])

    f = interp1d(x, y_first, kind='cubic')
    ax = plt.subplot()
    if list_2:
        y_second = []
        for i in list_2:
            y_second.append(list_2[i])
        f2 = interp1d(x, y_second, kind='cubic')
        ax.plot(xnew, f(xnew), '-', xnew, f2(xnew), '--')
    else:
        ax.plot(xnew, f(xnew), '-')

    ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    ax.grid(which='major', color='k')
    ax.minorticks_on()
    ax.grid(which='minor', color='gray', linestyle=':')
    plt.legend(['First picture', 'Second picture'], loc='best')
    plt.show()


def count_coef(list_1, list_2):
    coef = []
    countCoef = 0
    sumCoef = 0
    for i in list_1:
        coef.append(list_2[i]/list_1[i])
        countCoef += 1
        sumCoef += list_2[i]/list_1[i]

    print(sumCoef/countCoef + 0.1)
    return sumCoef/countCoef + 0.1


def other_method(some_image):
    image = cv2.imread(some_image)

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


def main():
    im = Image.open('./Pictures/etalon1.jpg')
    im1 = Image.open('./Pictures/example.jpg')

    list = sort_pixels(im)
    list1 = sort_pixels(im1)

    print(list)
    print(list1)
    count_coef(list, list1)
    #draft_graphic(list)
    #other_method('./Pictures/etalon1.jpg')


if __name__ == "__main__":
    main()



