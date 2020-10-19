import numpy as np
from PIL import Image

l_2d = [[0,1,2],[3,4,5]]
print(l_2d)
print(type(l_2d))

arr = np.array([[0,1,2],[3,4,5]])
print(arr)
print(type(arr))

arr = np.arange(6)
print(arr)

arr = np.arange(6).reshape((2,3))
print(arr)

print("-----Numpy Matrix-----")
mat = np.matrix([[0,1,2],[3,4,5]])
print(mat)
print(type(mat))

mat = np.matrix(arr)
print(mat)
print(type(mat))

mat_1d = np.matrix([0,1,2])
print(mat_1d)
print(type(mat_1d))

print(mat_1d.shape)

# コンストラクタの引数に一次元配列を渡すと二次元に拡張され、三次元以上の配列を渡すとエラーになる

# Pythonリスト型の二次元配列の要素の値は、list[行番号][列番号]でアクセスできる。行番号・列番号は0始まり。値を取得することも、変更（代入）することもできる

print(l_2d)
print(l_2d[0][1])

l_2d[0][1] = 100
print(l_2d)

# 転置行列
l_2d = [[0,1,2],[3,4,5]]
print(l_2d)

print([list(x) for x in list(zip(*l_2d))])

# numpy.ndarrayとnumpy.matrixは.Tで転置行列を取得できる。
arr = np.arange(6).reshape((2,3))
print(arr)
print(arr.T)

img = np.array(Image.open("JPG/lena.jpg"))
print(type(img))
print(img.shape)
print(img.T.shape)
print(img.T[0].shape)
Image.fromarray(np.uint8(img.T[0])).save("JPG/imgT0.jpg")
Image.fromarray(np.uint8(img.T[0].T)).save("JPG/imgT0T.jpg")

# 行列の和と差
print("-----行列の和と差-----")
l_2d_1 = [[0,1,2],[3,4,5]]
l_2d_2 = [[0,2,4],[6,8,10]]

print(l_2d_1 + l_2d_2)

arr1 = np.arange(6).reshape((2,3))
print(arr1)

arr2 = np.arange(0,12,2).reshape((2,3))
print(arr2)

print(arr1 + arr2)

print(arr1 - arr2)

# Pythonリスト型では、数値との*演算は配列の繰り返しとなり、リスト同士の*演算は定義されていないためerrorになる
print(l_2d_1 * 2)
# [[0, 1, 2], [3, 4, 5], [0, 1, 2], [3, 4, 5]]

# numpy.ndarrayとnumpy.matrixでは、数値（スカラー値）との*演算は各要素のスカラー倍となる
print(arr1 * 2)
# [[ 0  2  4]
#  [ 6  8 10]]

print(mat * 2)
# [[ 0  2  4]
#  [ 6  8 10]]

# 行列同士の要素ごとの積（アダマール積）を取得するには、numpy.multiply()を使う
print(np.multiply(arr1,arr2))

# numpy.ndarrayでは、*演算子はnumpy.multiply()と等価で、要素ごとの積になる
print(arr1 * arr2)
