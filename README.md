# Tic-Tac-Toe Game (Tkinter GUI)

This is a simple **Tic-Tac-Toe** game for two players built using **Python** and **Tkinter**. The game features a graphical interface with buttons, automatic turn handling, and game outcome detection (win or tie). The `tkmacosx` package is used for enhanced button styling on macOS.

## Features

- Classic 3x3 Tic-Tac-Toe board
- Turn-based player switching (`X` and `O`)
- Win detection (row, column, and diagonal)
- Tie detection
- Highlighting of winning line or tie state
- Restart button to reset the game

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `tkmacosx` (for button styling on macOS)

### Install dependencies:
```bash
pip install tkmacosx
```

## How to Run

1. Save the code to a file, e.g., `tictactoe.py`
2. Run the game using Python:
```bash
python tictactoe.py
```

## Gameplay Instructions

- The game starts with a randomly chosen player (`X` or `O`)
- Players take turns clicking on empty cells
- The game ends when:
  - One player gets 3 in a row/column/diagonal (win)
  - All cells are filled with no winner (tie)
- Click the **Restart** button to play again

