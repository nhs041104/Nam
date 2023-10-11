import numpy as np
import matplotlib.pyplot as plt

image_array = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
plt.imsave('Numpy_img.png', image_array, cmap='Greens')

plt.imshow(image_array, cmap='Greens')
plt.axis('off')
plt.show()
