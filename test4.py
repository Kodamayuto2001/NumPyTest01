import cv2 
import numpy as np 

src = cv2.imread("JPG/lena.jpg")

mask = np.zeros_like(src)

print(mask.shape)

print(mask.dtype)

cv2.rectangle(mask,(50,50),(100,200),(255,255,255),thickness=-1)
cv2.circle(mask,(200,100),50,(255,255,255),thickness=-1)
cv2.fillConvexPoly(mask,np.array([[330,50],[300,200],[360,150]]),(255,255,255))

cv2.imwrite("JPG/OpenCVMask.jpg",mask)

maskBlur = cv2.GaussianBlur(mask,(51,51),0)

cv2.imwrite("JPG/OpenCVMaskBlur.jpg",maskBlur)

dst = src * (maskBlur /255)

cv2.imwrite("JPG/MaskBlurResult.jpg",dst)