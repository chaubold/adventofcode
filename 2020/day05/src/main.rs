use std::fs;
use std::cmp;
use std::collections::HashSet;

fn to_seat_id(ticket: &str) -> u16 {
    let chars = ticket.chars().collect::<Vec<_>>();

    if chars.len() != 10 {
        panic!("Invalid Boarding pass {}", ticket);
    }

    let mut seat_id = 0;

    for i in 0..10 {
        if chars[9 - i] == 'B' || chars[9 - i] == 'R' {
            seat_id += 1 << i;
        }
    }

    seat_id
}

#[test]
fn seat_id_tests() {
    assert_eq!(to_seat_id("FBFBBFFRLR"), 357);
    assert_eq!(to_seat_id("BFFFBBFRRR"), 567);
    assert_eq!(to_seat_id("FFFBBBFRRR"), 119);
    assert_eq!(to_seat_id("BBFFBBFRLL"), 820);
}

fn main() {
    println!("Day 02!");
    let contents = fs::read_to_string("input.txt").expect("Could not load file!");
  
    let mut used_seats = HashSet::new();
    let mut max_seat_id = 0;
    for line in contents.lines() {
        let seat_id = to_seat_id(line);
        max_seat_id = cmp::max(seat_id, max_seat_id);
        used_seats.insert(seat_id);
    }
    
    println!("Max SeatID: {}", max_seat_id);

    for i in 1..max_seat_id {
        if !used_seats.contains(&i) && used_seats.contains(&(i - 1)) && used_seats.contains(&(i + 1)) {
            println!("Found my seat: {}", i)
        }
    }

    println!("Done.")
}