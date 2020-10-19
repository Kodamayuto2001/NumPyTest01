import numpy as np

# どっと積

print(np.dot(3,4))

print(np.dot([2,3],[2,3]))

a = [[2,0],
     [0,1]]
b = [[2,2],
     [2,2]]

x = np.dot(a,b)

print(x)

# ベクトルの内積
a = np.array([1,2,3])
b = np.array([0,1,0])
print(np.inner(a,b))

a = np.arange(24).reshape((2,3,4))
print(a)

b = np.arange(4)
print(b)

x = np.inner(a,b)
print(x)