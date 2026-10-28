import numpy as np

a = np.array([[1,2],
              [3,4]])
b = np.array([[4,3],
             [2,1]])
print("print 1 to every element:\n", a+1)
print("Subtracting 2 from each element : \n ", b - 2)
print("Sum of all array elements : \n", a.sum())
print("Array sum : \n", a+b)

# Data types in numpy
x = np.array([1,2])
print(x.dtype)

x = np.array([1.0,2.0])
print(x.dtype)

x = np.array([1,2], dtype=np.int64)
print(x.dtype)

# Math Operations on data
arr1 = np.array([[4,7],[2,6]], dtype=np.float64)
arr2 = np.array([[3,6],[2,8]], dtype=np.float64)

print(np.add(arr1,arr2))
print(np.sum(arr1))
print(np.sqrt(arr1))
print(arr1.T)