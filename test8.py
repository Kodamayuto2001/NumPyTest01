import numpy as np 
from PIL import Image 

# 4次元テンソル
# 画像の数、画像のheight, 画像のwidth, 画像のチャネル数

img = np.array([[100,0],[0,100]])
print(type(img))
print(img.shape)
Image.fromarray(np.uint8(img)).save("NumPyImg/0.jpg")
