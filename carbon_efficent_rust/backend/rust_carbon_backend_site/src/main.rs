use actix_web::{get, web, App, HttpServer, Responder};
use std::{thread, time};

#[get("/{name}")]
async fn index(web::Path((name)): web::Path<(String)>) -> impl Responder {
    thread::sleep(time::Duration::new(2,0));
    for n in 1..101 {
        if n == 50 {
            printn!("50!")
        }
    }
    format!("{}", name)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(index))
        .bind("127.0.0.1:8080")?
        .run()
        .await
}