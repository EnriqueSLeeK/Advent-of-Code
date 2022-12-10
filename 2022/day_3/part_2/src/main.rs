use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result::<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn  get_badge(first_sack: &str, second_sack: &str, third_sack: &str) -> char {

    let mut target = '\0';

    for c in first_sack.chars() {
        for k in second_sack.chars() {
            for p in third_sack.chars() {
                if c == k && c == p { target = c; }
            }
        }
        if target != '\0' { break; }
    }
    target
}

fn get_priority(first_sack: &str, second_sack: &str, third_sack: &str) -> i32 {

    let item: char = get_badge(first_sack, second_sack, third_sack);

    if item.is_ascii_uppercase() { return (item as i32 - 'A' as i32) + 27 }
    (item as i32 - 'a' as i32) + 1
}

fn main() {
    if let Ok(lines) = read_lines("../input.txt") {

        let mut index = 0;
        let mut sack: [String; 3] = ["".to_string(), "".to_string(), "".to_string()];
        let mut priority_sum = 0;
        for line in lines {
            if let Ok(line) = line {
                sack[index] = line;
                index += 1;
            }
            else {
                println!("Ugh bad line!");
                break;
            }
            if index == 3 {
                priority_sum += get_priority(&sack[0], &sack[1], &sack[2]);
                index = 0;
            }
        }
        println!("{}", priority_sum);
    }
    else {
        println!("Failure at opening a file");
    }
}
