"""
This module simulates a rock, paper, scissors game using a Markov chain model.
The game predicts the opponent's next move based on the history of moves.
"""

import os
import random
import numpy as np

states = ['VA', 'VT', 'VC', 'LA', 'LT', 'LC']
initial_probabilities = np.ones((6, 6)) / 6  # Equal probabilities for all transitions initially

# Load the transition matrix from a file if it exists
MATRIX_PATH = 'transition_matrix.txt'
if os.path.exists(MATRIX_PATH):
    my_matrix = np.loadtxt(MATRIX_PATH)
else:
    my_matrix = initial_probabilities.copy()


def update_transition_matrix(matrix, previous_state, next_state, increment=0.05, decrement=0.01):
    """
    Update the transition matrix based on observed move transitions.

    Parameters:
    matrix: The current transition matrix.
    previous_state: The index of the previous state.
    next_state: The index of the next state.
    increment: The amount to increase for the actual transition.
    decrement: The amount to decrease for all other transitions.

    Returns:
    The updated transition matrix.
    """
    for i in range(len(states)):
        if i == next_state:
            matrix[previous_state, i] += increment
        else:
            matrix[previous_state, i] -= decrement
            matrix[previous_state, i] = max(matrix[previous_state, i], 0)

    sum_prob = np.sum(matrix[previous_state, :])
    matrix[previous_state, :] = matrix[previous_state, :] / sum_prob
    return matrix


def predict_next_move(matrix, current_state):
    """
    Predict the opponent's next move based on the current state.

    Parameters:
    matrix: The current transition matrix.
    current_state: The index of the current state.

    Returns:
    The index of the predicted next move.
    """
    adjusted_probs = [sum(matrix[current_state][i:i + 2]) for i in range(0, len(states), 2)]
    predicted_move = adjusted_probs.index(max(adjusted_probs))
    return predicted_move


def move_to_state_index(move, outcome):
    """
    Convert a move and its outcome to the corresponding state index.

    Parameters:
    move: The player's move ('R', 'P', 'S').
    outcome: The outcome of the move ('W', 'L').

    Returns:
    The index of the corresponding state.
    """
    if move == 'R':
        return states.index('VT' if outcome == 'W' else 'LT')
    elif move == 'P':
        return states.index('VA' if outcome == 'W' else 'LA')
    else:  # 'S'
        return states.index('VC' if outcome == 'W' else 'LC')


def play_game(matrix):
    """
    Play the rock, paper, scissors game, updating and saving the transition matrix.

    Parameters:
    matrix: The initial transition matrix.

    Returns:
    None
    """
    player_score = 0
    ai_score = 0
    turns = 0
    current_state = random.randint(0, 5)

    while turns < 30 and player_score < 10 and ai_score < 10:
        user_move = input("Enter your move (R for Rock, P for Paper, S for Scissors): ").upper()
        if user_move not in ['R', 'P', 'S']:
            print("Invalid move. Please enter R, P, or S.")
            continue

        predicted_move = predict_next_move(matrix, current_state)
        ai_move_map = ['P', 'R', 'S']
        ai_move = ai_move_map[predicted_move]

        print(f"AI plays {ai_move}")

        if (user_move == 'R' and ai_move == 'S') or \
           (user_move == 'P' and ai_move == 'R') or \
           (user_move == 'S' and ai_move == 'P'):
            print("You win!")
            player_score += 1
        elif user_move == ai_move:
            print("It's a tie!")
        else:
            print("AI wins!")
            ai_score += 1

        if user_move != ai_move:
            next_state = move_to_state_index(ai_move, 'W' if user_move == ai_move else 'L')
            matrix = update_transition_matrix(matrix, current_state, next_state)
            current_state = next_state

        turns += 1

        if player_score >= 10 or ai_score >= 10:
            print(f"Game over. {'You win!' if player_score > ai_score else 'AI wins!'}")
            np.savetxt(MATRIX_PATH, matrix, fmt='%f')
            break

    if turns == 30:
        print(f"Maximum is 30 turns. Final score Player: {player_score}, AI: {ai_score}")

    np.savetxt(MATRIX_PATH, matrix, fmt='%f')


if __name__ == "__main__":
    play_game(my_matrix)
