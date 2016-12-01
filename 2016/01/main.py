# setup
import numpy as np
with open('input.txt') as f:
    directions = f.readline()

directions = [d.strip() for d in directions.split(',')]
lrToRotation = {'L': -1, 'R': 1}
directions = [(lrToRotation[d[0]], int(d[1:])) for d in directions]

# x faces east/west, y faces north/south
orientations = {
    0: np.array([0,1]), # north
    1: np.array([1,0]), # east
    2: np.array([0,-1]), # south
    3: np.array([-1,0]) # west
}

# -----------------------------------------------------------
# Part 1
currentOrientation = 0
currentPosition = np.array([0,0])

for d in directions:
    currentOrientation = (currentOrientation + d[0]) % 4
    currentPosition += orientations[currentOrientation] * d[1]

print(currentPosition)
print "Distance from Target ", abs(currentPosition[0])+abs(currentPosition[1])

# -----------------------------------------------------------
# Part 2

currentOrientation = 0
currentPosition = np.array([0,0])
visitedPositions = set([tuple(currentPosition)])

for d in directions:
    currentOrientation = (currentOrientation + d[0]) % 4
    for _ in range(d[1]):
        currentPosition += orientations[currentOrientation]
        if tuple(currentPosition) in visitedPositions:
            print currentPosition
            print "Distance from Target ", abs(currentPosition[0])+abs(currentPosition[1])
            exit()
        else:
            visitedPositions.add(tuple(currentPosition))


