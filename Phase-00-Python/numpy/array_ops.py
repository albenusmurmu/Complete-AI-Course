import numpy as np

a = np.array([[1,2],
              [3,4]])
b = np.array([[4,3],
             [2,1]])
print("print 1 to every element:\n", a+1)
print("Subtracting 2 from each element : \n ", b - 2)
print("Sum of all array elements : \n", a.sum())
print("Array sum : \n", a+b)