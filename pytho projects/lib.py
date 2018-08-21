from PIL import Image

bird = Image.open("birds.jpg")
bird.show()
birdata = bird.getdata()
birdlist = list(birdata)

#image2 = Image.new("RGB", (500,500))
#image2.show()
