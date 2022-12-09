use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result::<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn move_point(play_move: &str) -> i32 {
    match play_move {
        "A" => 1,
        "B" => 2,
        "C" => 3,
        &_ => 0,
    }
}

fn get_move(elf_move: &str, outcome: bool) -> &str {
    if outcome {
        return match elf_move {
            "A" => "B",
            "B" => "C",
            "C" => "A",
            &_ => "",
        }
    }
    match elf_move {
        "A" => "C",
        "B" => "A",
        "C" => "B",
        &_ => "",
    }
}

fn get_point(elf_move: &str, outcome: &str) -> i32 {
    if outcome == "Y" { return 3 + move_point(elf_move) }
    if outcome == "Z" { return 6 + move_point(get_move(elf_move, true)) }
    move_point(get_move(elf_move, false))
}

fn main() {
    if let Ok(lines) = read_lines("../input.txt") {

        let mut moves;
        let mut player;
        let mut elf;
        let mut sum = 0;
        for line in lines {
            if let Ok(round) = line {
                moves = round.split_whitespace();
                elf = moves.next().unwrap();
                player = moves.next().unwrap();
                sum += get_point(elf, player);
            }
        }
        println!("{}", sum);
    }
    else {
        println!("Failure at opening a file");
    }
}
