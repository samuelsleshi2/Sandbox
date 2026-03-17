import torch

# import and instantiate NN model, feed it data, keep track of expected answer
from torchvision.models import resnet18, ResNet18_Weights
model = resnet18(weights=ResNet18_Weights.DEFAULT)
data = torch.rand(1, 3, 64, 64)
label = torch.rand(1, 1000)

# using prediction and label to calculate the error and start backprop
prediction = model(data) # making prediction
loss = (prediction - label).sum() # error summed to one number
loss.backward() # initiation of backward propagation

# SGD optimizer used to perform gradient descent
optim = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)
optim.step()