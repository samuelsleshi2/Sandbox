1. what does "dim" do in the torch.cat function on line 46?

    - specifies what axis to concatenate along

2. what does learning rate and momentum mean with optimizers?

    - learning rate is the step size the model takes when .step() is called
    on the optimizer. step size too high = overshooting the goal. step size
    too low: taking microscopic steps which takes forever and is inefficient

    - momentum is what speeds up the training and prevents the model from
    getting stuck

3. what is gradient descent?

    - the algorithm that minimizes the loss (error). this is when the optimizer
    steps down the loss landscape to find where the error is lowest. remember,
    autograd has already calculated the slope, gradient descent is just the process
    of actually moving down that slope the gradient is the mathematical slope of the 
    hill or computational graph, and the descent is going down that graph or hill to 
    find the lowest possible error.

4. what is SGD (stochastic gradient descent) in terms of optimizers?

    - SGD looks at just one random data point, or a small batch, then updates the model weights. this makes it faster per step than evaluating the whole dataset

5. two steps to training a neural network:

    - Forward Propagation: The NN makes its best guess about the correct output. It runs the input data through each of its functions to make this guess.
    
    - Backward Propagation: The NN adjusts its parameters proportionate to the error in its guess. It does this by traversing backwards from the output, collecting the derivatives of the error with respect to the parameters of the functions (gradients), and optimizing the parameters using gradient descent.

6. how to train a neural network:

    - Define the neural network that has some learnable parameters (or weights)
    - Iterate over a dataset of inputs
    - Process input through the network
    - Compute the loss (how far is the output from being correct)
    - Propagate gradients back into the network’s parameters
    - Update the weights of the network, typically using a simple update rule: 
    weight = weight - learning_rate * gradient