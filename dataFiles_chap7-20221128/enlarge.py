"""
File: enlarge.py
Project 7.11

Defines and tests a function to enlarge an image.

define filename="smokey.gif"
input factor to enlarge image
output the original picture
use enlarge function to enlarge picture
    get piture's width and height
    set new image to width and height product factor
    run loop to get all old picture's height's pixel
        run loop to get all old picture's width's pixel
            get picture's pixel
            run the loop to enlarge height by factor
                run the loop to enlarge width by factor
                    enlarge the old picture's height's and width's pixel by factor to set new picture
    return new picture which is enlarged
output the new picture

"""
from images import Image

def enlarge(image, factor):
    """Builds and returns a copy of the image which is larger
    by the factor."""
    width = image.getWidth()
    height = image.getHeight()
    new = Image(width * factor, height * factor)
    for y in range(height- 1):
        for x in range(1, width):
            oldP = image.getPixel(x, y)
            for sety in range (factor):
                for setx in range(factor):
                    new.setPixel((x-1)*factor+setx, y*factor+sety, oldP)
    return new
def main():
    filename = "smokey.gif"
    image = Image(filename)
    factor=int(input("Please input the factor："))
    image.draw()
    image=enlarge(image, factor)
    image.draw()
if __name__ == "__main__":
   main()


