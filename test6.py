import cv2

img = cv2.imread("JPG/lena.jpg")
print(type(img))

print(img.shape)

# OpenCVで画像を上下左右に反転するにはcv2.flip()を使う
# flipcode = 0 上下反転
img_glip_ud = cv2.flip(img,0)
cv2.imwrite("JPG/lena_cv_flip_ud.jpg",img_glip_ud)

# flipcode > 0 で左右反転
img_flip_lr = cv2.flip(img,1)
cv2.imwrite("JPG/lena_cv_flip_lr.jpg",img_flip_lr)

#flipcode < 0 で上下左右反転
img_flip_ud_lr = cv2.flip(img,-1)
cv2.imwrite("JPG/lena_cv_flip_ud_lr.jpg",img_flip_ud_lr)
