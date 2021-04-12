# A* Algorithm - 15-Puzzle

## Introduction
Consist in a basic implementation of the search algorithm A* (A star) to solve the 15-puzzle game,
using different heuristics, as such: number of pieces out of place, number of pieces out of order,
Manhattan distance, linear combination between heuristics and maximum value between heuristics.
All functions were implemented in Python. Also an article was written (in portuguese)
comparing the efficiency of the heuristics.

<b>First project of the class Algorithmic Modeling and Optimization.</b>

## How to use

### Input

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

### Selecting heuristics

The selection of the heuristic is made on the line 166: 

      sucessor.hcost = heuristic_1(sucessor.state)

Change the name <b>"heuristic_n (sucessor.state)"</b> with <b>"n"</b> being one of the following number:

  <b>1</b> - Out of place</br>
  <b>2</b> - Out of order</br>
  <b>3</b> - Manhatthan distance</br>
  <b>4</b> - Linear combination</br>
  <b>5</b> - Maximum value</br>

### Output

The output format will be:

> Movements: <i><b>n</b></i><br>
Memory usage (in bytes): <i><b>n</b></i><br>
Execution time: <i><b>n</b></i> s<br>

## Configuration of the final board

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
