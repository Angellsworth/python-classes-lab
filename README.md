# Tic-Tac-Toe (Terminal Version)

A simple terminal-based game of Tic-Tac-Toe built using Python and Object-Oriented Programming (OOP). This app is playable in the terminal by two users taking turns to input their moves.

## 🔧 Technologies Used
- Python 3
- OOP principles
- Terminal I/O

---

## 🚀 How to Run the Game

1. Clone the repo or copy the code into a file named `exercises.py`
2. In your terminal, run:
   ```bash
   python3 exercises.py
   ```
3. Play by typing coordinates like `A1`, `b2`, or `C3` when prompted.

---

## 🎮 Game Features

- Alternates between Player X and Player O
- Board is updated and reprinted after each valid move
- Prevents invalid or already-taken moves
- Detects a win or tie and prints the appropriate message

---

## 🧠 Code Walkthrough

### Class Setup
```python
class Game:
```
Creates a blueprint for managing the game state and behavior.

### Initialization
```python
def __init__(self):
```
Sets up:
- `self.turn`: Tracks whose turn it is ("X" or "O")
- `self.board`: A dictionary of board positions (like "a1", "b2")
- `self.winner`: Tracks the winner (or None)
- `self.tie`: Tracks whether a tie has occurred

### Display Methods
```python
def print_board(self):
```
Displays the current game board in a readable format.

```python
def print_message(self):
```
Tells the user whose turn it is, if someone has won, or if the game ended in a tie.

### Game Loop
```python
def play_game(self):
```
Contains the main gameplay loop. Runs until someone wins or the board is full (tie).

### Player Interaction
```python
def get_move(self):
```
Prompts the player for a move. Validates the input before updating the board.

### Game Logic
```python
def check_for_winner(self):
```
Checks all possible win combinations to see if the current player has won.

```python
def check_for_tie(self):
```
Checks if the board is full and there's no winner.

```python
def switch_turn(self):
```
Alternates the value of `self.turn` between "X" and "O".

---

## ✅ Example Gameplay
```
Welcome to Tic-Tac-Toe!

    A   B   C
1)    |   |  
-----------
2)    |   |  
-----------
3)    |   |  

It is player X's turn!
Enter a valid move (example: A1): a1

    A   B   C
1)  X |   |  
-----------
2)    |   |  
-----------
3)    |   |  

It is player O's turn!
```

---

## ✨ Ideas to Extend
- Add player names
- Track win/loss record
- Play again option after game ends
- Add color/styling with ANSI escape codes

---

Made with ❤️ and Python.

