use std::collections::HashMap;
use std::io;


#[derive(Debug)]
/// This is a char map
struct CharMap {
    filename: String,
    character_map: HashMap<char, u32>,
}

impl CharMap {
    fn new(filename: &String) -> io::Result<Self> {
        std::fs::metadata(&filename)?; 

        let char_map = CharMap {
            filename: filename.clone(),
            character_map: HashMap::new()
        };

        Ok(char_map)
    }

    fn count_chars(&mut self) -> io::Result<()> {
        let file_contents: String = std::fs::read_to_string(&self.filename)?;

        for cur_char in file_contents.chars() {
           *self.character_map.entry(cur_char).or_insert(0) += 1;
        }

       Ok(())
    }
}

fn main() -> io::Result<()> {
    let my_args: Vec<String> = std::env::args().collect();

    let mut maps: Vec<CharMap> = Vec::new();
    for filename in my_args.iter().skip(1) {
        let mut cur_map = CharMap::new(filename)?;
        cur_map.count_chars()?;
        maps.push(cur_map);
    }

    println!("{:?}", maps);

    Ok(())
}
