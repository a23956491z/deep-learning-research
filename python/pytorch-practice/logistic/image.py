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
plt.imshow(image[0], cmap='gray')
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
