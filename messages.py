import json
import random


def get_file_content(path):
    with open(path) as f:
        content = json.load(f)
    return content


def get_pretty_message():
    path = 'data/stimul_words.json'
    words_list = get_file_content(path)
    return random.choice(words_list)
