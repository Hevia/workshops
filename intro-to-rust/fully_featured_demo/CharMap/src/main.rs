use std::{
    collections::HashMap,
    fs::{self, File},
    io::prelude::*,
    path::{Path, PathBuf},
};

use anyhow::Result;
use structopt::StructOpt;



#[derive(StructOpt)]

struct CLI {
    /// List of input files
    #[structopt(parse(from_os_str), required = true)]
    input: Vec<PathBuf>,

    /// Output to file instead of terminal
    #[structopt(short = "o", long = "output")]
    file_output: Option<PathBuf>,
}

/// Contains maps of characters to their counts for
/// individual files

#[derive(Debug)]
struct CharMap<T: AsRef<Path>> {
    /// Path to the file we want mapped
    file_path: T,

    /// Map of characters to their counts
    counter: HashMap<char, u32>,
}


impl<T: AsRef<Path>> CharMap<T> {
    /// Allocates a new Char Map with an empty counter
    fn new(file: T) -> Result<Self> {
        fs::metadata(&file)?;

        let map: HashMap<char, u32> = HashMap::new();

        let char_map = Self {
            file_path: file,
            counter: map,
        };

        Ok(char_map)
    }

    /// Counts all of the characters stored in file_path
    fn count_chars(&mut self) -> Result<()> {
        let contents = fs::read_to_string(&self.file_path)?;


        for char in contents.chars() {

            *self.counter.entry(char).or_insert(0) += 1
        }

        Ok(())
    }
}

fn main() -> Result<()> {
    let cli = CLI::from_args();

    let mut maps: Vec<CharMap<PathBuf>> = Vec::new();
    for file in cli.input {
        let mut current_map = CharMap::new(file)?;
        current_map.count_chars()?;
        maps.push(current_map);
    }

    match cli.file_output {
        Some(path) => {
            let mut file = File::create(path)?;
            for map in maps {
                writeln!(file, "{:?}", map)?;
            }
        }

        None => {
            for map in maps {
                println!("{:?}", map);
            }
        }
    }

    Ok(())
}


#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn counter_works() -> Result<()> {
        let filename = "unit_test.txt";
        let mut test_file = File::create(filename)?;
        test_file.write_all(b"abc")?;

        let mut map: HashMap<char, u32> = HashMap::new();
        map.insert('a', 1);
        map.insert('b', 1);
        map.insert('c', 1);

        let mut char_map = CharMap::new(filename)?;
        char_map.count_chars()?;

        assert_eq!(char_map.counter, map);
        assert_eq!(filename, char_map.file_path);

        fs::remove_file(filename)?;

        Ok(())
    }
}
