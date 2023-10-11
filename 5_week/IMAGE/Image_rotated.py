from PIL import Image

img = Image.open("C:\\Users\\남현승\\Desktop\\programing\\etc\\wook.png")

img_rotate = img.rotate((180))

img_rotate.show()
