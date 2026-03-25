from datasets import load_dataset
import random

# Load the dataset
dataset = load_dataset("rguo12/ubuntu_dialogue_corpus", "v2.0")
train_data = dataset['train']

# Sample 50 dialogues to pick 20 queries from
samples = random.sample(range(len(train_data)), 50)

with open('sampled_queries.txt', 'w', encoding='utf-8') as f:
    for i in samples:
        # Extract the first message from the dialogue
        dialogue = train_data[i]['utterance']
        f.write(f"{dialogue}\n")
