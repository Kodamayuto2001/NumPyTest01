import numpy as np
from PIL import Image 

print(np.linspace(0,10,3))

print(np.linspace(0,10,4))

print(np.linspace(0,10,5))

# np.tile() は配列を縦横に並べる関数
a = np.array([0,1,2,3])

print(np.tile(a,2))

print(np.tile(a,(3,2)))

print(np.tile(a,(2,1)))

# 縦または横方向に増加または減少するndarrayを生成する関数を準備
# このndarrayが単色のグラデーション画像に相当する

def getGradation2d(start,stop,width,height,is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start,stop,width),(height,1))
    else:
        return np.tile(np.linspace(start,stop,height),(width,1)).T

array = getGradation2d(100,200,100,100,True)
Image.fromarray(np.uint8(array)).save("JPG/Gradation2.jpg",quality=95)

def getGradation3d(width,height,startList,stopList,isHorizontalList):
    result = np.zeros((height,width,len(startList)),dtype=np.float)

    for i,(start,stop,isHorizontal) in enumerate(zip(startList,stopList,isHorizontalList)):
        result[:,:,i] = getGradation2d(start,stop,width,height,isHorizontal)
    return result


# numpy 行（高さ） x 列（幅） x 色（3）
# RGB
array = getGradation3d(512,256,(0,0,0),(255,255,255),(False,False,False))
Image.fromarray(np.uint8(array)).save("JPG/Gradation3.jpg",quality=95)

array = getGradation3d(512, 256, (0, 0, 192), (255, 255, 64), (True, False, False))
Image.fromarray(np.uint8(array)).save("JPG/Gradation4.jpg",quality=95)
