import torch
import numpy as np

# data that is used to make a tensor
data = [[2, 3], [3, 4]]
x_data = torch.tensor(data)

# using the data to make a 2D numpy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

# using the data to make a tensor of all 1's
x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones} \n")

# using the data to make a tensor of all random floats from 0 to 1
x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")

shape = (2, 3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeroes_tensor = torch.zeros(shape)

print("\nMore Tensors:", "\n", rand_tensor, "\n", ones_tensor, "\n", zeroes_tensor)