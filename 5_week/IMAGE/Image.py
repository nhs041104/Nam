from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("C:\\Users\\남현승\\Desktop\\programing\\etc\\wook.png")
img_np = np.array(img)

plt.imshow(img_np)
plt.show()
