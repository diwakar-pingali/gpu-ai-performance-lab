import numpy as np

#1 Create Numpy array from existing data
arr = np.array([1,2,3,4], dtype=np.int32)
print("arr\n", arr)

#2 Create Numpy array from shape
arr_1 = np.ones(4, dtype=np.int32)
print("arr_1\n", arr_1)

arr_2 = np.ones((2,2), dtype=np.int32)
print("arr_2\n", arr_2)

#3 Create Numpy array from numerical ranges
arr_3 = np.arange(4, dtype=np.int32)
print("arr_3\n", arr_3)

arr_4 = np.linspace(start=10, stop=14, num=4, dtype=np.int32)
print("arr_4\n", arr_4)