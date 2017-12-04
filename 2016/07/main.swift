import Foundation
let inputString = String(contentsOf: "input.txt", encoding: String.Encoding.utf8)

func checkString(input: String) -> Bool {
    // print("Looking at \(input)")
    var listOfChars = [Character](input.characters)
    var nextOptionalBracketIndex = listOfChars.index(of:"[")
    var resultIsValid : Bool? = nil 
    var insideBrackets = false

    while let nextBracketIndex = nextOptionalBracketIndex {
        // print("Walking inside=\(insideBrackets) until bracket at idx \(nextBracketIndex)")
        // process until next bracket
        if insideBrackets || resultIsValid == nil {
            for i in 0..<nextBracketIndex-3 {
                if(listOfChars[i] == listOfChars[i+3] && listOfChars[i+1] == listOfChars[i+2] && listOfChars[i] != listOfChars[i+1]) {
                    // print("Found matching pattern starting at idx \(i), inside=\(insideBrackets)")
                    resultIsValid = !insideBrackets // outside makes the result valid, inside makes it false
                }
            }
        }

        // toggle between inside and outside
        insideBrackets = !insideBrackets

        // strip away the part that we've already looked at
        listOfChars.removeFirst(nextBracketIndex+1)
        // print("Remaining string: \(String(listOfChars))")

        // find next bracket (if any)
        if insideBrackets {
            nextOptionalBracketIndex = listOfChars.index(of:"]")
        }
        else {
            nextOptionalBracketIndex = listOfChars.index(of:"[")
        }
    }

    // handle last block
    if insideBrackets || resultIsValid == nil {
        for i in 0..<listOfChars.count-3 {
            if(listOfChars[i] == listOfChars[i+3] && listOfChars[i+1] == listOfChars[i+2] && listOfChars[i] != listOfChars[i+1]) {
                // print("Found matching pattern starting at idx \(i), inside=\(insideBrackets)")
                resultIsValid = !insideBrackets // outside makes the result valid, inside makes it false
            }
        }
    }

    if resultIsValid != nil {
        return resultIsValid!
    }
    else {
        return false
    }
}

assert(checkString(input: "abba[mnop]qrst") == true)
assert(checkString(input: "abcd[bddb]xyyx") == false)
assert(checkString(input: "aaaa[qwer]tyui") == false)
assert(checkString(input: "ioxxoj[asdfgh]zxcvbn") == true)
assert(checkString(input: "ioxxoj[asdfgh]zxcvbn[abba]asdf") == false)
assert(checkString(input: "abcd[asdf]asdf[asdf]xyyx") == true)

var validIps = 0
for i in inputs {
    if checkString(input: i) {
        validIps += 1
    }
}

print("found \(validIps) valid IPs")