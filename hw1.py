import numpy as np
from numpy import genfromtxt

new_matrix = np.array([[1, 2, 3], [2, 4, 6], [2, 7, 8]])
print(new_matrix)

mnist_train = genfromtxt("mnist_train.csv", dtype=float, delimiter=',')
mnist_test = genfromtxt("mnist_test.csv", dtype=float, delimiter=',')

# Copies data into new array while dividing into required range
mnist_train_data = mnist_train[:, range(1, len(mnist_train[0]))]/255

# copies training values into new array
mnist_train_values = mnist_train[:, 0]


# for i in range(1,len(mnist_train))
print(len(mnist_train))
print(len(mnist_test))
print(len(mnist_train_data))
print(len(mnist_train_values))

print('done loading')
