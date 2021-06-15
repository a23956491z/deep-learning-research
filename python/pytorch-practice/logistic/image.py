# %%
import torch
import torchvision

from torchvision.datasets import MNIST

import matplotlib.pyplot as plt
# %%
dataset = MNIST(root='data/', download=True)

# %%
print(len(dataset))

test_dataset = MNIST(root='data/', train=False)
print(len(test_dataset))

# %%
test_dataset[0]

# %%
image, label = dataset[0]
plt.imshow(image, cmap='gray')
print('Label:', label)

# %%
import torchvision.transforms as transforms

dataset = MNIST(root='data/', train=True, transform=transforms.ToTensor())

img_tensor, label = dataset[0]
print(img_tensor.shape, label)

# %%
print(img_tensor[:, 10:15, 10:15])
print(torch.max(img_tensor), torch.min(img_tensor))

# %%
plt.imshow(img_tensor[0, 10:15, 10:15], cmap='gray')


# %%
# Spliting Training and Validation datasets
from torch.utils.data import random_split

train_ds, val_ds = random_split(dataset, [50000, 10000])
len(train_ds), len(val_ds)

# %%
# DataLoader
from torch.utils.data import DataLoader

batch_size = 128

train_loader = DataLoader(train_ds, batch_size, shuffle=True)
val_loader = DataLoader(val_ds, batch_size, shuffle=True)
