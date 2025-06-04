import json
import os
import random


def load_words(path="words.json"):
    base = os.path.dirname(__file__)
    file_path = os.path.join(base, path)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def quiz(words):
    correct = 0
    total = 0
    try:
        while True:
            word = random.choice(words)
            ans = input(f"Translate '{word['english']}': ").strip()
            if ans.lower() == word['translation'].lower():
                print("Correct!\n")
                correct += 1
            else:
                print(f"Wrong, the answer is {word['translation']}.\n")
            total += 1
    except KeyboardInterrupt:
        print(f"\nYou answered {correct} out of {total} correctly. Goodbye!")


def main():
    words = load_words()
    quiz(words)


if __name__ == "__main__":
    main()
