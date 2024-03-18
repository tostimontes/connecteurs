# French Connectors Learning Tool

## Introduction

This project is a Python-based educational tool designed to assist in learning French connectors and their translations from and into Spanish. It is a simple, interactive command-line program that presents the user with a random French connector (or a Spanish one) and asks for its translation. The tool provides immediate feedback on the accuracy of the user's response and offers examples of the connector used in sentences.
This tool is an excellent way for beginners and intermediate learners to practice and reinforce their knowledge of French connectors.

## How It Works

The program operates by randomly selecting a connector (a word or phrase that links parts of a sentence) from a predefined list and asking the user to translate it from French to Spanish or vice versa. It then evaluates the user's response, highlighting the differences from the correct translation if needed. To aid learning, it also displays example sentences using the selected connector in both French and Spanish.

- Wrong answer

![wrong-answer](/screenshots/wrong-answer.png)

- Almost correct answer

![almost-answer](/screenshots/almost-answer.png)

- Correct answer

![correct-answer](/screenshots/correct-answer.png)

## Setup and Execution

### Prerequisites

- Python: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. [Download the `connecteurs.py` file](https://github.com/tostimontes/connecteurs/raw/master/connecteurs.py) to your local machine.
2. Open your terminal or command prompt.

### Running the Program

In the terminal, navigate to the directory where you have saved `connecteurs.py` and run the following command:

```sh
python connecteurs.py
```

Follow the on-screen instructions to interact with the program.

## Libraries Used

- `random`: For selecting connectors randomly.
- `difflib`: To compare user input with the correct answer and provide a similarity score.
- `colorama`: For adding color to the terminal text, making the learning experience more engaging.

## Additional features

- Add score and score percentage

---
