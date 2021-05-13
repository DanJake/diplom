from PIL import Image
import matplotlib.pyplot as plt

t55 = [(140, 106, 0), (162, 88, 3),  (102, 144, 0), (145, 99, 5), (129, 118, 3), (121, 130, 3), (135, 111, 1), (116, 134, 0), (114, 134, 1), (97, 149, 2), (128, 117, 2)   ]
# 121, 130, 3
im = Image.open('./Pictures/etalon1.jpg')
temperature_list= {'95': [(0, 0, 0), (0, 0, 0)],
              '90': [(0, 174, 76), (0, 169, 76)],
              '85': 500,
              '80': 400,
              '75': 100,
              '70': 90,
              '65': 50,
              '60': 40,
              '55': 10,
              '50': 9,
              '45': 5,
              '40': 1}

temperature_count= {'40': 113,
              '45': 155,
              '50': 200,
              '55': 235,
              '60': 260,
              '65': 300,
              '70': 250,
              '75': 200,
              '80': 170,
              '85': 0,
              '90': 0,
              '95': 0}
red = 0
black = 0
orange = 0
range1 = (0, 174, 76)
range2 = (0, 169, 76)


for pixel in im.getdata():
    if pixel == range1 or range2:
        red += 1

for pixel in im.getdata():
    for value in t55:
        if pixel == value:
            temperature_count['55'] += 1

print('black=' + str(temperature_count['55'])+', red='+str(red)+', orange='+str(orange))

pixel_jpg = list(im.getdata())
print(len(pixel_jpg))
f = open('text.txt', 'w')
for index in pixel_jpg:
    f.write(str(index))
x = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
y = []
for i in temperature_count:
    y.append(temperature_count[i]*1000)
print(y)


plt.figure(figsize=(12, 7))
plt.plot(x, y, label="etalon", lw=5, mec='b', )
plt.legend()
plt.grid(True)
#plt.show()