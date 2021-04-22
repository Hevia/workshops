 use cogent::{
        Activation, EvaluationData, HaltCondition, Layer, MeasuredCondition, NeuralNetwork,
    };

use ndarray::{Array2,Axis};

fn main() {
let mut network = NeuralNetwork::new(784,&[
    Layer::Dense(128,Activation::ReLU),
    Layer::Dense(10,Activation::Softmax)
]);
let (mut train_data,mut train_labels):(Array2<f32>,Array2<usize>) = get_mnist_dataset(false);
let (test_data,test_labels):(Array2<f32>,Array2<usize>) = get_mnist_dataset(true);
network.train(&mut train_data,&mut train_labels)
    .evaluation_data(EvaluationData::Actual(&test_data,&test_labels)) // Sets evaluation data
    .l2(0.1) // Implements L2 regularisation with a 0.1 lambda vlaue
    .tracking() // Prints backpropgation progress within each iteration
    .log_interval(MeasuredCondition::Iteration(1)) // Prints evaluation after each iteration
    .go();
let (cost,correctly_classified):(f32,u32) = network.evaluate(&test_data,&test_labels,None);
println!("Cost: {:.2}",cost);
println!(
    "Accuracy: {}/{} ({:.2}%)",
    correctly_classified,
    test_data.len_of(Axis(1)),
    correctly_classified as f32 / test_data.len_of(Axis(1)) as f32
);
}
