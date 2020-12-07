import * as fs from "fs";

function containsLetterDuplicate(id: string, numTimes: number): boolean {
    let occurrencesPerLetter = new Map<string, number>()

    for (let letter of id) {
        if (occurrencesPerLetter.has(letter)) {
            occurrencesPerLetter.set(letter, 1 + occurrencesPerLetter.get(letter))
        } else {
            occurrencesPerLetter.set(letter, 1)
        }
    }

    let didFindRightOccurrence = false
    occurrencesPerLetter.forEach((num: number, letter: string) => {
        if (num == numTimes) {
            didFindRightOccurrence = true
        }
    });

    return didFindRightOccurrence
}

function letterDifference(idA: string, idB: string): string {
    if (idA.length != idB.length) {
        return null
    }

    let idxOfDifferingLetter = -1
    for (let idx = 0; idx < idA.length; idx++) {
        if (idA[idx] != idB[idx]) {
            if (idxOfDifferingLetter >= 0) {
                return null
            } else {
                idxOfDifferingLetter = idx
            }
        }
    }

    if (idxOfDifferingLetter >= 0) {
        return idA.slice(0, idxOfDifferingLetter).concat(idB.slice(idxOfDifferingLetter + 1))
    }
    return null
}

function run(input: string) {
    let lines = input.split('\n')
    let numDoubles = 0
    let numTriples = 0

    for (let l of lines) {
        if (containsLetterDuplicate(l, 2)) {
            numDoubles += 1
        }
        if (containsLetterDuplicate(l, 3)) {
            numTriples += 1
        }
    }

    console.log(numDoubles * numTriples)

    for (let i = 0; i < lines.length; i++) {
        for (let j = i + 1; j < lines.length; j++) {
            let res = letterDifference(lines[i], lines[j])
            if (res != null) {
                console.log(res)
                break
            }
        }
    }

    console.log("Done")
}

fs.readFile('input.txt', {}, (err, data) => {
    if (err) {
        return console.error(err);
    }
    run(data.toString());
})