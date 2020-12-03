use std::fs;

#[derive(Debug)]
struct Pos {
    x: usize,
    y: usize
}

impl Pos {
    fn new() -> Pos {
        Pos{ x: 0, y: 0}
    }

    fn step(&mut self, dx: usize, dy: usize) {
        self.x += dx;
        self.y += dy;
    }
}

#[derive(Debug)]
struct World {
    grid: Vec<Vec<char>>
}

impl World {
    fn height(&self) -> usize {
        self.grid.len()
    }

    fn width(&self) -> usize {
        self.grid[0].len()
    }

    fn is_tree(&self, pos: &Pos) -> bool {
        let mod_x = pos.x % self.width();
        self.grid[pos.y][mod_x] == '#'
    }

    fn load(file: &str) -> World {
        let contents = fs::read_to_string(file).expect("Could not load file!");

        let mut grid : Vec<Vec<char>> = Vec::new();
        for line in contents.lines() {
            grid.push(line.chars().collect::<Vec<_>>());
        }

        World{ grid }
    }
}

fn count_trees_for_step(world: &World, dx: usize, dy: usize) -> usize {
    let mut pos = Pos::new();
    let mut num_trees = 0;

    while pos.y < world.height() {
        if world.is_tree(&pos) {
            num_trees += 1;
        }
        pos.step(dx, dy);
    }
    
    println!("Num Trees: {} on the way to final pos {:?}", num_trees, pos);
    num_trees
}

fn main() {
    println!("Day 03!");
    
    let world = World::load("input.txt");
    println!("Found world of size {}x{}", world.width(), world.height());
    
    let encountered_trees =  
        count_trees_for_step(&world, 1, 1)
        * count_trees_for_step(&world, 3, 1)
        * count_trees_for_step(&world, 5, 1)
        * count_trees_for_step(&world, 7, 1)
        * count_trees_for_step(&world, 1, 2);

    println!("In total, found {} trees", encountered_trees);
}
