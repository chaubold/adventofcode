use std::fs;
use std::collections::HashSet;

fn part1(contents: &String) {
    let mut answers = HashSet::new();
    let mut sum_answers_per_group = 0;
    for line in contents.lines() {
        if line.is_empty() {
            // finish
            sum_answers_per_group += answers.len();
            answers.clear();
        }
        else {
            // add to current tags
            for a in line.chars() {
                answers.insert(a);
            }
        }
    }

    println!("Total sum of answers per group: {}", sum_answers_per_group);
}

fn part2(contents: &String) {
    let mut answers = HashSet::new();
    let mut sum_answers_per_group = 0;
    let mut first_person = true;
    for line in contents.lines() {
        if line.is_empty() {
            // finish
            sum_answers_per_group += answers.len();
            answers.clear();
            first_person = true;
        }
        else {
            // add to current tags
            let mut person_answers = HashSet::new();
            for a in line.chars() {
                person_answers.insert(a);
            }

            if first_person {
                answers = person_answers;
                first_person = false;
            }
            else {
                answers = answers.intersection(&person_answers).cloned().collect();
            }
        }
    }

    println!("Total sum of intersecting answers per group: {}", sum_answers_per_group);
}

fn main() {
    println!("Day 06!");
    let contents = fs::read_to_string("input.txt").expect("Could not load file!");
    
    part1(&contents);
    part2(&contents);

    println!("Done!");
}
