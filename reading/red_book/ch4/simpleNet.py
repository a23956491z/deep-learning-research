import numpy as np

# t is traning data(one hot)
# y is output of neural network
def cross_entropy_error(y, t):
    if y.ndim ==1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y)) / batch_size

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)

    y = exp_a / sum_exp_a
    return y

def numerical_gradient(f, x):
    h = 1e-4 # 0.0001

    grad = np.zeros_like(x)

    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x) # f(x+h)

        x[idx] = tmp_val - h
        fxh2 = f(x) # f(x-h)

        grad[idx] = (fxh1 - fxh2) / (2*h)

        x[idx] = tmp_val # 値を元に戻す
        it.iternext()

    return grad

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        #print(x, grad, grad*lr)
        x -= lr*grad

    return x

class simpleNet:
    def __init__(self):
        #normal distribution
        self.W = np.random.randn(2,3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)

        loss = cross_entropy_error(y, t)
        return loss

net = simpleNet()
print( net.W)

x = np.array([0.6, 0.9])
p = net.predict(x)
print(p,np.argmax(p))

t = np.array([0,0,1])
print('\nLoss : ',net.loss(x, t))

def f(W):
    return net.loss(x, t)


dW = numerical_gradient(f, net.W)
print('\n',dW)
