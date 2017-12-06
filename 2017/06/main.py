import numpy as np

memoryBanks = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

def redistribute(bankIndex):
    numBlocks = memoryBanks[bankIndex]
    memoryBanks[bankIndex] = 0
    for i in range(bankIndex+1, bankIndex+numBlocks+1):
        memoryBanks[i % len(memoryBanks)] += 1

history = []
while tuple(memoryBanks) not in history:
    history.append(tuple(memoryBanks))
    maxIdx = np.argmax(memoryBanks)
    print(f"redistributing bank {maxIdx} with {memoryBanks[maxIdx]} blocks")
    redistribute(maxIdx)
    print(memoryBanks)

print(f"Saw {len(history)} different configurations before returning to a known one")
idx = history.index(tuple(memoryBanks))
print(f"The config was seen before at idx {idx}, which makes it a cycle length of {len(history) - idx}") 