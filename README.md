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
| 8 | 12 | <b>0 | 15 |

0 representing the blank space


## Configuration of the goal board

The goal board is set as:

| | | | |
| ----- | ----- | -------- | ------- |
| 1 | 5 | 9 | 13 |
| 2 | 6 | 10 | 14 |
| 3 | 7 | 11 | 15 |
| 4 | 8 | 12 | <b>0 |
     
#Heuristics implemented

- Out of place: number of pieces of out place compared to final configuration.
- Out of order: number of pieces out of order in the numerical sequence, following the order of positions on the board
- Manhattan distance: standart Manhattan Distance.
- Linear combination: linear combination of the three previous heuristics, where the sum of the coefficients must be equal one.
- Max value: max value between out_of_place, out_of_order and manhattan_distance.

<ul>
<li>Out of place: number of pieces of out place compared to final configuration.</li>
<li>Out of order: number of pieces out of order in the numerical sequence, following the order of positions on the board.</li>
<li>Manhattan distance: standart Manhattan Distance.</li>
<li>Linear combination: linear combination of the three previous heuristics, where the sum of the coefficients must be equal one.</li>
<li>Max value: max value between out_of_place, out_of_order and manhattan_distance.</li>
</ul>
