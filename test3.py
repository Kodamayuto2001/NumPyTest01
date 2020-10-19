import numpy as np
from PIL import Image 

src1 = np.array(Image.open("JPG/lena.jpg"))
print(src1.shape)
src2 = np.array(Image.open("JPG/rocket.jpg").resize(src1.shape[1::-1],Image.BILINEAR))


mask1 = np.array(Image.open("JPG/Gradation4.jpg").resize(src1.shape[1::-1],Image.BILINEAR))

mask1 = mask1 / 255 

dst = src1 * mask1 + src2 * (1 - mask1)

Image.fromarray(dst.astype(np.uint8)).save("JPG/numpyGraImg.jpg")

mask2 = np.array(Image.open("JPG/horse_r.png").resize(src1.shape[1::-1],Image.BILINEAR))

mask2 = mask2 / 255

dst = (src1 * mask1 + src2 * (1 - mask1)) * mask2

Image.fromarray(dst.astype(np.uint8)).save("JPG/NumPyImgMaskGrad.jpg")