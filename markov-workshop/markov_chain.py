import json
import random
from typing import List
from data_collection import loadJSON

def exampleSentences():
    return ["I love to eat pancakes", "I like to eat pizza", "I like to eat porridge"]

def createMarkovChain(data_array: List[List[str]]) -> (dict, List[str]):
    """
    This functions creates our Markov Chain if we pass it a 2D Array of sentences
    """
    markov_chain = {}
    beginnings = []

    for sentence in data_array:
        # Let us split our sentence by words
        sentence_split_by_words = sentence.split()
        sentence_len = len(sentence_split_by_words)

        # We're going to loop over each word 
        for i, word in enumerate(sentence_split_by_words):
            if i == 0:
                beginnings.append(word)
            
            # If the word is not it in our dictonary then we add it
            if word not in markov_chain:
                markov_chain[word] = []

            # This a check so we don't go out of bounds
            if i == sentence_len - 1:
                break

            # We add the word that comes after our current word to the chain
            # In the example:
            # markov_chain["I"] = ["like", "like", "love"]
            markov_chain[word].append(sentence_split_by_words[i + 1])

    #print(markov_chain)
    #print(beginnings)

    return markov_chain, beginnings       


def generateText(markov_chain: dict, beginnings: List[str], iterations: int, generation_length: int) -> None:
    for _ in range(iterations):
        seed = random.choice(beginnings)
        result = seed

        for _ in range(generation_length):
            possibilities = markov_chain[seed]

            if possibilities == [] or possibilities == None:
                break
            
            seed = random.choice(possibilities)
            result += " " + seed

        print("========================================")
        print(result)
    
    print("========================================")

# Example - Slide sentences
# data = exampleSentences()
# markov_chain, beginnings = createMarkovChain(data)
# generateText(markov_chain, beginnings, 3, 7)

# Example - Academic Subjects + Business Categories
data_academia = loadJSON("data/academic_subjects.json")['subjects']
data_businesses = loadJSON("data/industries.json")["industries"]
data = data_academia + data_businesses
markov_chain, beginnings = createMarkovChain(data)
generateText(markov_chain, beginnings, 50, 15)

# Example - Dinosaur Wikipedia summaries
# data = loadJSON("data/processed_dinodata.json")
# markov_chain, beginnings = createMarkovChain(data['dinosaurs'])
# generateText(markov_chain, beginnings, 3, 100)

# Example - Oprah Shakespeare
# data = loadJSON("data/oprah_shakespeare.json")
# markov_chain, beginnings = createMarkovChain(data['text'])
# generateText(markov_chain, beginnings, 3, 100)



