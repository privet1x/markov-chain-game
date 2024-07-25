# Rock, Paper, Scissors Game with Markov Chain

This module simulates a rock, paper, scissors game using a Markov chain model. The game predicts the opponent's next move based on the history of moves.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Function Descriptions](#function-descriptions)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The game predicts the opponent's next move based on the history of moves and adjusts its strategy using a Markov chain model. It updates the transition probabilities between different states of the game as it learns from each move.

## Requirements

- Python 3.x
- NumPy (`numpy`)

You can install the required package using the following command:
```bash
pip install numpy
```

## Function Descriptions

- `update_transition_matrix(matrix, previous_state, next_state, increment=0.05, decrement=0.01)`: Updates the transition matrix based on observed move transitions.
- `predict_next_move(matrix, current_state)`: Predicts the opponent's next move based on the current state.
- `move_to_state_index(move, outcome)`: Converts a move and its outcome to the corresponding state index.
- `play_game(matrix)`: Plays the rock, paper, scissors game, updating and saving the transition matrix.

## File Descriptions

- `rock_paper_scissors.py`: Main script containing the game logic and functions.
- `transition_matrix.txt`: File to store the transition matrix, which is updated after each game.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
