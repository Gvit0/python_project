# python_project
![Rubut](https://img.shields.io/badge/Ru-37a779?style=for-the-badge)
[Rubut]:/RU.md
# list:
### machine_vision.py
### recursive_function_x_y_sum_search.py
### petya_strategy.py


## machine_vision.py
input:
```
 _   _
|_   _|   | |_|
|_| |_    |   |
```
output:
```6214```
## recursive_function_x_y_sum_search.py
This code defines a recursive function F(x, y, n) that takes three arguments: x, y, n. The function checks if the sum of x and y greater than 39 when n is equal to 1. If n is not equal to 1 the function recursively calls itself with either x or y updated to be the sum of the current value and itself, depending on which value is larger.

The code also initializes an empty list m to store the sums of x and y for which the function F returns True. The list m is populated by iterating over all possible values of x and y from 0 to 19, and checking if F(x, y, 0) returns True.

Finally, the code prints the minimum value in the list m. This code can be used to find the minimum sum of x and y for which the function F returns True when n is 0.

In summary, this code defines a recursive function F that checks if the sum of two numbers is greater than 39 when a certain condition is met, and then finds the minimum sum of those two numbers for which the function returns True when n is 0.

## petya_strategy.py 
Python code that solves the problem of the stone game.

Problem Description
Two players, Petya and Vasya, are playing a game with two heaps of stones. The first heap has 12 stones, and the second heap has S stones. Players take turns to remove either all the stones from one heap or an equal number of stones from both heaps. The player who removes the last stone wins the game.

Objective
The goal is to find the minimum value of S, such that Petya cannot win the game in one move, but Vasya can win the game in his first move, regardless of Petya's move.
