import Foundation

enum Op: String
{
    case increase = "inc"
    case decrease = "dec"
}

enum Relation : String
{
    case greater = ">"
    case less = "<"
    case greaterEqual = ">="
    case lessEqual = "<="
    case equal = "=="
    case notEqual = "!="
}

struct Condition 
{
    let register : String 
    let relation : Relation
    let value : Int

    func isValid(for registerValues: [String : Int]) -> Bool
    {
        let regValue : Int
        if let v = registerValues[register] 
        {
            regValue = v
        }
        else {
            print("Register \(register) was not set yet, setting to zero")
            regValue = 0
        }

        // let regValue = registerValues[register]
        switch relation
        {
            case .greater:
                return regValue > value
            case .less:
                return regValue < value
            case .greaterEqual:
                return regValue >= value
            case .lessEqual:
                return regValue <= value
            case .equal:
                return regValue == value
            case .notEqual:
                return regValue != value
        }
    }
}

func parseLine(line: String) -> (destReg: String, op: Op, value: Int, condition: Condition)
{
    let words = line.split(separator:" ").map { String($0) }
    let cond = Condition(register: words[4], relation: Relation(rawValue: words[5])!, value: Int(words[6])!)
    return (words[0], Op(rawValue: words[1])!, Int(words[2])!, cond)
}

// actual processing
let inputStrings = try! String(contentsOfFile: "input.txt", encoding: String.Encoding.utf8).split(separator:"\n").map {String($0)}
var registerValues : [String : Int] = [:]
var maxValue = 0
for line in inputStrings
{
    let (destReg, op, value, condition) = parseLine(line:line)
    if condition.isValid(for: registerValues) {
        print("Condition was true, executing line \(line)")
        var regValue : Int = 0
        if let v = registerValues[destReg] 
        {
            regValue = v
        }

        switch op 
        {
            case .increase:
                regValue += value
            case .decrease:
                regValue -= value
        }
        print("Setting value of register \(destReg) to \(regValue)")
        registerValues[destReg] = regValue
        maxValue = max(regValue, maxValue)
    }
    else {
        print("Condition is NOT true, NOT executing line \(line)")
    }
}

print("Maximum register value at the end is \(registerValues.values.max()!)")
print("Maximum register value overall was \(maxValue)")
