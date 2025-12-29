import numpy as np
#0-D Tensor
a=np.array(4)
print(a)
print(a.ndim)
#1-D Tensor: It is a collection of 0-D tensors
arr=np.array([1,2,3,4]) #as this vector contains 4 elements, it is a 4D Vector
print(arr)
print(arr.ndim)
#2-D Tensor
matrix=np.array([[1,2],[3,4],[5,6]])
print(matrix)
print(matrix.ndim)
#3-D Tensor
Matrix3D=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]]) 
print(Matrix3D)
