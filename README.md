# A* Algorithm - 15-Puzzle

## Introduction
First project of the class Algorithmic Modeling and Optimization.
Consist in a basic implementation of the search algorithm A* (A star) to solve the 15-puzzle game,
using different heuristics, as such: number of pieces out of place, number of pieces out of order,
Manhattan distance, linear combination between heuristics and maximum value between heuristics.
All functions were implemented in Python. Also an article was written (in portuguese)
comparing the efficiency of the heuristics.

## How to use

The program reads an input in the following format:

     1 5 9 2 6 10 13 3 7 11 14 4 8 12 0 15

This input correspond to the initial state (board):

<table>
  <tr>
    <td>1</td>
    <td>5</td>
    <td>9</td>
    <td>2</td>
  </tr>
  <tr>
    <td>6</td>
    <td>10</td>
    <td>13</td>
    <td>3</td>
  </tr>
  <tr>
    <td>7</td>
    <td>11</td>
    <td>14</td>
    <td>4</td>
  </tr>
  <tr>
    <td>8</td>
    <td>12</td>
    <td>0</td>
    <td>15</td>
  </tr>
</table>

<b>0 representing the blank space.</b>


## Configuration of the goal

The goal state is set as:

<table>
  <tr>
    <td>1</td>
    <td>5</td>
    <td>9</td>
    <td>13</td>
  </tr>
  <tr>
    <td>2</td>
    <td>6</td>
    <td>10</td>
    <td>14</td>
  </tr>
  <tr>
    <td>3</td>
    <td>7</td>
    <td>11</td>
    <td>15</td>
  </tr>
  <tr>
    <td>4</td>
    <td>8</td>
    <td>12</td>
    <td>0</td>
  </tr>
</table>
     
## Heuristics implemented

- Out of place: number of pieces of out place compared to final configuration.
- Out of order: number of pieces out of order in the numerical sequence, following the order of positions on the board
- Manhattan distance: standart Manhattan Distance.
- Linear combination: linear combination of the three previous heuristics, where the sum of the coefficients must be equal one.
- Max value: max value between out_of_place, out_of_order and manhattan_distance.
