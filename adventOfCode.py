# --------------------------------------------
# Day 1 part 1
# --------------------------------------------
parens = '(((())))()((((((( ... '
parens.count('(') - parens.count(')')

# --------------------------------------------
# Day 1 part 2
# --------------------------------------------
currentFloor = 0

for idx, dir in enumerate(parens):
    if currentFloor == -1:
        print idx
        break
    if dir == '(':
        currentFloor += 1
    else:
        currentFloor -= 1

# --------------------------------------------
# Day 2 part 1
# --------------------------------------------
f = open('boxes.txt', 'r')

def area(line):
    line = map(int, line.split('x'))
    line.sort()
    l,w,h = line
    return 3*l*w + 2*w*h + 2*h*l

s = 0
for l in f:
    s += area(l)

# --------------------------------------------
# Day 2 part 2
# --------------------------------------------
f = open('boxes.txt', 'r')

def ribbon(line):
    line = map(int, line.split('x'))
    line.sort()
    l,w,h = line
    return 2*l + 2*w + l*w*h

r = 0
for l in f:
    r += ribbon(l)

# --------------------------------------------
# Day 3 part 1
# --------------------------------------------
moves = '>>vv>^v^^^v<>v<>><>^vv^> ....'
current_pos = [0,0]
deliveries = {}

if tuple(current_pos) in deliveries:
    deliveries[tuple(current_pos)] += 1
else:
    deliveries[tuple(current_pos)] = 1

for m in moves:
    if m == '<':
        current_pos[0] -= 1
    elif m == '>':
        current_pos[0] += 1
    elif m == 'v':
        current_pos[1] -= 1
    else:
        current_pos[1] += 1

    if tuple(current_pos) in deliveries:
        deliveries[tuple(current_pos)] += 1
    else:
        deliveries[tuple(current_pos)] = 1

len(deliveries)

# --------------------------------------------
# Day 3 part 2
# --------------------------------------------
current_pos = [0,0]
other_pos = [0,0]
deliveries = {}

if tuple(current_pos) in deliveries:
    deliveries[tuple(current_pos)] += 1
else:
    deliveries[tuple(current_pos)] = 1

for m in moves:
    current_pos, other_pos = other_pos, current_pos
    if m == '<':
        current_pos[0] -= 1
    elif m == '>':
        current_pos[0] += 1
    elif m == 'v':
        current_pos[1] -= 1
    else:
        current_pos[1] += 1

    if tuple(current_pos) in deliveries:
        deliveries[tuple(current_pos)] += 1
    else:
        deliveries[tuple(current_pos)] = 1
        
len(deliveries)

# --------------------------------------------
# Day 4 part 1 and 2
# --------------------------------------------
import hashlib
prefix = 'iwrupvqb'

i = 0
while True:
    if i % 1000 == 0:
        print("\rTrying {}".format(i))
    s = prefix + str(i)
    m = hashlib.md5()
    m.update(s)
    h = m.hexdigest()
    if h[0:6] == '000000':
        break
    i += 1
print("Found valid adventcoin: {}".format(i))

# --------------------------------------------
# Day 5 part 1
# --------------------------------------------
def isNaughty(s):
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return True
    sumVovels = 0
    for c in 'aeiou':
        sumVovels += s.count(c)
    if sumVovels < 3:
        return True
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return False
    return True

f = open('naughtyStrings.txt', 'r')
numNice = 0
for l in f:
    if not isNaughty(l.strip()):
        numNice += 1
print("Found {} nice strings".format(numNice))

# --------------------------------------------
# Day 5 part 2
# --------------------------------------------
def hasDoubleLetterPair(s):
    for i in range(len(s) - 1):
        if s.count(s[i:i+2]) >= 2:
            return True
    return False

def hasSpacedRepeat(s):
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            return True
    return False

def isNice(s):
    return hasDoubleLetterPair(s) and hasSpacedRepeat(s)

