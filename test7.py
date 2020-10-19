import numpy as np
from PIL import Image 

img = np.array(Image.open("JPG/lena.jpg"))
print(type(img))

print(img.shape)

Image.fromarray(np.rot90(img)).save("JPG/lena_np_rot90.jpg")

Image.fromarray(np.rot90(img,2)).save("JPG/lena_np.rot90_180.jpg")

Image.fromarray(np.rot90(img,3)).save("JPG/lena_np_rot90_270.jpg")

# numpyでndarrayを上下左右に反転する関数はnp.flip()
# 上下に反転する関数　　　　　　　　　　　　np.flipud()
# 左右に反転する関数                    　np.fliplr()

Image.fromarray(np.flipud(img)).save("JPG/lena_np_flipud.jpg")
Image.fromarray(np.fliplr(img)).save("JPG/lena_np_fliplr.jpg")
Image.fromarray(np.flip(img,(0,1))).save("JPG/lena_np_flip_ud_lr.jpg")
