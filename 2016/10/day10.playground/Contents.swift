//: Playground - noun: a place where people can play

import Cocoa

//let input = ["value 5 goes to bot 2",
//    "bot 2 gives low to bot 1 and high to bot 0",
//    "value 3 goes to bot 1",
//    "bot 1 gives low to output 1 and high to bot 0",
//    "bot 0 gives low to output 2 and high to output 0",
//    "value 2 goes to bot 2"]

func loadInput() -> String {
    // load file
    do {
        return try String(contentsOfFile: "/Users/chaubold/Desktop/adventofcode/2016/10/input.txt")
    }
    catch _ as NSError {
        print("Couldn't load file")
        return String("")
    }
}

var fileContents = loadInput()

// split into lines
let input = fileContents.characters.split { (c: Character) -> Bool in return c == "\n" || c == "\r\n" }.map(String.init)

struct Directions {
    let lowString : String
    let low : Int
    let highString: String
    let high : Int
}

struct Bot {
    var values : [Int]
    let directions: Directions
    let key : Int
}

var botDict : [Int: Bot] = [:]
var outputDict : [Int: Bot] = [:]

// configure passing order
for line in input {
    let lineParts : [String] = line.characters.split { $0 == " " }.map(String.init)
    if lineParts[0] == "bot" {
        let low : Int = Int(lineParts[6])!
        let high : Int = Int(lineParts[11])!
        let d = Directions(lowString: lineParts[5], low: low, highString: lineParts[10], high: high)
        botDict[Int(lineParts[1])!] = Bot(values: [], directions: d, key: Int(lineParts[1])!)
    }
}

// configure inputs
for line in input {
    let lineParts : [String] = line.characters.split { $0 == " " }.map(String.init)
    if lineParts[0] == "value" {
        let botId : Int = Int(lineParts[5])!
        let value : Int = Int(lineParts[1])!
        botDict[botId]!.values.append(value)
    }
}

func passOn(bot: Bot) {
    if bot.values.contains(61) && bot.values.contains(17) {
        print("------ Bot \(bot.key) is responsible for comparing 61 and 17 ------")
    }
    
    var sortedValues : [Int] = bot.values.sorted()
    if bot.directions.lowString == "bot" {
        botDict[bot.directions.low]!.values.append(sortedValues[0])
        if botDict[bot.directions.low]!.values.count == 2 {
            passOn(bot: botDict[bot.directions.low]!)
        }
    }
    else {
        if outputDict[bot.directions.low] == nil {
            let d = Directions(lowString: "out", low: 0, highString: "out", high: 0)
            outputDict[bot.directions.low] = Bot(values: [], directions: d, key: bot.directions.low)
        }
        outputDict[bot.directions.low]!.values.append(sortedValues[0])
    }
    
    if bot.directions.highString == "bot" {
        botDict[bot.directions.high]!.values.append(sortedValues[1])
        if botDict[bot.directions.high]!.values.count == 2 {
            passOn(bot: botDict[bot.directions.high]!)
        }
    }
    else {
        if outputDict[bot.directions.high] == nil {
            let d = Directions(lowString: "out", low: 0, highString: "out", high: 0)
            outputDict[bot.directions.high] = Bot(values: [], directions: d, key: bot.directions.high)
        }
        outputDict[bot.directions.high]!.values.append(sortedValues[1])
    }
}

// pass on inputs
for (_, bot) in botDict {
    if bot.values.count == 2 {
        passOn(bot: bot)
    }
}

//print("\(botDict)")
//print("\(outputDict)")
print("Outputs 0,1,2 contain: \(outputDict[0]!.values), \(outputDict[1]!.values), and \(outputDict[2]!.values)")