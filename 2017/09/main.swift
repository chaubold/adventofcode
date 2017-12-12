import Foundation

enum State {
    case garbage
    case group
    case cancelled
}

func getGroupScore(_ stream: String) -> (groupScore: Int, numGarbageChars: Int)
{
    // print("Evaluating stream: \(stream)")
    var stateStack : [State] = [.group]
    var groupScore = 0
    var numGarbageChars = 0
    for c in stream
    {
        if stateStack.last! == .cancelled {
            // print("\t\tSkipping \(c)")
            _ = stateStack.popLast()
        }
        else
        {
            switch c
            {
                case "{":
                    if stateStack.last! == .group {
                        let score = stateStack.filter{$0 == .group}.count
                        // print("Adding new group with score \(score)")
                        groupScore += score // add score
                        stateStack.append(.group)
                    }
                    else {
                        numGarbageChars += 1
                    }
                case "}":
                    if stateStack.last! == .group {
                        _ = stateStack.popLast()
                    }
                    else {
                        numGarbageChars += 1
                    }
                case "<":
                    if stateStack.last! == .group {
                        // print("\tFound new garbage group")
                        stateStack.append(.garbage)
                    }
                    else {
                        numGarbageChars += 1
                    }
                case ">":
                    if stateStack.last! == .garbage {
                        // print("\tExiting garbage group")
                        _ = stateStack.popLast()
                    }
                case "!":
                    if stateStack.last! != .cancelled {
                        // print("\t\tFound skip command")
                        stateStack.append(.cancelled)
                    }
                default:
                    if stateStack.last! == .garbage {
                        numGarbageChars += 1
                    }
            }
        }
    }

    return (groupScore, numGarbageChars)
}

assert(getGroupScore("{}").0 == 1)
assert(getGroupScore("{{{}}}").0 == 1 + 2 + 3)
assert(getGroupScore("{{},{}}").0 == 1 + 2 + 2)
assert(getGroupScore("{{{},{},{{}}}}").0 == 1 + 2 + 3 + 3 + 3 + 4)
assert(getGroupScore("{<a>,<a>,<a>,<a>}").0 == 1)
assert(getGroupScore("{{<ab>},{<ab>},{<ab>},{<ab>}}").0 == 1 + 2 + 2 + 2 + 2)
assert(getGroupScore("{{<!!>},{<!!>},{<!!>},{<!!>}}").0 == 1 + 2 + 2 + 2 + 2)
assert(getGroupScore("{{<a!>},{<a!>},{<a!>},{<ab>}}").0 == 1 + 2)

let stream = try! String(contentsOfFile: "input.txt", encoding: String.Encoding.utf8)
let (groupScore, numGarbageChars) = getGroupScore(stream)
print("GroupScore: \(groupScore), garbage chars \(numGarbageChars)")