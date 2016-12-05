from collections import Counter

def sortCompare(x, y):
    if x[1] == y[1]:
        return ord(x[0]) - ord(y[0])
    else:
        return y[1] - x[1]

def checkChecksum(s):
    expectedChecksum = s[-6:-1]
    sectorId = int(s[-10:-7])
    body = s[:-10]
    bodyNoDash = body.replace('-','')
    c = Counter(bodyNoDash)
    #mostCommon = c.most_common(5)
    mostCommon = [(k,v) for k,v in c.iteritems()]
    mostCommon.sort(cmp=sortCompare)
    mostCommon = mostCommon[:5]
    calculatedChecksum = ''.join([m[0] for m in mostCommon])

    # print("Found checksum: {}, expected {}".format(calculatedChecksum, expectedChecksum))

    if expectedChecksum == calculatedChecksum:
        message = []
        for c in body:
            if c == '-':
                message.append(' ')
            else:
                message.append(chr((ord(c)-ord('a')+sectorId)%26 + ord('a')))
        message = ''.join(message)
        if 'north' in message:
            print(s)
            print(message)
        return True, sectorId
    else:
        return False, 0

# test
s = 'aaaaa-bbb-z-y-x-123[abxyz]'
assert(checkChecksum(s)[0])
s = 'a-b-c-d-e-f-g-h-987[abcde]'
assert(checkChecksum(s)[0])
s = 'not-a-real-room-404[oarel]'
assert(checkChecksum(s)[0])
s = 'totally-real-room-200[decoy]'
assert(not checkChecksum(s)[0])

with open('input.txt', 'r') as f:
    sumOfSectorIds = 0
    for line in f:
        line = line.strip()
        sumOfSectorIds += checkChecksum(line)[1]
    print(sumOfSectorIds)
