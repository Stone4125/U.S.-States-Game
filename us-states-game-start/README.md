# U.S. States Game

A small Python game built with `turtle` and `pandas` to learn the 50 U.S. states.

The player must guess the names of the U.S. states by typing them into an interactive window. If the answer is correct, the state name is displayed at its location on the map of the United States.

The game ends when the user types `Exit`, which automatically creates a `miss_states.csv` file containing the states that were not found.

## Features

- Graphical interface with `turtle`
- Loading data from a CSV file
- Detection of already guessed states
- Display of each state's position on the map
- Score tracking
- Export of missed states to a CSV file

## Prerequisites

- Python 3.x
- `pandas`
- standard `turtle` library (included with Python)

## Installation

1. Open a terminal in the project folder.
2. Install the dependencies:

```bash
pip install pandas
```

## Running the game

From the project folder, run:

```bash
python main.py
```

## How to play

- Enter the name of a U.S. state.
- If the state is correct, its name appears on the map.
- The score increases with each correct answer.
- Type `Exit` to quit the game and save the missed states to `miss_states.csv`.

## Project structure

```text
us-states-game-start/
├── 50_states.csv
├── blank_states_img.gif
├── main.py
├── miss_states.csv
└── README.md
```

## Important files

- `main.py` : main game logic
- `50_states.csv` : list of U.S. states and their coordinates
- `blank_states_img.gif` : background map used by the game
- `miss_states.csv` : file generated automatically when exiting the game

## Note

This project is a simple visual learning exercise for working with CSV data, graphical display with Turtle, and game logic.
