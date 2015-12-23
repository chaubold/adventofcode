# --------------------------------------------
# Day 1 part 1
# --------------------------------------------
f = open('day1.txt', 'r')
parens = f.readline().strip()
print("Result is {}".format(parens.count('(') - parens.count(')')))

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
print("Santa ends up on floor {}".format(currentFloor))

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
print("They need {} square feet of wrapping paper".format(s))

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
print("They need {} feet of ribbon".format(r))

# --------------------------------------------
# Day 3 part 1
# --------------------------------------------
f = open('day3.txt', 'r')
moves = f.readline().strip()
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

print("Presents were delivered to {} houses".format(len(deliveries)))

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
print("Presents were delivered to {} houses".format(len(deliveries)))

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
    if h[0:6] == '000000': # h[0:5] == '00000' for part 1
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

# --------------------------------------------
# Day 8 part 1
# --------------------------------------------
codeLength = 0
stringLength = 0

f = open('day8.txt', 'r')
for l in f:
    l = l.strip()
    codeLength += len(l)
    stringLength += len(l.encode('utf-8').decode('unicode_escape')) - 2 # subtract apostrophes

print("The size difference of the representations is {}".format(codeLength - stringLength))

# --------------------------------------------
# Day 8 part 2
# --------------------------------------------
codeLength = 0
encodedLength = 0

f = open('day8.txt', 'r')
for l in f:
    l = l.strip()
    codeLength += len(l)
    encodedLength += len(l) + l.count('\\') + l.count('"') + 2

print("The size difference of the representations is {}".format(encodedLength - codeLength))

# --------------------------------------------
# Day 9 part 1 & 2
# --------------------------------------------
import itertools
cities = set([])
distances = {}

f = open('day9.txt', 'r')
for l in f:
    l = l.strip()
    w = l.split('=')
    d = w[-1]
    cs = w[0].split(' ')
    cs = (cs[0], cs[2])
    cities.add(cs[0])
    cities.add(cs[1])
    distances[cs] = int(d) # store in both directions
    distances[(cs[1], cs[0])] = int(d)

bestPath, bestDist = None, np.infty
worstPath, worstDist = None, 0

for i in itertools.permutations(cities):
    d = 0
    for idx in range(len(i) - 1):
        d += distances[(i[idx], i[idx+1])]
    if d < bestDist:
        bestDist, bestPath = d, i
    if d > worstDist:
        worstDist, worstPath = d, i

print("Best path is {} with distance {}".format(bestPath, bestDist))
print("worst path is {} with distance {}".format(worstPath, worstDist))

# --------------------------------------------
# Day 10 part 1 & 2
# --------------------------------------------
seq = '1321131112'
outSeq = ''

for i in range(50): # 40 for the first part
    print("Iteration {}, sequence has length {}".format(str(i), len(seq)))
    idx = 0
    while idx < len(seq):
        e = seq[idx]
        occurrances = 0
        while idx < len(seq) and seq[idx] == e:
            idx += 1
            occurrances += 1

        outSeq += str(occurrances) + str(e)
    seq = outSeq
    outSeq = ''

print("Resulting sequence has length {}".format(len(seq)))

# --------------------------------------------
# Day 11 part 1 & 2
# --------------------------------------------
import itertools

def valid(pwd):
    # exclude i,o,l
    if pwd.count('i') + pwd.count('o') + pwd.count('l') > 0:
        return False
    
    # find doubles 
    # WARNING: letters of pairs are required to be different (not 'aatlgaa') but are not yet checked for that!
    if sum([1 for _,g in itertools.groupby(pwd) if len(list(g)) > 1]) < 2:
        return False

    # find ascending row of 3
    good = False
    for i, c in enumerate(pwd[:-2]):
        if ord(pwd[i+1]) == ord(c) + 1:
            if ord(pwd[i+2]) == ord(c) + 2:
                good = True
    return good

neg_examples = ['hijklmmn', 'abbceffg', 'abbcegjk']
pos_examples = ['abcdffaa', 'ghjaabcc']

for s in neg_examples:
    assert(valid(s) == False)
for s in pos_examples:
    assert(valid(s) == True)

