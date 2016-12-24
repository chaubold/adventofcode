//: Playground - noun: a place where people can play

import Cocoa

func loadInput() -> String {
    // load file
    do {
        return try String(contentsOfFile: "/Users/chaubold/Desktop/adventofcode/2016/08/input.txt")
    }
    catch _ as NSError {
        print("Couldn't load file")
        return String("")
    }
}

var fileContents = loadInput()

// split into lines
let lineArray = fileContents.characters.split { (c: Character) -> Bool in return c == "\n" || c == "\r\n" }.map(String.init)
//lineArray.count

var screen = Array(repeating: Array(repeating: false, count: 50), count: 6)

func printScreen() {
    print("Current Screen: ")
    for line in screen {
        for pixel in line{
            if pixel {
                print("#", terminator: "")
            }
            else {
                print(".", terminator: "")
            }
        }
        print("")
    }
}

//printScreen()

func turnOn(x: Int, y: Int) {
    for i in 0..<x {
        for j in 0..<y {
            screen[j][i] = true
        }
    }
}

//turnOn(x: 10, y: 3)
//printScreen()

func rotateRow(_ rowIdx: Int, by: Int) {
    for _ in 0..<by {
        screen[rowIdx].insert(screen[rowIdx].remove(at: 49), at: 0)
    }
}

//rotateRow(2, by: 10)
//printScreen()

func rotateCol(_ colIdx: Int, by: Int) {
    var tempA, tempB : Bool
    for _ in 0..<by {
        tempA = screen[0][colIdx]
        for i in 1..<6 {
            tempB = screen[i][colIdx]
            screen[i][colIdx] = tempA
            swap(&tempA, &tempB)
        }
        screen[0][colIdx] = tempA
    }
}

//rotateCol(2, by: 3)
//printScreen()

//var line = "rect 3x2"
//var line = "rotate column x=10 by 4"
//print(line)


for line in lineArray {
    print(line)
    let lineParts = line.characters.split { (c: Character) -> Bool in return c == " " || c == "x" || c == "=" }.map(String.init)
    
    if lineParts[0] == "rect" {
        turnOn(x: Int(lineParts[1])!, y: Int(lineParts[2])!)
    }
    else if lineParts[0] == "rotate" {
        if lineParts[1] == "row" {
            rotateRow(Int(lineParts[3])!, by: Int(lineParts[5])!)
        }
        else if lineParts[1] == "column" {
            rotateCol(Int(lineParts[2])!, by: Int(lineParts[4])!)
        }
        else {
            print("Should not get here, problems with \(line)")
        }
    }
    else {
        print("Should not get here, problems with \(line)")
    }
}

printScreen()

func countActive() -> Int {
    var numActive : Int = 0
    for line in screen {
        for pixel in line{
            if pixel {
                numActive += 1
            }
        }
    }
    return numActive
}

print("\(countActive()) lights are active at the end")
