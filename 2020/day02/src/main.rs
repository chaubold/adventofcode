use std::fs;
use std::str::FromStr;

#[derive(Debug, Clone)]
struct RuleParsingError;

#[derive(Debug)]
struct Rule {
    character: char,
    min_count: usize,
    max_count: usize
}

impl FromStr for Rule {
    type Err = RuleParsingError;

    fn from_str(rule_str: &str) -> Result<Self, Self::Err> {
        let parts = rule_str.split_whitespace().collect::<Vec<_>>();
        let counts = parts[0].split("-").collect::<Vec<_>>();
        let character: char = parts[1].parse().map_err(|_| RuleParsingError)?; // map parsing error to our error type
        let min_count: usize = counts[0].parse().map_err(|_| RuleParsingError)?; // question mark returns the failure if not Ok
        let max_count: usize = counts[1].parse().map_err(|_| RuleParsingError)?;
        Ok(Rule{ character, min_count, max_count })
    }
}

impl Rule {
    fn is_password_valid(&self, pw: &str) -> bool {
        // first char is a space!
        let mut count = 0;
        for c in pw.chars() {
            if self.character == c {
                count += 1;
            }
        }

        if (self.min_count <= count) && (self.max_count >= count) {
            return true;
        }
        else {
            return false;
        }
    }

    fn is_password_valid_part2(&self, pw: &str) -> bool {
        // first char is a space!
        let chars = pw.chars().collect::<Vec<_>>();
        // println!("Applying rule {:?} to '{}'", self, pw);
        // println!("\tChars are {} and {}", chars[self.min_count], chars[self.max_count]);
        if chars[self.min_count] == self.character && chars[self.max_count] != self.character {
            return true;
        }
        else if chars[self.min_count] != self.character && chars[self.max_count] == self.character {
            return true;
        }
        else {
            return false;
        }
    }
}

fn main() {
    println!("Day 02!");
    let contents = fs::read_to_string("input.txt").expect("Could not load file!");
    let mut num_valid_passwords = 0;
    let mut num_valid_passwords_part2 = 0;
    for line in contents.lines() {
        let parts = line.split(":").collect::<Vec<_>>();

        match Rule::from_str(parts[0]) {
            Ok(rule) => {
                let pw = parts[1];

                if rule.is_password_valid(pw) {
                    num_valid_passwords += 1;
                }

                if rule.is_password_valid_part2(pw) {
                    num_valid_passwords_part2 += 1;
                }
            }
            Err(_) => println!("Did not understand line: {}", line)
        }
    }
    
    println!("Num Valid Passwords: {}", num_valid_passwords);
    println!("Num Valid Passwords Part 2: {}", num_valid_passwords_part2);
    println!("Done.")
}

// Tests

#[test]
fn rule1() {
    let line = "1-3 a: abcde";

    let parts = line.split(":").collect::<Vec<_>>();
    assert_eq!(parts.len(), 2);

    match Rule::from_str(parts[0]) {
        Ok(rule) => {
            let pw = parts[1];

            assert!(rule.is_password_valid(pw));
            assert!(rule.is_password_valid_part2(pw));
        }
        Err(_) => panic!("Did not understand line: {}", line)
    }
}

#[test]
fn rule2() {
    let line = "1-3 b: cdefg";
    
    let parts = line.split(":").collect::<Vec<_>>();
    assert_eq!(parts.len(), 2);

    match Rule::from_str(parts[0]) {
        Ok(rule) => {
            let pw = parts[1];

            assert!(!rule.is_password_valid(pw));
            assert!(!rule.is_password_valid_part2(pw));
        }
        Err(_) => panic!("Did not understand line: {}", line)
    }
}

#[test]
fn rule3() {
    let line = "2-9 c: ccccccccc";
    
    let parts = line.split(":").collect::<Vec<_>>();
    assert_eq!(parts.len(), 2);

    match Rule::from_str(parts[0]) {
        Ok(rule) => {
            let pw = parts[1];

            assert!(rule.is_password_valid(pw));
            assert!(!rule.is_password_valid_part2(pw));
        }
        Err(_) => panic!("Did not understand line: {}", line)
    }
}
