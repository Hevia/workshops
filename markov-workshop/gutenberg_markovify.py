import markovify
import os
from pathlib import Path

ROOT_DIR = Path.cwd()
DATA_DIR = f"{ROOT_DIR}/data/gutenberg/"

# This example is taken from the markovify repo README
combined_model = None
for (dirpath, _, filenames) in os.walk(DATA_DIR):
    for filename in filenames:
        with open(os.path.join(dirpath, filename)) as f:
            model = markovify.Text(f, retain_original=False, well_formed=False)
            if combined_model:
                combined_model = markovify.combine(models=[combined_model, model])
            else:
                combined_model = model

print(combined_model.make_sentence())