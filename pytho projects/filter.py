from PIL import Image

image = Image.open("images.jpg")
imdata = image.getdata()
imagelist = list(imdata)
newimagelist = []

#getting intensity of each pixel by adding numbers in each tuple together
for pixel in imagelist:
    #color=tuple
    intensity = pixel[0] + pixel[1] + pixel[2]
    #print(intensity)
    if(intensity < 182):
        newimagelist.append((0, 51, 76))
    elif(182 <= intensity <= 364):
        newimagelist.append((97, 23, 151))
    elif(364 <= intensity <= 546):
        newimagelist.append((255, 0, 151))
    else:
        newimagelist.append((252, 227, 166))
image.putdata(newimagelist)
image.show()
