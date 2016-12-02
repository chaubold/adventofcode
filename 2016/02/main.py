# setup
import numpy as np
with open('input.txt') as f:
    directions = f.readlines()

# test, should return 1985
# directions = ['ULL','RRDDD','LURDL','UUUUD']

# what to do on each letter of instructions
updates = {
    'U': np.array([0,-1]), # north
    'R': np.array([1,0]), # east
    'D': np.array([0,1]), # south
    'L': np.array([-1,0]) # west
}

# Part 1:
# keypad = np.array([[1,2,3], [4,5,6], [7,8,9]])
# minMaxPerRowCol = np.array([[0,2], [0,2], [0,2]])
# currentPos = np.array([1,1]) # start at 5

# Part 2: 
# Result should now be 5DB3!
keypad = np.array([[0,0,1,0,0], [0,2,3,4,0], [5,6,7,8,9], [0,'A','B','C',0], [0,0,'D',0,0]])
minMaxPerRowCol = np.array([[2,2], [1,3], [0,4], [1,3], [2,2]])
currentPos = np.array([0,2]) # start at 5

numbers = []

for numberInstructionLine in directions:
    numberInstructionLine = numberInstructionLine.strip()
    for i in numberInstructionLine:
        rowBounds = minMaxPerRowCol[currentPos[0]]
        colBounds = minMaxPerRowCol[currentPos[1]]
        currentPos += updates[i]
        currentPos[0] = np.clip(currentPos[0], colBounds[0], colBounds[1])
        currentPos[1] = np.clip(currentPos[1], rowBounds[0], rowBounds[1])
        # print('\tgoing {} to {}'.format(i, currentPos))
    # print("Found {} at {}".format(keypad[currentPos[1], currentPos[0]], currentPos))
    numbers.append(keypad[currentPos[1], currentPos[0]])

print("Keypad code is {}".format(numbers))