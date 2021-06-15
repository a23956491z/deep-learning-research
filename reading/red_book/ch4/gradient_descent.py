def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

#assume we have multiple x ([x0, x1, x2...])
def numerical_gradient(f, x):

	h = 1e-4
	grad = np.zeros_like(x)

	for idx in range(x.size):

		tmp_val = x[idx]

		# f(x+h)
		x[idx] = tmp_val + h #only change one variable
		fxh1 = f(x)
		# f(x-h)
		x[idx] = tmp_val - h
		fxh2 = f(x)

		grad[idx] = (fxh1- fxh2) / (2*h)
		x[idx] = tmp_val

	return grad
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        #print(x, grad, grad*lr)
        x -= lr*grad

    return x

def func1(x):
    return x[0]**2 + x[1]**2

import numpy as np
x = np.array([-3.0,4.0])


#print(func1(x))
#print(numerical_diff(func1, x))
print(gradient_descent(func1, x, lr=0.1, step_num = 100))
