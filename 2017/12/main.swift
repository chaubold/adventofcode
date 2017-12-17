import Foundation
var nodeNeighborDict : [Int:Set<Int>] = [:]

// actual processing
let inputStrings = try! String(contentsOfFile: "input.txt", encoding: String.Encoding.utf8).split(separator:"\n").map {String($0)}

for line in inputStrings
{
	let lineWithoutCommas = line.replacingOccurrences(of:",", with:" ")
	let words = lineWithoutCommas.split(separator:" ").map { String($0) }

	let rootId = Int(words[0])!
	let connectedIds = Set(words[2..<words.count].map {Int($0)!})
	if var neighborSet = nodeNeighborDict[rootId] {
		connectedIds.forEach{neighborSet.insert($0)}
	}
	else {
		nodeNeighborDict[rootId] = connectedIds
	}
}

print(nodeNeighborDict)

// find neighbors of 0:
func findNodeNeighbors(_ root: Int) -> Set<Int> {
	var neighborsOfNode = Set<Int>([])
	var priorityQueue = [root]

	for (node, neighborSet) in nodeNeighborDict {
		if neighborSet.contains(root) {
			priorityQueue.append(node)
		}
	}

	while !priorityQueue.isEmpty {
		let node = priorityQueue.removeFirst()
		// print("Processing node \(node)")
		if !neighborsOfNode.contains(node) {
			neighborsOfNode.insert(node)
			for neighbor in nodeNeighborDict[node] ?? [] {
				priorityQueue.append(neighbor)
			}
		}
	}
	return neighborsOfNode
}

let neighborsOfNull = findNodeNeighbors(0)
print("Node 0 has \(neighborsOfNull.count) neighbors")

// get num connected components
var remainingNodes = Set<Int>(nodeNeighborDict.keys)
var numConnectedComponents = 0
while !remainingNodes.isEmpty {
	numConnectedComponents += 1
	let nextUnusedNode = remainingNodes.removeFirst()
	let neighbors = findNodeNeighbors(nextUnusedNode)
	print("Node \(nextUnusedNode) has \(neighbors.count) neighbors")
	remainingNodes.subtract(neighbors)
}

print("Num connected components: \(numConnectedComponents)")