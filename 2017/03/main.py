import numpy as np

def getRingOf(index):
    # ring in the middle starts with idx=1
    return int(np.ceil((np.ceil(np.sqrt(index)) - 1) / 2)) + 1

def getSidelengthOfRing(ring):
    if ring > 0:
        return 1 + 2 * (ring - 1)
    else:
        return 0

def getIndexOnRing(index):
    ring = getRingOf(index)
    ringStartsAtIdx = getSidelengthOfRing(ring - 1) ** 2 + 1
    indexOnRing = index - ringStartsAtIdx
    return indexOnRing, ring

def getManhattanDistToCenter(index):
    indexOnRing, ring = getIndexOnRing(index)
    if ring > 1:
        ringSidelength = getSidelengthOfRing(ring)
        positionOnSide = (indexOnRing % (ringSidelength-1)) + 1
        # print(f"Index on Ring {indexOnRing}, Pos on side {positionOnSide}")
        # print(f"CrossIdx {int(np.ceil(ringSidelength / 2)) - 1}")
        stepsFromCross = abs(positionOnSide + 1 - int(np.ceil(ringSidelength / 2)))
    else:
        return 0
    

    # print(f"Index {index} is on ring {ring} with side length {ringSidelength} and {stepsFromCross} away from cross")
    # manhattan dist is = steps outward from center + steps away from middle cross
    return (ring - 1) + stepsFromCross

assert getManhattanDistToCenter(1) == 0
assert getManhattanDistToCenter(10) == 3
assert getManhattanDistToCenter(23) == 2
assert getManhattanDistToCenter(1024) == 31
input = 325489
print(getManhattanDistToCenter(input))

def getXYof(index):
    '''
    Define coordinate system with 0,0 in the middle, +x to the right, +y to the top
    '''
    indexOnRing, ring = getIndexOnRing(index)
    if ring > 1:
        ringSidelength = getSidelengthOfRing(ring)
        sideIndex = int(np.floor(indexOnRing / (ringSidelength-1)))
        positionOnSide = (indexOnRing % (ringSidelength-1)) + 1
        coordinateOnSide = positionOnSide + 1 - int(np.ceil(ringSidelength / 2))

        if sideIndex == 0:
            return (ring - 1, coordinateOnSide)
        elif sideIndex == 1:
            return (-1*coordinateOnSide, ring - 1)
        elif sideIndex == 2:
            return (-1*(ring - 1), -1*coordinateOnSide)
        else:
            return (coordinateOnSide, -1*(ring - 1))

    else:
        return (0,0)

def getManhattanDist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def isDirectNeighbor(a, b):
    return abs(a[0] - b[0]) < 2 and abs(a[1] - b[1]) < 2

assert getXYof(1) == (0, 0)

values = {}

for i in range(1,1000):
    # print(f"{i} at {getXYof(i)}")
    assert getManhattanDist(getXYof(i), (0,0)) == getManhattanDistToCenter(i)
    sumOfNeighbors = 0
    posI = getXYof(i)
    for j in range(1,i):
        posJ = getXYof(j)
        if isDirectNeighbor(posI, posJ):
            sumOfNeighbors += values[j]
    values[i] = max(sumOfNeighbors, 1)

    if sumOfNeighbors > input:
        print(f"found {sumOfNeighbors} at {i}")
        break
    # print(f"Computed value {values[i]} at {i}")