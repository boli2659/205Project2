import image_slicer
from PIL import Image
from PIL import ImageDraw, ImageFont


tiles = image_slicer.slice(input('Enter File Name:'), 4, save=False)

for tile in tiles:
    overlay = ImageDraw.Draw(tile.image)

image_slicer.save_tiles(tiles)

image1 = Image.open('C:\\Users\\Michael\\Documents\\205Project2\\Project2\\_02_02.png')
image2 = Image.open('C:\\Users\\Michael\\Documents\\205Project2\\Project2\\_02_01.png')
image3 = Image.open('C:\\Users\\Michael\\Documents\\205Project2\\Project2\\_01_02.png')
image4 = Image.open('C:\\Users\\Michael\\Documents\\205Project2\\Project2\\_01_01.png')

width,height = image1.size
width = (width * 2) + 20
height = (height * 2) + 20
jigsaw = Image.new('RGB',(width,height))
width,height = image1.size
jigsaw.paste(image1,(0,0))
jigsaw.paste(image2,(width + 10,0))
jigsaw.paste(image3,(0,height + 10))
jigsaw.paste(image4,(width + 10, height + 10))

jigsaw.show()

picture1 = 0
while picture1 != 4:
    picture1 = int(input("Where should the top left square be?\n1. Top left\n2. Bottom Left\n3. Top right\n4. Bottom right\n"))
    if picture1 != 4:
        print("Incorrect Try again")
print("Correct!")

while picture1 != 2:
    picture1 = int(input("Where should the top right square be?\n1. Top left\n2. Bottom Left\n3. Top right\n4. Bottom right\n"))
    if  picture1 != 2:
        print("Incorrect Try again")
print("Correct!")

while picture1 != 1:
    picture1 = int(input("Where should the bottom left square be?\n1. Top left\n2. Bottom Left\n3. Top right\n4. Bottom right\n"))
    if  picture1 != 1:
        print("Incorrect Try again")
print("Correct!")

while picture1 != 3:
    picture1 = int(input("Where should the bottom right square be?\n1. Top left\n2. Bottom Left\n3. Top right\n4. Bottom right\n"))
    if  picture1 != 3:
        print("Incorrect Try again")
print("Correct!")
print ("Jigsaw Solved!")

jigsaw.paste(image4,(0,0))
jigsaw.paste(image3,(width + 10,0))
jigsaw.paste(image2,(0,height + 10))
jigsaw.paste(image1,(width + 10, height+ 10))

jigsaw.show()