def increment(pwd):
    pwd = list(pwd) # string doesn't allow assignments to positions, so transform to list of char
    alphabet_start = ord('a')
    alphabet_end = ord('z')

    carry = 1
    for idx, c in reversed(list(enumerate(pwd))): # walk backwards along list but remember index into pwd
        if carry == 0:
            break
        ci = ord(c) + 1
        if ci > alphabet_end:
            ci = alphabet_start
            carry = 1
        else:
            carry = 0
        pwd[idx] = chr(ci) # update the character to the new value
    return ''.join(pwd) # transform back to string

def findNextPwd(old_pwd):
    new_pwd = increment(old_pwd)
    while(not valid(new_pwd)):
        # print(new_pwd, ' is not valid')
        new_pwd = increment(new_pwd)
    return new_pwd

assert(findNextPwd('abcdefgh') == pos_examples[0])
assert(findNextPwd('ghijklmn') == pos_examples[1])

old_pwd = 'hepxcrrq'
new_pwd = findNextPwd(old_pwd)
print("Next valid password is ", new_pwd)
print("Next valid password is ", findNextPwd(new_pwd))

# --------------------------------------------
# Day 12 part 1
# --------------------------------------------
import json
with open('day12.json', 'r') as f:
    root = json.load(f)

def parse(node):
    accumulated = 0
    if isinstance(node, dict):
        for v in node.values():
            accumulated += parse(v)
    elif isinstance(node, list):
        for v in node:
            accumulated += parse(v)
    elif isinstance(node, int):
        return node

    return accumulated

print("Overall sum: {}".format(parse(root)))

# --------------------------------------------
# Day 12 part 2
# --------------------------------------------
import json
with open('day12.json', 'r') as f:
    root = json.load(f)

def parseNoRed(node):
    accumulated = 0
    if isinstance(node, dict):
        values = list(node.values())
        if 'red' not in values:
            for v in node.values():
                accumulated += parseNoRed(v)
    elif isinstance(node, list):
        for v in node:
            accumulated += parseNoRed(v)
    elif isinstance(node, int):
        return node

    return accumulated

print("Overall sum without red: {}".format(parseNoRed(root)))

# --------------------------------------------
# Day 13 part 1
# --------------------------------------------
import itertools
persons = set([])
happiness = {}

f = open('day13.txt', 'r')
for l in f:
    l = l.strip()
    w = l.split(' ')
    p1 = w[0]
    p2 = w[-1][:-1]
    persons.add(p1)
    persons.add(p2)
    h = int(w[3])
    if w[2] == 'lose':
        h *= -1
    happiness[(p1, p2)] = h

def findBestSeating(persons, happiness):
    bestSeating, bestHappy = None, 0

    for i in itertools.permutations(persons):
        d = 0
        for idx in range(len(i) - 1):
            d += happiness[(i[idx], i[idx+1])]
            d += happiness[(i[idx+1], i[idx])]
        d += happiness[(i[-1], i[0])] # add last link to close circle
        d += happiness[(i[0], i[-1])] # add last link to close circle

        if d > bestHappy:
            bestHappy, bestSeating = d, i
    return bestSeating, bestHappy

bestSeating, bestHappy = findBestSeating(persons, happiness)

print("Best path is {} with distance {}".format(bestSeating, bestHappy))

# --------------------------------------------
# Day 13 part 2
# --------------------------------------------
for p in persons:
    happiness[('me', p)] = 0
    happiness[(p, 'me')] = 0
persons.add('me')

bestSeating, bestHappy = findBestSeating(persons, happiness)

print("Best path is {} with distance {}".format(bestSeating, bestHappy))

# --------------------------------------------
# Day 14 part 1
# --------------------------------------------
class Reindeer:
    def __init__(self, line):
        line = line.strip()
        w = line.split()
        self.name = w[0]
        self._speed = int(w[3])
        self._moveTime = int(w[6])
        self._restTime = int(w[-2])
        self._timeToStateChange = self._moveTime
        self._inMovingState = True
        self.position = 0
        self.points = 0 # for part 2

    def simulateSecond(self):
        if self._timeToStateChange == 0:
            self._inMovingState = not self._inMovingState
            if self._inMovingState:
                self._timeToStateChange = self._moveTime
            else:
                self._timeToStateChange = self._restTime

        if self._inMovingState:
            self.position += self._speed
        self._timeToStateChange -= 1

