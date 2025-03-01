# Project: Sudoku Game

This project is my first independent project with [boot.dev](https://www.boot.dev/tracks/backend). With this project, I am aiming to implement a playable & solvable game of Sudoku from scratch. Specific goals are:

[X] Implement UI that performs backtracking algorithm to solve a puzzle
[X] Create a function that can initialize a unique, solvable sudoku board
[X] Implement game playable from command line
[] Implement game playable from GUI



## Description

TODO: Include diagram detailing index conventions for rows, cols, boxes


## Usage

Run `python3 main.py` in the terminal. Use `-h` or `--help` to see the available options for playing the game. 

A valid sudoku grid will be generated, then some values will be taken away to make a grid with a unique solution. The chosen difficulty will determine the number of cells that are empty (It might take a little longer to generate expert games!)

If you choose to play the game, use the format (<row>,<col>= <val>) to input values. Indices must be between 1-9.


## Testing

Run `python3 -m unittest discover` in the terminal to perform all unit tests. (I've slacked on these a little bit...)