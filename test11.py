import numpy as np 
from PIL import Image 

arr1 = np.arange(4).reshape((2,2))
print(arr1)
# [[0 1]
#  [2 3]]

arr2 = np.arange(6).reshape((2,3))
print(arr2)
# [[0 1 2]
#  [3 4 5]]

print(np.dot(arr1,arr2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(arr1.dot(arr2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(np.matmul(arr1,arr2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(arr1 @ arr2)
# [[ 3  4  5]
#  [ 9 14 19]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

print(np.dot(mat1,mat2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(mat1.dot(mat2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(np.matmul(mat1, mat2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(mat1 @ mat2)
# [[ 3  4  5]
#  [ 9 14 19]]

print(mat1 * mat2)
# [[ 3  4  5]
#  [ 9 14 19]]

#               numpy.ndarray	    numpy.matrix
# 次元数	    任意	            2次元のみ
# *演算子	    各要素ごとの積	    行列の積
# **演算子	    各要素をべき乗	    行列の積を繰り返す
# **-1	        各要素を-1乗	    逆行列
# **-n	        各要素を-n乗	    逆行列の積を繰り返す
# .I属性    	無い	            逆行列

# ndarrayでも@演算子で行列の積が計算できるようになったので、matrixを使うメリットは少なくなった