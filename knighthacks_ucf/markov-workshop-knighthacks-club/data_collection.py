from pathlib import Path
import json
import time
import string
import wikipedia

ROOT_DIR = Path.cwd()
DATA_DIR = f"{ROOT_DIR}/data"

def loadJSON(data_path: str):
    with open(data_path) as json_data:
        data = json.load(json_data)
        return data

def loadCurrentCheckpoint(checkpoint_len: int):
    return loadJSON(f"checkpoints/dinosaurs{checkpoint_len}.json")

def loadDinosaurData():
    return loadJSON("data/animals/dinosaurs.json")

def grabDinosaurSummaries():
    checkpoint_len = 400
    dinosaurs = loadDinosaurData()['dinosaurs'][checkpoint_len:]
    #wiki_wiki = wikipediaapi.Wikipedia('en')
    #dinosaurs = ["Kangnasaurus", "Epachthosaurus", "Zuolong"]
    dinosaur_summaries = loadCurrentCheckpoint(checkpoint_len)
    i = 0
    total = checkpoint_len

    for dinosaur in dinosaurs:
        try:
            dinosaur_summaries[dinosaur] = wikipedia.summary(dinosaur)
        except Exception:
            print(f"Exception on dinosaur: {dinosaur}")
            continue

        i += 1

        if i == 50:
            total += 50
            print(f"Downloaded: {total} dinosaurs so far")
            with open(f"{ROOT_DIR}/checkpoints/dinosaurs{total}.json", 'w+') as json_file:
                json.dump(dinosaur_summaries, json_file, indent=4)
            i = 0
            time.sleep(5)


def preprocessDinosaurSummaries():
    data = loadJSON(f"{ROOT_DIR}/checkpoints/dinosaurs1400.json")
    processed_data = {"dinosaurs": []}

    for dinosaur in data.keys():
        processed_data['dinosaurs'].append(
            data[dinosaur]
            .replace("-", " ")
            .replace("\n", " ")
            .translate(str.maketrans('', '', string.punctuation))
            .encode("ascii", "ignore")
            .decode()
            )

    with open(f"{DATA_DIR}/processed_dinodata.json", 'w+') as json_file:
        json.dump(processed_data, json_file, indent=4)

# What a weird function name
def preprocessOprahShakespeareData():
    oprah = loadJSON(f"{ROOT_DIR}/data/people/oprah_quotes.json")['oprahQuotes']
    shake_phrases = loadJSON(f"{ROOT_DIR}/data/people/shakespeare_phrases.json")['phrases']
    shake_sonnets= loadJSON(f"{ROOT_DIR}/data/people/shakespeare_sonnets.json")['sonnets']

    lines = []
    for sonnet in shake_sonnets:
        lines = lines + sonnet['lines']

    data = {"text": []}
    data['text'] = oprah + lines + shake_phrases
    
    with open(f"{DATA_DIR}/oprah_shakespeare.json", 'w+') as json_file:
        json.dump(data, json_file, indent=4)


#grabDinosaurSummaries()
#preprocessDinosaurSummaries()
preprocessOprahShakespeareData()