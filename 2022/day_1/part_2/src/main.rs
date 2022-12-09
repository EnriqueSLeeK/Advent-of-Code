use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result::<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() {
    if let Ok(lines) = read_lines("../input.txt") {
        let mut number: i32 = 0;
        let mut list_total_calories = Vec::new();
        for line in lines {
            if let Ok(num) = line {
                if num.is_empty() { 
                    list_total_calories.push(number);
                    number = 0;
                    continue;
                }
                number += num.parse::<i32>().unwrap();
            }
        }
        list_total_calories.sort();
        println!("{}", list_total_calories.iter().rev().take(3).sum::<i32>());
    }
    else {
        println!("Error opening file");
    }
}
