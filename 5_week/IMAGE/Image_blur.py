from PIL import ImageFilter
from PIL import Image

img = Image.open("C:\\Users\\남현승\\Desktop\\programing\\etc\\wook.png")


img_blur = img.filter(ImageFilter.GaussianBlur(10))
img_blur.show()
