import PIL
from PIL import Image
import requests
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
from IPython.display import display
import numpy as np
import imageio
import matplotlib.pyplot as plt
#add path to the image file
filename = R'C:\Users\clarkj5\Documents\Python Scripts\TestImage.jpg'
#input image dimensions
with Image.open(filename) as image:
    width, height = image.size
#print image details to check image has been found
print (image.size)
print(image)
print(type(image))
image = Image.open(filename)
output_image = Image.new('I', image.size, 0xffffff)
#iterate through pixels
def binarize(image, threshold):
    #Show starting image
    image.show()
    output_image=image.convert("L")
    #show greyscale image
    output_image.show()
    #iterate through pixels changing to black or white deoending on if they are above or below the threshold
    for x in range(output_image.width):
        for y in range(output_image.height):
            # for the given pixel at w,h, lets check its value against the threshold
            if output_image.getpixel((x,y))< threshold: 
                # lets set this to zero (Black)
                output_image.putpixel( (x,y), 0 )
            else:
                # otherwise lets set this to 255 (White)
                output_image.putpixel( (x,y), 255 )
    
    return output_image

#(image to be examined, threshold)
binarize(image, 100)
#show final image 
output_image.show(R'C:\Users\clarkj5\Documents\Python Scripts\circleout.jpg', image)