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

