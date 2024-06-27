# Treasure Hunt Game

This is a simple console-based treasure hunt game implemented in Python. The player has to guess the location of the treasure on a 10x10 grid within 7 attempts. After each guess, the game provides a hint indicating how many steps away the guess was from the actual treasure location.

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/username/repository.git`.
2. Navigate to the project directory using `cd repository`.
3. Run the game using `python main.py`.

## Gameplay

The treasure is hidden in a 10x10 grid. The player has to guess the coordinates of the treasure. The 'x' coordinate is a number from 1 to 10 and the 'y' coordinate is a letter from A to J. For example, '1, A' would be the top-left corner of the grid. The player has 7 attempts to find the treasure. After each guess, the game provides a hint indicating how many steps away the guess was from the treasure.

## Code Overview

The game is implemented using three main classes:

- `Player`: This class represents the player. It keeps track of the player's attempts and the coordinates of their guesses.
- `TreasureMap`: This class represents the treasure map. It generates a random location for the treasure and provides methods to check if a guess is correct and to get a hint after each guess.
- `Game`: This class represents the game. It handles the game loop, user input, and game logic.

## Running Tests

This project includes a suite of tests to verify that the game works as expected. These tests are located in the `test_main.py` file.

To run the tests, you will need to have Python and the `unittest` module installed on your machine. `unittest` is included in the standard library for Python 3, so you should not need to install it separately.

Here are the steps to run the tests:

1. Open a terminal and navigate to the root directory of your project (the directory that contains all your project files).

2. Run the following command to execute the tests:
```bash
python -m unittest test_main.py
