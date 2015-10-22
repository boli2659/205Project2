
"""Project 2.py
Team Satoshi Nakamoto"""

from PIL import Image
import random

img1 = Image.open('C:\\Users\\Miguel\\Desktop\\CSUMB\\Fall 2015\\CST205\\Images\\Tiger.jpg')

n = 4 #number of tiles

width, height = img1.size

row = int(width / (n/2))
column = int(height / (n/2))
preX = 0
preY = 0
newX = int(row)
newY = int(column)

img_list = []

for x in range(0, int(n/2)):
    for y in range(0, int(n/2)):
        crop_rectangle = (preX, preY, newX, newY)
        crop_im = img1.crop(crop_rectangle)
        #crop_im.show()
        img_list.append(crop_im)
        #print (preX)
        #print (preY)
        #print (newX)
        #print (newY)
        preX = int(newX)
        if preX > 150:
            preX = 0

        newX = int(newX) + row
        if newX > 300:
            newX = 150

    preY = int(newY)

    newY = int(newY) + column

#img1.show()

preX = 0
preY = 0
newX = int(row)
newY = int(column)



random.shuffle(img_list)

jigsaw = Image.new('RGB', (width, height))

for crop_im in img_list:
    jigsaw.paste(img_list[0], (0, 0))
    jigsaw.paste(img_list[1], (0, 84))
    jigsaw.paste(img_list[2], (150, 0))
    jigsaw.paste(img_list[3], (150, 84))

jigsaw.show()





