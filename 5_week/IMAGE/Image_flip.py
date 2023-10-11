from PIL import Image

img = Image.open("C:\\Users\\남현승\\Desktop\\programing\\etc\\wook.png")

img_filp_LR = img.transpose((Image.FLIP_LEFT_RIGHT))
img_filp_LR.show()


img_filp_TB = img.transpose((Image.FLIP_TOP_BOTTOM))
img_filp_TB.show()
