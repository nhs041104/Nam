# 이미지

## 이미지 불러오기

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("C:/Users/남현승/Desktop/programing/etc/IMAGE/wook.png")
img_np = np.array(img)

plt.imshow(img_np)
plt.show()
```

Python Imaging Library (PIL) 모듈에서 Image 클래스를 가져온다. 이후 PIL 이미지 객체를 NumPy 배열로 변환하고 그 이미지를 matplot을 이용하여 그래프에 출력시킨다. 

---

## 이미지 크기변경

```python
from PIL import Image

img = Image.open("C:/Users/남현승/Desktop/programing/etc/IMAGE/wook.png")
img_resize = img.resize((400, 400))

img_resize.show()
```

resize를 사용하여 이미지의 크기를 변경시킨다.

---

## 이미지 자르기
```python
from PIL import Image

img = Image.open("C:/Users/남현승/Desktop/programing/etc/IMAGE/wook.png")
img_cropped = img.crop((100, 100, 400, 400))

img_cropped.show()
```

crop을 사용해 원하는 좌표를 지정하여 좌표맘큼 이미지를 자른다.

---

## 이미지 회전

```python
from PIL import Image

img = Image.open("C:/Users/남현승/Desktop/programing/etc/IMAGE/wook.png")
img_rotate = img.rotate((180))

img_rotate.show()
```

rotate를 사용하여 원하는 각도만큼 이미지를 회전시킨다.

---

## 이미지 상하좌우 대칭

```python
from PIL import Image

img = Image.open("C:/Users/남현승/Desktop/programing/etc/IMAGE/wook.png")

img_filp_LR = img.transpose((Image.FLIP_LEFT_RIGHT))
img_filp_LR.show()

img_filp_TB = img.transpose((Image.FLIP_TOP_BOTTOM))
img_filp_TB.show()
```

FLIP_LEFT_RIGHT는 좌우대칭, FLIP_TOP_BOTTOM은 상하대칭이다.

---

## 이미지 필터링

- Blur

```python
from PIL import ImageFilter
from PIL import Image

img = Image.open("C:/Users/남현승/Desktop/programing/etc/IMAGE/wook.png")

img_blur = img.filter(ImageFilter.GaussianBlur(10))
img_blur.show()
```

ImageFilter 클래스를 사용하여 GaussianBlur를 통해 이미지를 블러 처리한다.

---

- Contour

```python
from PIL import ImageFilter
from PIL import Image

img = Image.open("C:/Users/남현승/Desktop/programing/etc/IMAGE/wook.png")

img_contour = img.filter(ImageFilter.CONTOUR)
img_contour.show()
```

마찬가지로 ImageFilter 클래스를 통해 CONTOUR를 사용하여 윤곽을 강조시킨다.

---

- Detail

```python
from PIL import ImageFilter
from PIL import Image

img = Image.open("C:/Users/남현승/Desktop/programing/etc/IMAGE/wook.png")

img_detail = img.filter(ImageFilter.DETAIL)
img_detail.show()
```

DETAIL을 통해 이미지의 세부정보를 강조 시킨다.

---

- Smooth

```python
from PIL import ImageFilter
from PIL import Image

img = Image.open("C:/Users/남현승/Desktop/programing/etc/IMAGE/wook.png")

img_smooth = img.filter(ImageFilter.SMOOTH)
img_smooth.show()
```

SMOOTH를 사용하여 이미지를 부드럽게 만든다.

---

# 이미지 병합 및 저장

```python
from PIL import Image

img_01 = Image.open("C:/Users/남현승/Desktop/programing/etc/IMAGE/wook.png")
img_02 = Image.open("C:/Users/남현승/Desktop/programing/etc/IMAGE/ok.png")

img_01_size = img_01.size
img_02_size = img_02.size

print('img 1 size: ', img_01_size)
print('img 2 size: ', img_02_size)

new_im = Image.new('RGB', (2*img_01_size[0],img_01_size[1]), (250,250,250))

new_im.paste(img_01, (0,0))
new_im.paste(img_02, (img_01_size[0],0))

new_im.save("merged_images.png", "PNG")
new_im.show()
```

paste 메서드를 사용하여 img_01 및 img_02 이미지를 new_im 이미지에 붙여넣고 img_01은 (0, 0) 위치에, img_02는 img_01 이미지의 오른쪽에 위치시킨후 save를 사용하여 merged_images라는 PNG파일로 새로 저장시킨다.

---

# 이미지를 바이트 배열로 변환

```python
def image_to_byte_array(image_path):
    with open(image_path, "rb") as image_file:
        byte_array = bytearray(image_file.read())
    return byte_array

image_path = "C:/Users/남현승/Desktop/programing/etc/IMAGE/wook.png"

image_byte_array = image_to_byte_array(image_path)

print(len(image_byte_array))
```

def함수를 이용하여 이미지 파일 경로를 인수 받고 바이너리 읽기를 통해 이미지 파일을 바이트 배열로 변환시킨다.

---

# Numpy 배열을 이미지로 변환

```python
import numpy as np
import matplotlib.pyplot as plt

image_array = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
plt.imsave('Numpy_img.png', image_array, cmap='Greens')

plt.imshow(image_array, cmap='Greens')
plt.axis('off')
plt.show()
```

0에서 255 사이의 무작위 정수를 가진 100x100 크기의 NumPy 배열을 생성하고 dtype=np.uint8을 사용하여 배열의 데이터 타입을 8비트의 부호 없는 정수로 설정한다.
그리고 imsave 함수를 사용하여 NumPy 배열 image_array를 'Numpy_img.png'라는 파일로 저장하는데 이때 cmap='Greens'로 배열의 값을, 즉 보여지는 이미지 파일의 색을 녹색으로 설정한다.(plt.axis('off'))는 그래프의 x축, y축을 끄는 역할을 한다.

---
