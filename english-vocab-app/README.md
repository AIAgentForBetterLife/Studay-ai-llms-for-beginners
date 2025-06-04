# English Vocabulary Memorization App

This simple project provides a command-line tool to help you practice English vocabulary. It loads a small list of words and their definitions, quizzes you randomly and tracks your progress in the session.

## Features

- Random flash cards
- Tracks how many answers you get correct
- Easy to extend with your own vocabulary list

## Usage

```bash
python app.py
```

During each run, the app will show a word in English and ask you for its translation in your native language. Type the correct answer and press Enter to see if you are right. The program will continue until you decide to quit with `Ctrl+C`.

## Customizing Words

Edit `words.json` to add or modify vocabulary. Each entry should contain an `english` word and its `translation` field.
