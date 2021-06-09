# %% ####################
import torch

# value
t1 = torch.tensor(4.)
# vector
t2 = torch.tensor([1., 2, 3, 4])
# matrix
t3 = torch.tensor([[5, 6],
                   [7, 8],
                   [9, 10]])

# size of tensor
print(t3.shape)

# %% ####################
x = torch.tensor(3.)
w = torch.tensor(4., requires_grad=True)
b = torch.tensor(5., requires_grad=True)

y = w * x + b

# calculate gradient
y.backward()

# Display gradients
print('dy/dx:', x.grad)
print('dy/dw:', w.grad)
print('dy/db:', b.grad)

# %% ####################
t6 = torch.full((3,2), 42)
print(t6)
t7 = torch.cat((t3, t6))
print(t7)

# %% ####################
import numpy as np

x = np.array([[1, 2], [3, 4.]])
y = torch.from_numpy(x)
y
