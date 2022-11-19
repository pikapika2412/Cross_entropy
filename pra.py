import numpy as np
import math as m

w = np.array([0, 1, 5, 1, 2])
y = np.array([1, 6, 1]).T
x = np.array([[1, 1, 1], [1, -2, 0], [2, 5, 1]])

x1 = np.array([1, 1, 2])
x2 = np.array([1, -2, 5])
x3 = np.array([1, 0, 1])

label = ['cat', 'dog', 'cat']

def step1(x, w):
	sum = 0
	for i in range(3):
		sum += x1[i] * w[i]
	return sum

def step2(h, w):
	y = []
	for i in range (2):
		t = h * w[i + 3]
		y.append(t)

	return y

def step3(y):
	z = []
	
	z1 = round(m.exp(y[0]) / (m.exp(y[0]) + m.exp(y[1])), 6)
	z2 = 1 - z1

	z.append(z1)
	z.append(z2)

	return z

def step4(label, z):
	if label == 'cat':
		l = [1, 0]
	else:
		l = [0, 1]

	r = - (l[0] * m.log(m.e, z[0]) + l[1] * m.log(m.e, z[1]))
	return r

h = step1(x1, w)
y = step2(h, w)
z = step3(y)
r = step4(label[0], z)

print(y)
print(z)
print(r)