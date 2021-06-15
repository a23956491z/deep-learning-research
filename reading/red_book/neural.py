import numpy as np

def sigmoid(x):
    return 1 / ( 1 + np.exp(-x))

X = np.array([1.0,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])


print("W1.shape",W1.shape)
print("B1.shape",B1.shape)
print("X.shape",X.shape)

A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)

print("A1",A1)
print("Z1",Z1)

print()
print("W2.shape",W2.shape)
print("B2.shape",B2.shape)
print("Z1.shape",Z1.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

print("A2",A2)
print("Z2",Z2)

def identity_func(x):
    return x

W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])

A3 = np.dot(Z2, W3) + B3
Y = identity_func(A3)
