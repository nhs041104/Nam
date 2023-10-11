from PIL import ImageFilter
from PIL import Image

img = Image.open("C:\\Users\\남현승\\Desktop\\programing\\etc\\wook.png")


img_detail = img.filter(ImageFilter.DETAIL)
img_detail.show()
