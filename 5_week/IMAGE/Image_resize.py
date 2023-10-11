from PIL import Image

img = Image.open("C:\\Users\\남현승\\Desktop\\programing\\etc\\wook.png")

img_resize = img.resize((400, 400))

img_resize.show()
