from PIL import Image
import matplotlib.pyplot as plt

t55 = [(140, 106, 0), (162, 88, 3),  (102, 144, 0), (145, 99, 5), (129, 118, 3), (121, 130, 3), (135, 111, 1), (116, 134, 0), (114, 134, 1), (97, 149, 2), (128, 117, 2)   ]
# 121, 130, 3
im = Image.open('./Pictures/etalon1.jpg')
temperature_list= {'69': [(249, 248, 10), (249, 248, 8)],
              '67': [(247, 228, 1), ],
              '65': [(248, 172, 1), ], #last
              '64': [(247, 109, 0), (247, 113, 0), (246, 120, 0)],
              '63': [(247, 104, 0)],
              '62': [(248, 42, 2), (246, 62, 0), (247, 65, 0)],
              '60': [(244, 5, 0), (239, 8, 0)],
              '55': [(0, 0, 0), (0, 0, 0)],
              '50': [(0, 0, 0), (0, 0, 0)],
              '42': [(54, 0, 156), (0, 0, 0)],
              '40': [(64, 1, 144), (67, 0, 144), (65, 0, 142), (68, 0, 139), (67, 0, 139),
                     (68, 0, 137), (64, 0, 146), (63, 1, 146), (65, 1, 141), (64, 1, 142) ]}

temperature_count= {'40': 0,
              '45': 0,
              '50': 0,
              '55': 0,
              '60': 0,
              '65': 0,
              '70': 0,
              '75': 0,
              '80': 0,
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



print('black=' + str(temperature_count['55'])+', red='+str(red)+', orange='+str(orange))
pixel_jpg = list(im.getdata())
f = open('text.txt', 'w')
for index in pixel_jpg:
    f.write(str(index) + '\n')

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