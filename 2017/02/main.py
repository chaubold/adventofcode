with open('input.txt', 'r') as f:
	lines = f.readlines()

lines = [[int(v) for v in l.split('\t')] for l in lines]

checksums = 0
for l in lines:
	checksums += max(l) - min(l)

print(checksums)

divs = 0
for l in lines:
	for a in l:
		for b in l:
			if a > b and a % b == 0:
				divs += a // b

print(divs)

