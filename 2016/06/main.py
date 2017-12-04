import numpy as np

with open('test.txt', 'r') as f:
    inStrings = f.readlines()
inString = [list(s.strip()) for s in inStrings]
inArray = np.array(inString)
print(inArray.shape)

message = np.zeros(inArray.shape[1])
for i in range(inArray.shape[1]):
    