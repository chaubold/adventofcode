from collections import Counter
s = 'aaaaa-bbb-z-y-x-123[abxyz]'
checksum = s[-6:-1]
sectorId = int(s[-10:-7])
bla = s[:-11].replace('-','')

print(checksum, sectorId, histogram)

def computeChecksum(s):
     histogram = Counter(s)
     letters