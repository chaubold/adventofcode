import numpy as np

data = np.genfromtxt('input.txt')
print(data.shape)

# part 1
result = np.logical_and(data[:,0] + data[:,1] > data[:,2], np.logical_and(data[:,2] + data[:,1] > data[:,0], data[:,0] + data[:,2] > data[:,1]))
print(np.count_nonzero(result))

# part 2
data = np.reshape(data.T, [1908,3])
result = np.logical_and(data[:,0] + data[:,1] > data[:,2], np.logical_and(data[:,2] + data[:,1] > data[:,0], data[:,0] + data[:,2] > data[:,1]))
print(np.count_nonzero(result))