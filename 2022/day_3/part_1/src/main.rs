use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result::<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn  get_repeated_item(first_half: &str, second_half: &str) -> char {

    let mut target = '\0';

    for c in first_half.chars() {
        for k in second_half.chars() {
            if c == k { target = c; }
        }
        if target != '\0' { break; }
    }
    target
}

fn get_priority(first_half: &str, second_half: &str) -> i32 {

    let item: char = get_repeated_item(first_half, second_half);

    if item.is_ascii_uppercase() { return (item as i32 - 'A' as i32) + 27 }
    (item as i32 - 'a' as i32) + 1

}

fn main() {
    if let Ok(lines) = read_lines("../input.txt") {

        let mut len;
        let mut priority_sum = 0;
        for line in lines {
            if let Ok(sack) = line {
                len = sack.len();
                priority_sum += get_priority(&sack[0..len/2], &sack[len/2..len]);
            }
        }
        println!("{}", priority_sum);
    }
    else {
        println!("Failure at opening a file");
    }
}
