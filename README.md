# Chess Puzzle Trainer in Effekt

![Tests](https://github.com/zaryar/EffektChess/workflows/Effekt%20Tests/badge.svg)

A chess puzzle trainer implemented in [Effekt](https://github.com/effekt-lang/effekt), a research programming language that supports algebraic effects and handlers.


## must-have

- Find a puzzle better than 90 and select one randomly.
- Parse FEN Notation
- Display Board as ASCII
- User Input Validation (Accept user moves in algebraic notation)
- Check if the user’s move matches the correct solution.
- if yes: the opponent moves
- if no: get 3 chances

## can-have

- Better way to see the current state of the board / better way to input his move.
- Filter by Rating (difficulty) 
- Progression system: Like you start by only being able to do simple puzzles; if you solve 10, you unlock harder puzzles, and so on.

## Will-not-have

- Online Multiplayer
- AI Opponent
- Advanced Chess Analytics/Feedback

## Effects and handlers

- InvalidMove
- InvalidPuzzle
- PuzzleWon
- PuzzleLost

- IOError
- OutOfBounds


## FFI and libraries

- string - String manipulation
- option - Optional values
- list - List operations
- io - File operations
- exception - Error handling
- Chess puzzles from Lichess

## How to use
1. Install Effekt following the official instructions
2. Clone this repository
```# Install dependencies
# Run game
effekt src/main.effekt

# Run tests
effekt src/test.effek
```

## Features

- **Simple Viewer**:
   - View board from both white and black's perspective
   - Show the last move from the enemie
   - Put in your move with algebraic notation.
- **Progress System**: 
  - Unlock harder puzzles by solving easier ones
  - Lose progress when failing puzzles
- **Settings**: 
  - Remove already played puzzles.
  - Hardcore Mode ( One chance per move ) / Nomal mode, you get a tipp after you make a mistake
- **Effect-based Error Handling**:
  - Invalid puzzle handling
  - Move validation
  - Game state management
