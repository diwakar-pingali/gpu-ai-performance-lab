import torch 
import numpy as np

#set the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#1 directly from data
data = [[1,2],[3,4]]
x_data = torch.tensor(data, device=device)

#2 from numpy array
np_array = np.array(data)
x_data = torch.from_numpy(np_array)
x_data = x_data.to(device)

#3 with random, const values
shape = (2, 2)
rand_tensor = torch.rand(shape, device=device)
ones_tensor = torch.ones(shape, device=device)

print(f"Datatype of tensor: {rand_tensor.dtype}")
print(f"Device tensor is stored on: {rand_tensor.device}")