f = open('naughtyStrings.txt', 'r')
numNice = 0
for l in f:
    if isNice(l.strip()):
        numNice += 1
print("Found {} nice strings".format(numNice))

# --------------------------------------------
# Day 6 part 1
# --------------------------------------------
import numpy as np

lights = np.zeros((1000,1000), dtype=np.uint8)

f = open('day6.txt', 'r')
for l in f:
    l = l.strip()
    words = l.split(' ')
    starts = map(int, words[-3].split(','))
    ends = map(int, words[-1].split(','))
    ends = [e + 1 for e in ends]
    if words[0] == 'toggle':
        lights[starts[0]:ends[0], starts[1]:ends[1]] = 1 - lights[starts[0]:ends[0], starts[1]:ends[1]]
    else:
        if words[1] == 'on':
            lights[starts[0]:ends[0], starts[1]:ends[1]] = 1
        else:
            lights[starts[0]:ends[0], starts[1]:ends[1]] = 0

print("{} lights are burning!".format(np.count_nonzero(lights)))

# --------------------------------------------
# Day 6 part 2
# --------------------------------------------
import numpy as np

lights = np.zeros((1000,1000), dtype=np.int32)

f = open('day6.txt', 'r')
for l in f:
    l = l.strip()
    words = l.split(' ')
    starts = map(int, words[-3].split(','))
    ends = map(int, words[-1].split(','))
    ends = [e + 1 for e in ends]
    if words[0] == 'toggle':
        lights[starts[0]:ends[0], starts[1]:ends[1]] += 2
    else:
        if words[1] == 'on':
            lights[starts[0]:ends[0], starts[1]:ends[1]] += 1
        else:
            lights[starts[0]:ends[0], starts[1]:ends[1]] -= 1
    lights[lights < 0] = 0

print("Total brightness: {}".format(np.sum(lights)))

# --------------------------------------------
# Day 7 part 1
# --------------------------------------------
providedValues = {}
mask = 65535

class Gate:
    def __init__(self, words):
        if words[0] == 'NOT':
            self.__operator = words[0]
            self.__inputs = [words[1]]
        else:
            self.__inputs = [words[0]]
            self.__operator = words[1]
        if self.__operator == 'AND' or self.__operator == 'OR':
            self.__inputs.append(words[2])
        if 'SHIFT' in self.__operator:
            self.__bits = int(words[2])
        self.__cached = None
        self.__output = words[-1]

    def __getValue(self, key):
        if str.isdigit(key):
            return int(key)
        else:
            return providedValues[key].evaluate()

    def evaluate(self):
        if self.__cached == None:
            if self.__operator == 'NOT':
                self.__cached = ~self.__getValue(self.__inputs[0])
            elif self.__operator == 'AND':
                self.__cached = self.__getValue(self.__inputs[0]) & self.__getValue(self.__inputs[1])
            elif self.__operator == 'OR':
                self.__cached = self.__getValue(self.__inputs[0]) | self.__getValue(self.__inputs[1])
            elif self.__operator == 'LSHIFT':
                self.__cached = self.__getValue(self.__inputs[0]) << self.__bits
            elif self.__operator == 'RSHIFT':
                self.__cached = self.__getValue(self.__inputs[0]) >> self.__bits
            elif self.__operator == '->':
                self.__cached = self.__getValue(self.__inputs[0])

            if self.__cached == None:
                print("Result of {} -> {} is None with inputs {}".format(self.__operator, self.__output, self.__inputs.keys()))
            else:
                # constrain to 16 bit
                self.__cached = self.__cached & mask
        return self.__cached

f = open('day7.txt', 'r')
for l in f:
    l = l.strip()
    words = l.split(' ')
    providedValues[words[-1]] = Gate(words)

print("Input to a:{}".format(providedValues['a'].evaluate()))

# for part 2: in day7.txt replace the line '14146 -> b' by the new value as input to b

