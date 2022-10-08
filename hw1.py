import numpy as np
from numpy import genfromtxt

# initialize array of random weights for inputs and bias
weights = np.random.uniform(low=-0.05, high=0.05, size=(10, 785))
# identity matrix used to compare truthy values in perceptron output
trutharray = np.identity(10, float)

# pull csv's into arrays
mnist_train = genfromtxt("mnist_train_snip.csv", dtype=float, delimiter=',')
mnist_test = genfromtxt("mnist_test_snip.csv", dtype=float, delimiter=',')

# splits out input/data portion of training and test arrays
mnist_train_data = np.append(
    mnist_train[:, range(1, len(mnist_train[0]))]/255, np.full((len(mnist_train), 1), 1, dtype=float), axis=1)
mnist_test_data = np.append(
    mnist_test[:, range(1, len(mnist_test[0]))]/255, np.full((len(mnist_test), 1), 1, dtype=float), axis=1)

# splits out values of training and test arrays
mnist_train_values = mnist_train[:, 0]
mnist_test_values = mnist_train[:, 0]


def sigmoid(a):
    return 1 if a > 0 else 0

# inrow is input data for perceptron
# Creates output array to capture result of each perceptron
# Loops through input array and dots with each perceptron weightset
# Runs the dot through the sigmoid function and stores in output array


def perceptronout(inrow):
    output = np.zeros((10))
    for i in range(0, 9):
        output[i] = sigmoid(np.dot(inrow, weights[i]))
    return output

# outresult is the return from perceptronout
# trueval is the value we're aiming for
# return is array indicating which of the perceptrons had the right output
# uses identity matrix - compares outresult array to appropriate row in identity array
# reverse logic on output (zero for true match) allows us to directly use in training


def comparetrue(outresult, trueval):
    output = np.zeros((10))
    for i in range(0, 9):
        if outresult[i] == trutharray[trueval]:
            output[i] = 0
        else:
            output[i] = 1
    return output


def trainonrow(select, n):
    outaccurate = comparetrue(perceptronout(
        mnist_train_data[select]), mnist_train_values[select])
    for i in range(0, 9):
        weights


# for i in range(1,len(mnist_train))
print(len(mnist_train))
print(len(mnist_test))
print(len(mnist_train_data))
print(len(mnist_train_values))

print('done loading')
