# %%
import torch.nn as nn
import numpy as np
import torch

# %%
# Input (temp, rainfall, humidity)
inputs = np.array([[73, 67, 43],
                    [91, 88, 64],
                   [87, 134, 58],
                   [102, 43, 37],
                   [69, 96, 70],
                   [74, 66, 43],
                   [91, 87, 65],
                   [88, 134, 59],
                   [101, 44, 37],
                   [68, 96, 71],
                   [73, 66, 44],
                   [92, 87, 64],
                   [87, 135, 57],
                   [103, 43, 36],
                   [68, 97, 70]],
                  dtype='float32')

# Targets (apples, oranges)
targets = np.array([[56, 70],
                    [81, 101],
                    [119, 133],
                    [22, 37],
                    [103, 119],
                    [57, 69],
                    [80, 102],
                    [118, 132],
                    [21, 38],
                    [104, 118],
                    [57, 69],
                    [82, 100],
                    [118, 134],
                    [20, 38],
                    [102, 120]],
                   dtype='float32')

inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)

# %%
from torch.utils.data import TensorDataset

# TensorDataset access to rows from inputs and targets
train_ds = TensorDataset(inputs, targets)
train_ds[0:3]

# %%
# DataLoader is a iterable object
# and it use for create batch
from torch.utils.data import DataLoader
batch_size = 5
train_dl = DataLoader(train_ds, batch_size, shuffle=True)

for xb, yb in train_dl:
    print(xb)
    print(yb)
    break

# %%
model =  nn.Linear(3, 2)

# print each parameter
print(model.weight)
print(model.bias)

# print all parameters
print(list(model.parameters()))

# %%
preds = model(inputs)
preds


# %%
# LOSS function
import torch.nn.functional as F
loss_fn = F.mse_loss

loss = loss_fn(model(inputs), targets)
print(loss)

# %%
# define optimizer
# stochastic gradient descent
opt = torch.optim.SGD(model.parameters(),lr=1e-5)

# %%
# train the model
def fit(num_epochs, model, loss_fn, opt, train_dl):

    for epoch in range(num_epochs):

        # train with batches of data
        for xb, yb in train_dl:

            # generate predictions
            pred = model(xb)

            # use loss_fn to calculate loss
            loss = loss_fn(pred, yb)

            # calculate gradients
            loss.backward()

            # Update parameters using gradients
            # we use SGD method here
            opt.step()

            opt.zero_grad()

        if(epoch+1) % 10 == 0:
            print('Epoch [{}/{}], LOSS: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

# %%
fit(100, model, loss_fn, opt, train_dl)
# %%
# generate predicitons
preds = model(inputs)
print(preds)

# %%
print(targets)
