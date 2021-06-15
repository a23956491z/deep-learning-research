import numpy as np
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.9

    if w1*x1 + w2*x2 > theta:
        return 1
    return 0

def AND2(x1, x2):
    w = np.array([0.5, 0.5])
    x = np.array([x1, x2])
    b = -0.9

    if (np.sum( w*x ) + b) > 0:
        return 1
    return 0

def perceptron(w, b, x):
    if(np.sum( w*x) + b) > 0:
        return 1
    return 0

def OR(x1, x2):
    x = np.array([x1, x2])
    return perceptron(np.array([0.5, 0.5]), -0.3, x)

def NAND(x1, x2):
    x = np.array([x1, x2])
    return perceptron(np.array([-0.5, -0.5]), 0.7, x)

def XOR(x1, x2):
    y1 = NAND(x1,x2)
    y2 = OR(x1,x2)

    return AND(y1,y2)



testing = [(0,0), (0,1), (1,0), (1,1)]

print("a\tb\tAND")
for tu in testing:
    a, b = tu[0], tu[1]
    print(a, b, AND2(a, b), sep='\t')

print("\na\tb\tOR")
for tu in testing:
    a, b = tu[0], tu[1]
    print(a, b, OR(a, b), sep='\t')

print("\na\tb\tNAND")
for tu in testing:
    a, b = tu[0], tu[1]
    print(a, b, NAND(a, b), sep='\t')


print("\na\tb\tXOR")
for tu in testing:
    a, b = tu[0], tu[1]
    print(a, b, XOR(a, b), sep='\t')
