import Foundation

struct Generator {
	private var previousValue : UInt64
	private let factor : UInt64
	private let divisor : UInt64 = 2147483647
	private let criterium : UInt64

	init(startingValue : UInt64, factor : UInt64, criterium : UInt64) {
		previousValue = startingValue
		self.factor = factor
		self.criterium = criterium
	}

	mutating func getNext() -> UInt64 {
		previousValue = (previousValue * factor) % divisor
		return previousValue
	}

	mutating func getNextMatching() -> UInt64 {
		var value = getNext()
		while value % criterium != 0 {
			value = getNext()
		}
		return value
	}
}

// test
// var a = Generator(startingValue: 65, factor: 16807, criterium : 4)
// var b = Generator(startingValue: 8921, factor: 48271, criterium : 8)

// real:
var a = Generator(startingValue: 722, factor: 16807, criterium : 4)
var b = Generator(startingValue: 354, factor: 48271, criterium : 8)

// var matchCount = 0
// for _ in 0..<40000000
// {
// 	let resultA = a.getNext()
// 	let resultB = b.getNext()
	
// 	if UInt16(truncatingIfNeeded:resultA) == UInt16(truncatingIfNeeded:resultB) {
// 		// print("A generated \(resultA)")
// 		// print("B generated \(resultB)")
// 		// print("Last 16 bits match!")
// 		matchCount += 1
// 	}
// }

// print("Last 16 bits matched \(matchCount) times")

// ------------------------------------------------------------------------
// Part 2
// ------------------------------------------------------------------------

var matchCount = 0
for _ in 0..<5000000
// for _ in 0..<1060
{
	let resultA = a.getNextMatching()
	let resultB = b.getNextMatching()
	
	if UInt16(truncatingIfNeeded:resultA) == UInt16(truncatingIfNeeded:resultB) {
		// print("A generated \(resultA)")
		// print("B generated \(resultB)")
		// print("Last 16 bits match!")
		matchCount += 1
	}
}

print("Last 16 bits matched \(matchCount) times")
