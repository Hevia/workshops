fn main() {

    // declaring some variables
    let hello: i32 = 10;
    let mut goodbye = 11;
    println!("goodbye is now: {}", goodbye);
    // hello = 12;
    
    // goodbye = "its now a string!"
    goodbye = 44;
    println!("goodbye is now: {}", goodbye);

    let v = vec![1, 2, 3, 4, 5];
    //v.push(4);
    println!("v[3]: {}", v[3]);

    let mut v2 = Vec::new();
    
    for n in 1..11 {
        v2.push(n);
    }

    for i in v2.iter() {
        match i {
            1 => println!("One is the loneliest number"),
            2 | 3 | 5 => println!("Two Three Five!"),
            6 | 7 => println!("Fallout: 67"),
            9 => println!("What is 9*9??"),
            10 => println!("Ten"),
            _ => println!("4 & 8 didnt get any matches :(")
        }
    }
}
