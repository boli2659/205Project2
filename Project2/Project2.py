import image_slicer
from PIL import Image
from PIL import ImageDraw, ImageFont


tiles = image_slicer.slice('C:\\Users\\Michael\\Desktop\\Project2\\illidan.png', 4, save=False)

for tile in tiles:
    overlay = ImageDraw.Draw(tile.image)

image_slicer.save_tiles(tiles)


jigsaw = Image.new('RGB',(980,980))
image1 = Image.open('C:\\Users\\Michael\\Desktop\\Project2\\_02_02.png')
image2 = Image.open('C:\\Users\\Michael\\Desktop\\Project2\\_02_01.png')
image3 = Image.open('C:\\Users\\Michael\\Desktop\\Project2\\_01_02.png')
image4 = Image.open('C:\\Users\\Michael\\Desktop\\Project2\\_01_01.png')
jigsaw.paste(image1,(0,0))
jigsaw.paste(image2,(490,0))
jigsaw.paste(image3,(0,490))
jigsaw.paste(image4,(490,490))

jigsaw.show()

Position = input('First image position:')


                 
