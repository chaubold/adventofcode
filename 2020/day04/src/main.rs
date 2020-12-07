use std::fs;
use std::collections::HashMap;

extern crate regex;
use regex::Regex;

#[derive(Debug)]
struct Passport {
    entries: HashMap<String, String>
}

impl Passport {
    fn new(fields: &Vec<&str>) -> Passport {
        let mut entries = HashMap::new();

        for f in fields {
            let field_parts = f.split(":").collect::<Vec<_>>();
            if field_parts.len() != 2 {
                panic!("Invalid num elements in field: {}", f);
            }
            entries.insert(String::from(field_parts[0]), String::from(field_parts[1]));
        }

        Passport{entries}
    }

    fn is_complete(&self) -> bool {
        // self.entries.contains_key(cid) &&
        self.entries.contains_key("byr") &&
        self.entries.contains_key("iyr") &&
        self.entries.contains_key("eyr") &&
        self.entries.contains_key("hgt") &&
        self.entries.contains_key("hcl") &&
        self.entries.contains_key("ecl") &&
        self.entries.contains_key("pid")
    }

    fn is_valid(&self) -> bool {
        if !self.is_complete() {
            return false;
        }

        match self.entries.get("byr") {
            None => return false,
            Some(val) => {
                if val.len() != 4 {
                    return false;
                }

                let num : usize = val.parse().expect("Could not convert to number!");
                if num < 1920 || num > 2002 {
                    return false;
                }
            }
        }

        match self.entries.get("iyr") {
            None => return false,
            Some(val) => {
                if val.len() != 4 {
                    return false;
                }

                let num : usize = val.parse().expect("Could not convert to number!");
                if num < 2010 || num > 2020 {
                    return false;
                }
            }
        }

        match self.entries.get("eyr") {
            None => return false,
            Some(val) => {
                if val.len() != 4 {
                    return false;
                }

                let num : usize = val.parse().expect("Could not convert to number!");
                if num < 2020 || num > 2030 {
                    return false;
                }
            }
        }

        let valid_eye_colors = [
            String::from("amb"), 
            String::from("blu"), 
            String::from("brn"), 
            String::from("gry"), 
            String::from("grn"), 
            String::from("hzl"), 
            String::from("oth")
        ];
        match self.entries.get("ecl") {
            None => return false,
            Some(val) => {
                if !valid_eye_colors.contains(val) {
                    return false;
                }
            }
        }

        match self.entries.get("pid") {
            None => return false,
            Some(val) => {
                if val.len() != 9 {
                    return false;
                }

                match val.parse::<usize>() {
                    Ok(_) => {},
                    Err(_) => return false
                }
            }
        }

        let color_regex = Regex::new(r"^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$").unwrap();
        match self.entries.get("hcl") {
            None => return false,
            Some(val) => {
                if !color_regex.is_match(val) {
                    return false;
                }
            }
        }

        let height_regex = Regex::new(r"^(\d{3}cm|\d{2}in)$").unwrap();
        match self.entries.get("hgt") {
            None => return false,
            Some(val) => {
                if !height_regex.is_match(val) {
                    return false;
                }

                let chars = val.chars().collect::<Vec<_>>();

                if chars[3] == 'c'  {
                    let height : usize = val[0..3].parse().unwrap();
                    if height < 150 || height > 193 {
                        return false;
                    }
                }
                else if chars[3] == 'n'  {
                    let height : usize = val[0..2].parse().unwrap();
                    if height < 59 || height > 76 {
                        return false;
                    }
                }
            }
        }

        true
    }

    fn load(file: &str) -> Vec<Passport> {
        let contents = fs::read_to_string(file).expect("Could not load file!");

        let mut passports = Vec::new();
        let mut fields = Vec::new();
        for line in contents.lines() {
            if line.is_empty() {
                passports.push(Passport::new(&fields));
                fields.clear();
                continue
            }

            let fields_in_line = line.split(" ").collect::<Vec<_>>();
            fields.extend(fields_in_line.iter());
        }

        // if the last line was not empty, create a Passport from the last set of fields
        match contents.lines().last() {
            None => {}
            Some(last_line) => {
                if !last_line.is_empty() {
                    passports.push(Passport::new(&fields));
                }
            }
        }

        passports
    }
}

fn main() {
    println!("Day 04!");
    
    let passports = Passport::load("input.txt");
    println!("Found {} passports", passports.len());
    
    let mut num_complete_passports = 0;
    let mut num_valid_passports = 0;
    for p in passports {
        if p.is_complete() {
            // println!("+valid {:?}", p);
            num_complete_passports += 1;

            if p.is_valid() {
                num_valid_passports += 1;
            }
        }
        else {
            // println!("-INVALID {:?}", p);
        }
    }

    println!("Found {} passports with all required fields", num_complete_passports);
    println!("Found {} valid passports", num_valid_passports);
}

#[test]
fn test_data() {
    let passports = Passport::load("test.txt");
    assert_eq!(passports.len(), 4);
    
    assert!(passports[0].is_complete());
    assert!(!passports[1].is_complete());
    assert!(passports[2].is_complete());
    assert!(!passports[3].is_complete());
}

#[test]
fn test_data_2() {
    let passports = Passport::load("test_2.txt");
    assert_eq!(passports.len(), 8);
    
    assert!(!passports[0].is_valid());
    assert!(!passports[1].is_valid());
    assert!(!passports[2].is_valid());
    assert!(!passports[3].is_valid());
    assert!(passports[4].is_valid());
    assert!(passports[5].is_valid());
    assert!(passports[6].is_valid());
    assert!(passports[7].is_valid());
}

#[test]
fn test_regex() {
    let color_regex = Regex::new(r"^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$").unwrap();
    assert!(color_regex.is_match("#ff99a2"));
    assert!(!color_regex.is_match("#fx90a2"));

    let height_regex = Regex::new(r"^(\d{3}cm|\d{2}in)$").unwrap();
    assert!(height_regex.is_match("170cm"));
    assert!(height_regex.is_match("59in"));
    assert!(!height_regex.is_match("170in"));
    assert!(!height_regex.is_match("59cm"));
}