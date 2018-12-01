import * as fs from "fs";

function run(input: string) {
    let lines = input.split('\n');
    let frequency: number = 0;
    let previouslySeenNumbers: Set<number> = new Set([]);
    let iteration = 0;
    while (true) {
        for (let l of lines) {
            frequency += parseInt(l);
            if (previouslySeenNumbers.has(frequency)) {
                console.log("Found double frequency: " + frequency);
                return
            } else {
                previouslySeenNumbers.add(frequency);
            }
        }
        console.log("After iteration " + iteration + ", found frequency " + frequency)
        iteration += 1;
    }
}

fs.readFile('input.txt', {}, (err, data) => {
    if (err) {
        return console.error(err);
    }
    run(data.toString());
})
console.log("Done");