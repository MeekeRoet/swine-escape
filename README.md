# Swine escape


### Table of contents
  * [Game instructions](#game-instructions)
  * [Solution](#solution)
  * [Illustration of gameplay](#illustration-of-gameplay)



### Game instructions
Consider the following board game: A game board has 12 spaces. The swine senses the Christmas spirit and manages to run away from home couple of weeks beforehand. Fortunately for it, the butcher is a bit of a drunkard and easily distracted. The swine starts on space 7, and the butcher on space 1. On each game turn a 6-sided die is rolled. On an outcome from 1 to 3, the swine moves that many spaces forward. On an outcome of 5 or 6, the butcher moves that many spaces forward. On the outcome 4, both advance one space. The swine wins if it reaches the river, located at space 12. The final roll does not have to be exact, moving past space 12 is OK. The butcher wins if he catches up with the swine (or moves past it).


**What are the probabilities of winning for the swine and the butcher?**

Your assignment is to create a mathematical or statistical model to find these probabilities, and implement the solution as a computer program in whatever language you like. Consider the following questions as well:

* Can you make your model easily extendable for different initial conditions (board size and initial positions)?
* Pros and cons of the approach?
* Can you say something about how long the game takes (also under different initial conditions)?


### Solution

The questions were tackled using three different approaches: a [Markov chain](../master/markov.ipynb) and a [dynamic programme](../master/dp.ipynb) (DP), both exact, and by [simulation](../master/simulation.ipynb), an approximation. 

The Markov and DP solvers can be called from the command line using ``python solve_game.py``, optionally providing board length (``-l``), swine starting position (``-s``), butcher starting position (``-b``), and solution method (``-m``) as arguments to run a different game/solver than the default. For instance, ``python solve_game.py -l 12 -s 7 -b 1 -m dp`` will solve the default game using DP.

Furthermore, the simulation results were processed into a [Tableau dashboard](https://public.tableau.com/profile/meeke.roet#!/vizhome/Dashboardswineescape/Swineescapedashboard) showing the approximated winning probabilities and length of the game for various combinations of starting positions and board length.




### Illustration of gameplay

The below GIF demonstrates the gameplay when the butcher (grey) starts at square 1, the swine (pink) starts at square 7, and the board is 20 squares long. The code used to generate the animation can be found in [swine-escape-simulation.ipynb](../master/swine-escape-simulation.ipynb) under Animation.

![Output sample](https://github.com/MeekeRoet/swine-escape/blob/master/swine-escape.gif)
