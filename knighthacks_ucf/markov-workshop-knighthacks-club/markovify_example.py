import markovify
from data_collection import loadJSON

# Get raw text as string.
dinosaurs = loadJSON("data/processed_dinodata.json")['dinosaurs']

# Build the model.
text_model = markovify.Text(dinosaurs)

# Print five randomly-generated sentences
for i in range(1):
    print(text_model.make_sentence())