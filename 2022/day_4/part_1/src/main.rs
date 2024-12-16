use std::fs::File;
use std::path::Path;
use std::io::{self, BufRead};

fn read_lines<P>(filename: P) -> io::Result::<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn overlap(min: &str, max: &str, min_p: &str, max_p: &str) -> i32 {

    let a = min.parse::<i32>().unwrap();
    let b = max.parse::<i32>().unwrap();

    let a_p = min_p.parse::<i32>().unwrap();
    let b_p = max_p.parse::<i32>().unwrap();

    if a <= a_p && b >= b_p { return 1 }
    if a >= a_p && b <= b_p { return 1 }
    0
}


fn main() {
    if let Ok(lines) = read_lines("../input.txt") {

        let mut sections_ranges;
        let mut fully_covered: i32 = 0;
        for line in lines {
            if let Ok(line) = line {
                sections_ranges = line.split([',', '-'].as_ref());
                fully_covered += overlap(sections_ranges.next().unwrap(),
                    sections_ranges.next().unwrap(),
                    sections_ranges.next().unwrap(),
                    sections_ranges.next().unwrap());

            }
        }
        println!("{}", fully_covered);
    }
    else {
        println!("Failure at opening a file");
    }
}