reindeers = []
f = open('day14.txt', 'r')
for l in f:
    reindeers.append(Reindeer(l))

numSeconds = 2503
# numSeconds = 1000
for t in range(0, numSeconds):
    for r in reindeers:
        r.simulateSecond()

def findBestReindeer(key=lambda x: x.position):
    bestDist = 0
    bestReindeer = None
    for r in reindeers:
        if bestDist < key(r):
            bestDist = key(r)
            bestReindeer = r
    return bestReindeer

winner = findBestReindeer()
print("{} ran the furthest in {} seconds: {} km".format(winner.name, numSeconds, winner.position))

# --------------------------------------------
# Day 14 part 2
# --------------------------------------------
def findBestReindeers():
    bestDist = 0
    bestReindeer = []
    for r in reindeers:
        if bestDist < r.position:
            bestDist = r.position
            bestReindeer = [r]
        elif bestDist == r.position:
            bestReindeer.append(r)
    return bestReindeer

reindeers = []
f = open('day14.txt', 'r')
# f = open('day14-example.txt', 'r')
for l in f:
    reindeers.append(Reindeer(l))

numSeconds = 2503
# numSeconds = 1000
for t in range(0, numSeconds):
    for r in reindeers:
        r.simulateSecond()

    rs = findBestReindeers()
    for i in rs:
        i.points += 1

winner = findBestReindeer(key=lambda x: x.points)
print("{} collected the most points: {}".format(winner.name, winner.points))

# --------------------------------------------
# Day 15 part 1
# --------------------------------------------
class Ingredient:
    def __init__(self, line):
        self.name, propertyString = line.split(':')
        ps = propertyString.split(',')
        self.properties = {}
        for p in ps:
            t = p.strip().split(' ')
            self.properties[t[0]] = int(t[1])

    def __mul__(self, other):
        assert(isinstance(other, int))
        res = {}
        for p, v in self.properties.iteritems():
            res[p] = v * other
        return res

def add(dictA, dictB):
    if dictB is None:
        return dictA
    assert(len(dictA) == len(dictB))
    res = {}
    for k,v in dictA.iteritems():
        assert(k in dictB)
        res[k] = v + dictB[k]
    return res

def evaluate(teaspoons, ingredients, calorieLimit=None):
    s = None
    for t,i in zip(teaspoons, ingredients):
        s = add(i*t, s)

    prod = 1
    for k,v in s.iteritems():
        if calorieLimit != None and k == 'calories' and v != calorieLimit:
            return 0
        if not k == 'calories':
            prod *= max(0, v)
    return prod

ingredients = []
f = open('day15.txt', 'r')
for l in f:
    ingredients.append(Ingredient(l.strip()))

best = (None, 0)
for a in range(1,100):
    for b in range(1,100):
        for c in range(1,100):
            d = 100 - a - b - c 
            if d < 0: 
                break
            teaspoons = [a,b,c,d]
            e = evaluate(teaspoons, ingredients)
            if e > best[1]:
                best = (teaspoons, e)

print("Best combination is {} with value {}".format(best[0], best[1]))

best = (None, 0)
for a in range(1,100):
    for b in range(1,100):
        for c in range(1,100):
            d = 100 - a - b - c 
            if d < 0: 
                break
            teaspoons = [a,b,c,d]
            e = evaluate(teaspoons, ingredients, calorieLimit=500)
            if e > best[1]:
                best = (teaspoons, e)

print("Best combination with calorieLimit 500 is {} with value {}".format(best[0], best[1]))

# --------------------------------------------
# Day 16 part 1
# --------------------------------------------
cues = ["children: 3","cats: 7","samoyeds: 2",
            "pomeranians: 3","akitas: 0","vizslas: 0",
            "goldfish: 5","trees: 3","cars: 2","perfumes: 1"]

def getAuntAndProps(line):
    indexOfSeparator = line.find(':')
    aunt = line[:indexOfSeparator]
    propList = line[indexOfSeparator+1:]
    props = map(str.strip, propList.split(','))
    return aunt, props

# Warning, this is not really the best check, there might be contradictions!
def numMatches(props):
    return sum([1 for p in props if p in cues])

best = None

