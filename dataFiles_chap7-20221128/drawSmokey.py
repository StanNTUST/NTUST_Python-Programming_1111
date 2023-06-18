from images import Image
image = Image("smokey.gif")
image.draw()
print("1==================")
print(image.getWidth())
print(image.getHeight())
print("2==================")
print(image)
print("3==================")
print(image.getPixel(0,0))
print("4==================")
image = Image(150, 150)
image.draw()
print("5==================")
blue = (0, 0, 255)
y = image.getHeight() // 2
for x in range(image.getWidth()):
    image.setPixel(x, y-1, blue)
    image.setPixel(x, y, blue)
    image.setPixel(x, y+1, blue)
image.draw()
print("6==================")
image.save("horizontal.gif")
image = Image("horizontal.gif")
image.draw()
print("7==================")
for y in range(image.getHeight()):
    for x in range(image.getWidth()):
        image.setPixel(x, y, (255,0,0))
image.draw()  
print("8==================")
image = Image("smokey.gif") 
image.draw()
print("9==================")
(r, g, b) = image.getPixel(0, 0)
print(r,g,b)
r =+10
g =+10
b =+10
image.setPixel(0, 0, (r, g, b))
image.draw()
print("10==================")
def blackAndWhite(image):
    """Converts the argument image to black and white."""
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)
blackAndWhite(image) 
image.draw()    
print("11==================")
image = Image("smokey.gif")
def grayscale(image):
    """Converts the argument image to grayscale."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))  
grayscale(image) 
image.draw()   
print("12==================")
from images import Image
image = Image("smokey.gif")
image.draw()
newImage = image.clone() # Create a copy of image
newImage.draw()
print("13==================")
grayscale(newImage) # Change in second window only
newImage.draw()
image.draw() # Verify no change to original
