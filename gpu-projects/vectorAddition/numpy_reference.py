import numpy as np
import time

#1. Initialiaze a numpy array of size 1024 * 1024
dim_x = 1024
dim_y = 1024
array_size =  dim_x * dim_y
vec_A = np.arange(array_size, dtype=np.float32).reshape(dim_x, dim_y)
vec_B = np.arange(array_size, dtype=np.float32).reshape(dim_x, dim_y)

#2. Start Timer
start_time = time.perf_counter()

#3. Perform Vector Addition
vec_C = vec_A + vec_B

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")

print(vec_C)
