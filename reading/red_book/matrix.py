import numpy as np

A = np.array([[1,2], [3,4]])
print(A.shape)

B = np.array([[5,6], [7,8]])
print(B.shape)

print(np.dot(A,B))

X = np.array([1,2])
W = np.array([[1,3,5], [2,4,5]])
print("X shape", X.shape)
print("W shape", W.shape)
print(W)

Y = np.dot(X,W)
print(Y)
