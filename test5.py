import cv2

img = cv2.imread("JPG/lena.jpg")
print(type(img))

print(img.shape)

imgRotate90ClockWise = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("JPG/lenaCVRotate90ClockWise.jpg",imgRotate90ClockWise)

imgRotate90CounterClockWise = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite("JPG/lenaCVRotate90CounterClockWise.jpg",imgRotate90CounterClockWise)

imgRotate180 = cv2.rotate(img,cv2.ROTATE_180)
cv2.imwrite("JPG/lenaCVRotate180.jpg",imgRotate180)
