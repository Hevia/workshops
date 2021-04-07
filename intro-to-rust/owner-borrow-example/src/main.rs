fn main() {
    // Ownnership
    // Each Value in Rust has a variable that’s called its owner
    let x = 8; // Integers are a fixed size, so theyre allocated on a stack

    // There can only be one owner at a time
    let mut y = 4;
    let z = y; // z "copies" the value of y
    y = 5;
    println!("y is: {}", y);
    println!("z is: {}", z);

    // When the owner goes out of scope, the value will be dropped
    {
        let a = 5;
    }
    //println!("a is {}", a); // This will error out

    // Ownership with heap
    let v1 = String::from("hello");
    let v2 = v1;
    // do something with v1

    // ---------------------------------------------------------------------------------------------

    // Borrowing
    let mut s = String::from("hello"); // This is allocated on the heap bc Strings can grow/shrink in size

    // Why is this different from "ownership" above?
    // Read only borrow references
    let r1 = &s; // read only referece, can have unlimited of these!
    let r2 = &s; // no problem

    //let r3 = &mut s; // UH OH, can only have ONE read/write ref OR any number of read references, how do we fix this?
    //println!("{}, {}, and {}", r1, r2, r3);
    
    // Only ONE mutable borrow reference at a time
    {
        let r1 = &mut s;
    } // r1 is dropped out of scope so we can make a mutable borrow again

    //let r2 = &mut s;
}
