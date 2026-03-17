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

# shape determines the dimensions of the tensors
shape = (2, 3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeroes_tensor = torch.zeros(shape)
print("\nMore Tensors:", "\n", rand_tensor, "\n", ones_tensor, "\n", zeroes_tensor)

# generates a 3x4 tensor of floats, prints its size, datatype, and device 
tensor = torch.rand(3, 4)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

# checks if tensor can be run on GPU, and then prints device it's stored on
if torch.cuda.is_available():
    tensor = tensor.to("cuda")
    print(f"Tensor is stored on {tensor.device}")

print("\n", tensor)

# selects all row values of the second column in the 4x4 and sets them to 0
tensor = torch.ones(4, 4)
tensor[:,1] = 0
print(tensor)

# concatenates three copies of "tensor" together, with dimension = 1
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(F"t1 = {t1}")

# multiplies the tensor by itself (squares it)
print(f"tensor * tensor \n {tensor * tensor}")

# adds 5 to the tensor with an in-place operation _
print(tensor, "\n")
tensor.add_(5)
print(tensor, "\n")

# tensor to numpy array
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

# numpy array to tensor
n = np.ones(5)
t = torch.from_numpy(n)
print(f"t: {t}")
print(f"n: {n}")