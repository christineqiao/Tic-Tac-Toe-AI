# Tic-Tac-Toe AI

A Python-based Tic-Tac-Toe game featuring an AI opponent powered by the **minimax algorithm**. This project explores how artificial intelligence can evaluate possible moves, anticipate an opponent's decisions, and make optimal choices through recursive game-tree search.

## Features

- **Human vs. AI:** Challenge an AI opponent that uses minimax to make optimal moves.
- **AI vs. AI:** Watch two AI players compete against each other.
- **Human vs. Human:** Play against a friend through the terminal.
- **Minimax Algorithm:** Recursively evaluates possible future moves to determine the best outcome.
- **Game-State Evaluation:** Detects wins, losses, and ties.
- **Custom Starting Positions:** Start a game from an existing valid board configuration.
- **Input Validation:** Prevents invalid moves and board configurations.

## How It Works

The game represents the board as a nine-character string:

- `X` represents Player X.
- `O` represents Player O.
- `.` represents an empty space.

The AI uses the **minimax algorithm** to explore possible moves and evaluate their outcomes. Player X maximizes the score, while Player O minimizes it. Terminal game states are assigned scores based on whether X wins, O wins, or the game ends in a tie.

By evaluating future moves recursively, the AI selects an optimal move. When both players use minimax, the game ends in a tie from an empty board.

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open your terminal in the project directory.
4. Run:

```bash
python3 ttt_shell.py
```

You will be prompted to choose whether each player is human or AI:

```text
X is human or AI? (h: human, a: AI)
O is human or AI? (h: human, a: AI)
Input state (ENTER for empty board):
```

Press Enter at the third prompt to start with an empty board.

## Board Layout

Each position is represented by an index from 0 to 8:

```text
0 1 2
3 4 5
6 7 8
```

Enter the index of an available position to make your move.

## Technologies and Concepts

- Python 3
- Minimax Algorithm
- Recursive Game-Tree Search
- Adversarial Search
- Game-State Evaluation
- Terminal-Based User Interaction

## Future Improvements

- Implement alpha-beta pruning to optimize search efficiency.
- Add adjustable AI difficulty levels.
- Create a graphical user interface.
- Add a scoreboard to track multiple rounds.

## Background

Originally developed as part of a high school artificial intelligence programming course to explore adversarial search algorithms, recursion, and decision-making in two-player games.