f = open('day16.txt', 'r')
for l in f:
    aunt, props = getAuntAndProps(l)
    matches = numMatches(props)
    if best is None or matches > best[2]:
        best = (aunt, props, matches)

print("Best matching aunt is {} with {}".format(best[0], best[1]))

# --------------------------------------------
# Day 16 part 2
# --------------------------------------------
cues = ["children: 3","samoyeds: 2",
            "akitas: 0","vizslas: 0",
            "cars: 2","perfumes: 1"]

def getAuntAndProps(line):
    indexOfSeparator = line.find(':')
    aunt = line[:indexOfSeparator]
    propList = line[indexOfSeparator+1:]
    props = map(str.strip, propList.split(','))
    return aunt, props

# Warning, this is not really the best check, there might be contradictions!
def numMatches(props):
    m = 0
    for p in props:
        s, n = p.split(':')
        if 'cats' in p and int(n) > 7:
            m += 1
        elif 'trees' in p and int(n) > 3:
            m += 1
        elif 'pomeranians' in p and int(n) < 3:
            m += 1
        elif 'goldfish' in p and int(n) < 5:
            m += 1
        elif p in cues:
            m += 1

    return m

best = None

f = open('day16.txt', 'r')
for l in f:
    aunt, props = getAuntAndProps(l)
    matches = numMatches(props)
    if best is None or matches > best[2]:
        best = (aunt, props, matches)

print("Best matching aunt is {} with {}".format(best[0], best[1]))

# --------------------------------------------
# Day 17 part 1
# --------------------------------------------
import itertools
# containers = [20, 15, 10, 5, 5]
# targetCapacity = 25

containers = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
targetCapacity = 150

goodCombinations = 0
for i in range(1, len(containers)):
    for c in itertools.combinations(containers, i):
        if sum(c) == targetCapacity:
            print(c)
            goodCombinations += 1

print("Found {} combinations that fit 150".format(goodCombinations))

# --------------------------------------------
# Day 17 part 2
# --------------------------------------------
# counted in logs: 17 ways of combining 4 containers

# --------------------------------------------
# Day 18 part 1
# --------------------------------------------
import numpy as np
import scipy.signal
grid = []
f = open('day18.txt', 'r')
for l in f:
    l = l.strip()
    row = []
    for i in l:
        if i == '.':
            row.append(0)
        else:
            row.append(1)
    grid.append(row)

grid = np.array(grid)
kernel = np.array([[1,1,1], [1,0,1], [1,1,1]])
numIterations = 100

for i in range(numIterations):
    activeNeighbors = scipy.signal.convolve2d(grid, kernel, mode='same')
    twoActive = activeNeighbors == 2
    threeActive = activeNeighbors == 3
    nextGrid = np.zeros_like(grid)
    nextGrid[grid == 1] = np.logical_or(twoActive, threeActive)[grid == 1].astype(int)
    nextGrid[grid == 0] = threeActive[grid == 0].astype(int)
    grid = nextGrid

print("Grid has {} lights switched on".format(np.count_nonzero(grid)))

# --------------------------------------------
# Day 18 part 2
# --------------------------------------------
import numpy as np
import scipy.signal
grid = []
f = open('day18.txt', 'r')
for l in f:
    l = l.strip()
    row = []
    for i in l:
        if i == '.':
            row.append(0)
        else:
            row.append(1)
    grid.append(row)

grid = np.array(grid)
# enable corners
grid[0,0] = 1
grid[0,-1] = 1
grid[-1,-1] = 1
grid[-1,0] = 1
kernel = np.array([[1,1,1], [1,0,1], [1,1,1]])
numIterations = 100

for i in range(numIterations):
    activeNeighbors = scipy.signal.convolve2d(grid, kernel, mode='same')
    twoActive = activeNeighbors == 2
    threeActive = activeNeighbors == 3
    nextGrid = np.zeros_like(grid)
    nextGrid[grid == 1] = np.logical_or(twoActive, threeActive)[grid == 1].astype(int)
    nextGrid[grid == 0] = threeActive[grid == 0].astype(int)
    grid = nextGrid
    # enable corners
    grid[0,0] = 1
    grid[0,-1] = 1
    grid[-1,-1] = 1
    grid[-1,0] = 1

