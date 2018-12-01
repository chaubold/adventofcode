import Foundation

struct CircularList {
  var list : [Int]
  
  init(length: Int) {
    list = [Int](0..<length)
  }
  
  mutating func rotate(from startIndex:Int, length:Int) {
    let endIndex = startIndex + length
    
    if endIndex <= list.count {
      list.replaceSubrange(startIndex..<endIndex, with: list[startIndex..<endIndex].reversed())
    } else {
      let wrappedAroundEndIndex = endIndex % list.count
      let reversedElements = [Int]((list[startIndex...] + list[..<wrappedAroundEndIndex]).reversed())
      let splitIndex = list.count - startIndex
      list[startIndex...] = reversedElements[..<splitIndex]
      list[..<wrappedAroundEndIndex] = reversedElements[splitIndex...]
    }
  }
}

func tieKnots(in list:CircularList, lengths:[Int], numRounds:Int = 1) -> CircularList {
  var knotList = list
  var skipSize = 0
  var currentPos = 0
  for _ in 0..<numRounds {
    for l in lengths {
      if l >= knotList.list.count {
        continue
      }
      
      knotList.rotate(from: currentPos, length: l)
      assert(knotList.list.count == list.list.count)
      currentPos = (currentPos + skipSize + l) % knotList.list.count
      skipSize += 1
    }
  }
  
  return knotList
}
//
//let testList = CircularList(length: 5)
//let testLengths = [3, 4, 1, 5]
//let testResultList = tieKnots(in: testList, lengths: testLengths)
//print("List at the end: \(testResultList.list)")
//
let inputURL = Bundle.main.url(forResource: "input", withExtension: "txt")!
//let input = try! String(contentsOf: inputURL)
//let lengths = input.split(separator: ",").map { Int($0)! }
//let list = CircularList(length: 256)
//let resultList = tieKnots(in: list, lengths: lengths)
//
//print("List at the end: \(resultList.list)")
//print("\nMultiplying the first two elements yields: \(resultList.list[0] * resultList.list[1])")

var inputAsBytes = try! Data(contentsOf: inputURL)
inputAsBytes.append(contentsOf: [17, 31, 73, 47, 23])
let lengths = inputAsBytes.map { Int($0) }
let list = CircularList(length: 256)
let resultList = tieKnots(in: list, lengths: lengths, numRounds:64)

print("List at the end: \(resultList.list)")

var xorBlocks = [UInt8]()
var hexString : String = ""
for i in 0..<16 {
  var val : UInt8 = 0
  for j in 0..<16 {
    val = val ^ UInt8(resultList.list[i * 16 + j])
  }
  xorBlocks.append(val)
  hexString.append(contentsOf: String(format:"%02X", val))
}
print(xorBlocks)
print(hexString.lowercased())
