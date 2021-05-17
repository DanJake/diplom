from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy.interpolate import interp1d

class Temperature:

    def __init__(self,
                 temperature,
                 minRange,
                 maxRange):
        self.temperature = temperature
        self.minRange = minRange
        self.maxRange = maxRange
        self.pixelCount = 0

    def append_pixel(self):
        self.pixelCount += 1

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

    tmpDict = {}
    for i in control_list:
        tmpDict[i.temperature] = 0

    for pixel in image.getdata():
        for i in control_list:
            if i.minRange[0] < pixel[0] < i.maxRange[0] and i.minRange[1] < pixel[1] < i.maxRange[1] and i.minRange[2] < pixel[2] < i.maxRange[2]:
                i.append_pixel()
                tmpDict[i.temperature] += 1

    return tmpDict

def draf_graphic(list_1, list_2=[] ):
    x = np.linspace(40, 70, num=16, endpoint=True)
    y = []
    xnew = np.linspace(40, 70, num=150, endpoint=True)

    for i in list_1:
        y.append(list_1[i])

    f = interp1d(x, y, kind='cubic')
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
    plt.legend(['Etalon', 'Second'], loc='best')
    plt.show()

def main():
    im = Image.open('./Pictures/etalon1.jpg')
    im1 = Image.open('./Pictures/example.jpg')
    im2 = Image.open('./Pictures/IRT041_.DTV')
    sort_pixels(im)
    list = sort_pixels(im)
    list1 = sort_pixels(im1)

    print(list)
    print(list1)
    draf_graphic(list)


if __name__ == "__main__":
    main()



