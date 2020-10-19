import numpy as np
from PIL import Image 

src1 = np.array(Image.open('lena.jpg'))
src2 = np.array(Image.open('rocket.jpg').resize(src1.shape[1::-1], Image.BILINEAR))

dst = src1 * 0.5 + src2 * 0.5 

Image.fromarray(dst.astype(np.uint8)).save("alphaBlend.jpg")

dst = src1 * 0.5 + src2 * 0.5 + (96,128,160)

# clip()メソッドで最小値0,最大値255に収めている
dst = dst.clip(0, 255)

Image.fromarray(dst.astype(np.uint8)).save("alphaBlendGamma.jpg")

# マスク処理
src = np.array(Image.open("lena.jpg"))
mask = np.array(Image.open("horse_r.png").resize(src.shape[1::-1],Image.BILINEAR))

#print(mask.dtype,mask.min(),mask.max())

mask = mask / 255

#print(mask.dtype, mask.min(), mask.max())

dst = src * mask 

Image.fromarray(dst.astype(np.uint8)).save("numpyMask.jpg")