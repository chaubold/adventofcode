
def isValid(passphrase):
    wordList = passphrase.split(' ')
    wordSet = set(wordList)
    return len(wordList) == len(wordSet)

assert isValid("aa bb cc dd ee")
assert not isValid("aa bb cc dd aa")
assert isValid("aa bb cc dd aaa")

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]
print(sum([1 for l in lines if isValid(l)]))

from collections import Counter

def isValid2(passphrase):
    wordList = passphrase.split(' ')
    counters = [Counter(w) for w in wordList]
    for i in range(len(counters)):
        for j in range(i + 1, len(counters)):
            if counters[i] == counters[j]:
                return False
    return True

assert isValid2('abcde fghij')
assert not isValid2('abcde xyz ecdab')
assert isValid2('a ab abc abd abf abj')
assert isValid2('iiii oiii ooii oooi oooo')
assert not isValid2('oiii ioii iioi iiio')

print(sum([1 for l in lines if isValid2(l)]))