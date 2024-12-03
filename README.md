# EffektChess(puzzles)

The base idea is that I first find the best rated puzzles with popularity (Popularity is a number between 100 (best) and -100 (worst).). Then a random puzzle is chosen and build from the FEN notation. After that, the user sees the current check board via ASCII and can put in his move with algebraic notation. The move can be correct or incorrect, after a correct move the user sees the move from the opponent and the system repeats. After a wrong move, he can try again, maybe like 3 times or so.

I did some research and found that Lichess shares their puzzles in a CSV file with the following structure: PuzzleId,**FEN**,**Moves**,_Rating_,_RatingDeviation_,**Popularity**,NbPlays,_Themes_,GameUrl,OpeningTags.

While Bold stands for: **I need it for the base structure**
and Italic stands for: _I could use it for extensions_.

## must-have

- Find a puzzle better than 90 and select one randomly.
- Parse FEN Notation
- Display Board as ASCII
- User Input Validation (Accept user moves in algebraic notation)
- Check if the user’s move matches the correct solution.
- if yes: the opponent moves
- if no: get 3 changses and lose.

## can-have

- Better way to see the current state of the board / better way to input his move.
- Filter by Rating (difficulty) or themes (like opening, fork or mate in 2...)
- Progression system: Like you start by only being able to do simple puzzles, if you solve 10 in a given time you unlock harder puzzles and so on.

## Will-not-have

- Online Multiplayer
- AI Opponent
- Advanced Chess Analytics/Feedback

## Effects and handlers

- Illegal/Wrong move
- Corrupted puzzle data

- Timers?

## FFI and libraries

- string
- option
- list
- io (time, console)?
- chesspuzzles from lichess

## Table of contents

- [First steps](#first-steps)
- [Useful commands](#useful-commands)
  - [Effekt commands](#effekt-commands)
  - [Nix-related commands](#nix-related-commands)
- [Example projects](#example-projects-using-this-template)
- [Repository structure](#repository-structure)
- [CI](#ci)

---

## First steps

After using this template, follow these steps to set up your project:

1. Set up your development environment:
   - Clone this repository locally.
   - Open it in VSCode.
   - Install the Effekt VSCode extension offered in the pop-up in the bottom right.

2. Customize the project:
   - Open `flake.nix` and update the project name and other relevant values (follow the comments).
   - Push your `flake.nix` file after the changes and see if the CI agrees.

3. Set-up auto-update CI:
   - Go to Settings -> Actions -> General and check "Allow GitHub Actions to create and approve pull requests"
     in order to get weekly Pull Requests on Tuesday that update the Effekt version in CI.
   - See the [CI](#ci) section for more details

4. Replace this `README` with your own!
   - Please link back to this repo if you can :)

## Useful commands

### Effekt commands

Run the main file:
```sh
effekt src/main.effekt
```
This (like many other Effekt commands) uses the JavaScript backend by default.
To use a different backend, add the `--backend <backend>` flag.

Run the tests:
```sh
effekt src/test.effekt
```

Open the REPL:
```sh
effekt
```

Build the project:
```sh
effekt --build src/main.effekt
```
This builds the project into the `out/` directory, creating a runnable file `out/main`.

To see all available options and backends, run:
```sh
effekt --help
```

### Nix-related commands

While Nix installation is optional, it provides several benefits:

Update dependencies (also runs automatically in CI):
```sh
nix flake update
```

Open a shell with all necessary dependencies:
```sh
nix develop
```

Run the main entry point:
```sh
nix run
```

Build the project (output in `result/bin/`):
```sh
nix build
```

## Example projects using this template

- [`effekt-stm`](https://github.com/jiribenes/effekt-stm)
- This very project!

## Repository structure

- `.github/workflows/*.yml`: Contains the [CI](#ci) definitions
- `src/`: Contains the source code
  - `main.effekt`: Main entry point
  - `test.effekt`: Entry point for tests
  - `lib.effekt`: Library code imported by `main` and `test`
- `flake.nix`: Package configuration in a Nix flake
- `flake.lock`: Auto-generated lockfile for dependencies
- `LICENSE`: Project license
- `README`: This README file

## CI

Two GitHub Actions are set up:

1. `flake-check`:
   - Checks the `flake.nix` file, builds and tests the project
   - Runs on demand, on `main`, and on PRs
   - To run custom commands, add a step using:
     - `nix run -- <ARGS>` to run the main entry point with the given arguments
     - `nix develop -c '<bash command to run>'` to run commands in the correct environment

2. `update-flake-lock`:
   - Updates package versions in `flake.nix`
   - Runs on demand and weekly (Tuesdays at 00:00 UTC)
