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
        "X" => 1,
        "Y" => 2,
        "Z" => 3,
        &_ => 0,
    }
}

fn get_point(elf_move: &str, player_move: &str) -> i32 {
    if elf_move == "A" && player_move == "X" { return 3 + move_point(player_move) }
    if elf_move == "B" && player_move == "Y" { return 3 + move_point(player_move) }
    if elf_move == "C" && player_move == "Z" { return 3 + move_point(player_move) }
    if elf_move == "A" && player_move == "Y" { return 6 + move_point(player_move) }
    if elf_move == "B" && player_move == "Z" { return 6 + move_point(player_move) }
    if elf_move == "C" && player_move == "X" { return 6 + move_point(player_move) }
    move_point(player_move)
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
