use std::fs;

fn main() {
    println!("Day 01!");
    let contents = fs::read_to_string("input.txt").expect("Could not load file!");
    let mut numbers = Vec::new();
    for line in contents.lines() {
        let num : u32 = line.parse().expect("Could not parse line as number");
        numbers.push(num);
        // println!("Found number {}", num);
    }
    // println!("... Found {} numbers", numbers.len());

    for i in 0..numbers.len() {
        let a = numbers[i];
        for j in i+1..numbers.len() {
            let b = numbers[j];
            if a + b == 2020 {
                println!("{} + {} = {}. {} * {} = {}", a, b, a+b, a, b, a*b);
            }
        }
    }

    for i in 0..numbers.len() {
        let a = numbers[i];
        for j in i+1..numbers.len() {
            let b = numbers[j];
            for k in j+1..numbers.len() {
                let c = numbers[k];
                if a + b + c == 2020 {
                    println!("{} + {} + {} = {}. {} * {} * {} = {}", a, b, c, a+b+c, a, b, c, a*b*c);
                }
            }
        }
    }

    println!("Done.")
}
