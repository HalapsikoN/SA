# importing required libraries of opencv 
import cv2
import openpyxl
import numpy as np

wb = openpyxl.load_workbook('labb.xlsx')
sheet = wb['test2']

# importing library for plotting 
from matplotlib import pyplot as plt

# reads an input image 
img = cv2.imread('flower2.jpg', 0)

# find frequency of pixels in range 0-255 
histr = cv2.calcHist([img], [0], None, [256], [0, 256])

convertedHist = []

for i in range(0, len(histr), 10):
    temp = 0
    if i < 250:
        for j in range(i, i + 10, 1):
            temp += histr[j]
    else:
        for j in range(i, i + 6, 1):
            temp += histr[j]
    convertedHist.append(temp)

print(len(convertedHist))

for i in range(0, len(convertedHist), 1):
    sheet['D' + str(i + 2)] = int(convertedHist[i])

wb.save('labb.xlsx')

# show the plotting graph of an image 
# plt.plot(histr)
# plt.grid()
# plt.show()

allPoint = []
# for i in range(0, len(img), 1):
#    for j in range(0, len(img[i]), 1):
#        allPoint.append(img[i][j])

# print(len(allPoint))

# for i in range(0, len(allPoint), 1):
#    sheet['C' + str(i + 2)] = int(allPoint[i])

#wb.save('labb.xlsx')

print("yse")
