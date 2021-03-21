# A* Algorithm - 15-Puzzle

## Introduction
First project of the class Algorithmic Modeling and Optimization.
Consist in a basic implementation of the search algorithm A* (A star) to solve the 15-puzzle game,
using different heuristics, as such: number of pieces out of place, number of pieces out of order,
Manhattan distance, linear combination between heuristics and maximum value between heuristics.
All functions were implemented in Python. Also an article was written (in portuguese)
comparing the efficiency of the heuristics.

## How to execute

The program read an input in the format:

     1 5 9 2 6 10 13 3 7 11 14 4 8 12 0 15

This input correspond to (board-game):
 
| | | | |
| ----- | ----- | -------- | ------- |
| 1 | 5 | 9 | 2 |
| 6 | 10 | 13 | 3 |
| 7 | 11 | 14 | 4 |
| 8 | 12 | <b> 0  | 15 |

0 representing the blank space