print("Grid has {} lights switched on".format(np.count_nonzero(grid)))

# --------------------------------------------
# Day 19 part 1
# --------------------------------------------
import re

rules = []
origin = None
f = open('day19.txt', 'r')
foundEmptyLine = False
for l in f:
    l = l.strip()
    # quit after all rules have been read
    if l == '':
        foundEmptyLine = True
    elif foundEmptyLine:
        origin = l
    else:
        r = l.split('=')
        r[1] = r[1][1:]
        r = map(str.strip, r)
        rules.append(r)

results = set([]) # use a set to remove duplicates
for r in rules:
    # find all occurrences
    occurrences = [m.start() for m in re.finditer(r[0], origin)]
    for o in occurrences:
        transformed = origin[:o] + r[1] + origin[o+len(r[0]):]
        results.add(transformed)

print("Found {} different molecules".format(len(results)))

# --------------------------------------------
# Day 19 part 2
# --------------------------------------------
import re

rules = []
target = None
f = open('day19.txt', 'r')
foundEmptyLine = False
for l in f:
    l = l.strip()
    # quit after all rules have been read
    if l == '':
        foundEmptyLine = True
    elif foundEmptyLine:
        target = l
    else:
        r = l.split('=')
        r[1] = r[1][1:]
        r = map(str.strip, r)
        rules.append(r)

results = set(['e']) # use a set to remove duplicates
nextResults = set([])
steps = 0
while target not in results:
    for w in results:
        for r in rules:
            # find all occurrences
            occurrences = [m.start() for m in re.finditer(r[0], w)]
            for o in occurrences:
                transformed = w[:o] + r[1] + w[o+len(r[0]):]
                nextResults.add(transformed)
    results = set(nextResults)
    nextResults = set([])
    steps += 1

print("Needed {} steps to get to medicine".format(steps))

# --------------------------------------------
# Day 20 part 1
# --------------------------------------------
import sys
def numPresents(n):
    p = 0
    for i in xrange(1, n+1):
        if n % i == 0:
            p += 10 * i
    return p

j = 1000000 # found by simple trying
while numPresents(j) < 34000000:
    j += 1 
    if j % 1000 == 0:
        print('{}'.format(j))

print("\nThe first house to get 34000000 presents is {}".format(i))

# --------------------------------------------
# Day 23 part 1
# --------------------------------------------
# read instructions
f = open('day23.txt', 'r')
instructions = []
for l in f:
    instructions.append(l.strip().split(' '))

# init variables - use lists because they are mutable instead of pure intergers!
a = [0]
b = [0]
instructionPtr = 0
def getVarByName(name):
    # we only compare the first char, to ignore the trailing comma in jumps
    if name[0] == 'a':
        return a
    elif name[0] == 'b':
        return b
    else:
        raise ArgumentException

# process
while 0 <= instructionPtr < len(instructions):
    print("InstructionPtr: {}".format(instructionPtr))
    i = instructions[instructionPtr]
    print("\tInstruction: {}".format(i))

    if i[0] == 'hlf':
        var = getVarByName(i[1])
        var[0] /= 2
        print("Executed hlf {} -> {}".format(i[1], var[0]))
    elif i[0] == 'tpl':
        var = getVarByName(i[1])
        var[0] *= 3
        print("Executed tpl {} -> {}".format(i[1], var[0]))
    elif i[0] == 'inc':
        var = getVarByName(i[1])
        var[0] += 1
        print("Executed inc {} -> {}".format(i[1], var[0]))
    elif i[0] == 'jmp':
        instructionPtr += int(i[1])
        print("Executed jmp {} -> {}".format(i[1], instructionPtr))
    elif i[0] == 'jie':
        var = getVarByName(i[1])
        if var[0] % 2 == 0:
            instructionPtr += int(i[2])
            print("Executed jie {}(={}) {} -> {}".format(i[1], var[0], i[2], instructionPtr))
            continue
    elif i[0] == 'jio':
        var = getVarByName(i[1])
        if var[0] == 1:
            instructionPtr += int(i[2])
            print("Executed jio {}(={}) {} -> {}".format(i[1], var[0], i[2], instructionPtr))
            continue

    instructionPtr += 1

# output values
print("Variables have values a={}, b={}".format(a,b))



