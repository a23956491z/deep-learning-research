# %%
import numpy as  np
import torch

# Input (temp, rainfall, humidity)
inputs = np.array([[73, 67, 43],
                   [91, 88, 64],
                   [87, 134, 58],
                   [102, 43, 37],
                   [69, 96, 70]], dtype='float32')

# Targets (apples, oranges)
targets = np.array([[56, 70],
                    [81, 101],
                    [119, 133],
                    [22, 37],
                    [103, 119]], dtype='float32')

inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)
print(inputs)
print(targets)

# %%
""" ADD Weight(w) & Bias(b) """

w = torch.randn(2, 3, requires_grad=True)
b = torch.randn(2, requires_grad=True)

print(w)
print(b)

# linear regression model
def model(x):

    # @ present the matrix multiplication
    return x @ w.t() + b

# %%
preds = model(inputs)
print('preds:')
print(preds)
print('target:')
print(targets)

# %%
# MSE loss
def mse(t1, t2):
    diff = t1 - t2

    # torch.tensor.numel returns the number of elements in tensor
    return torch.sum(diff*diff) / diff.numel()

loss = mse(preds, targets)
print(loss)

# %%
# compute gradients
loss.backward()

# %%
print(w)
print(w.grad)
print(b)
print(b.grad)

# %%
# reset the gradients to zero
w.grad.zero_()
b.grad.zero_()
print(w.grad)
print(b.grad)

# %%
# adjist weights & auto reset gradients
preds = model(inputs)
loss = mse(preds, targets)
loss.backward()

with torch.no_grad():
    w -= w.grad * 1e-5
    b -= b.grad * 1e-5
    w.grad.zero_()
    b.grad.zero_()

print(w)
print(b)
print(loss)


# %%
# train for 100 epochs
for i in range(100):
    preds = model(inputs)
    loss = mse(preds, targets)
    loss.backward()

    with torch.no_grad():
        w -= w.grad * 1e-5
        b -= b.grad * 1e-5
        w.grad.zero_()
        b.grad.zero_()

# calculate the final loss
preds = model(inputs)
loss = mse(preds, targets)
print(loss)
print(preds)
print(targets)
