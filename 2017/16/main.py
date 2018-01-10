# programList = list('abcde')

# with open('test_input.txt', 'r') as f:
# 	instructions = f.read().strip().split(',')

programList = list('abcdefghijklmnop')
startingValue = programList[:]

with open('input.txt', 'r') as f:
 	instructions = f.read().strip().split(',')

def applyInstructions(programList):
	for i in instructions:
		# print("current instruction: {}".format(i))
		if i[0] == 's':
			steps = int(i[1:])
			programList = programList[-steps:] + programList[0:-steps]
		elif i[0] == 'x':
			positions = i[1:].split('/')
			pos1, pos2 = [int(p) for p in positions]
			# print("\tFound positions {} and {}".format(pos1, pos2))
			programList[pos1], programList[pos2] = programList[pos2], programList[pos1]
		elif i[0] == 'p':
			names = i[1:].split('/')
			pos1, pos2 = [programList.index(n) for n in names]
			# print("\tFound positions {} and {}".format(pos1, pos2))
			programList[pos1], programList[pos2] = programList[pos2], programList[pos1]
		# print("\tnew program list: {}".format(programList))
	return programList

numIters = None
for c in range(10000):
	programList = applyInstructions(programList)
	print('\t' + ''.join(programList))

	if programList == startingValue:
		print("Found equivalent configuration after {} iterations!".format(c))
		numIters = c+1
		break

remainingIterations = 1000000000 % numIters
print("Running shortcut: only {} iters to do".format(remainingIterations))
for c in range(remainingIterations):
	programList = applyInstructions(programList)

print(''.join(programList))