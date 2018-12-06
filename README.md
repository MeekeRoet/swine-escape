# Swine escape


## Table of contents
  * [Introduction](#introduction)
  * [Game instructions](#game-instructions)
  * [Organization of the repository](#organization-of-the-repository)


## Introduction
This repository contains code for a mathematical brainteaser/programming challenge that was presented to me during a job application procedure.


## Game instructions
Consider the following board game: A game board has 12 spaces. The swine senses the Christmas spirit and manages to run away from home couple of weeks beforehand. Fortunately for it, the butcher is a bit of a drunkard and easily distracted. The swine starts on space 7, and the butcher on space 1. On each game turn a 6-sided die is rolled. On an outcome from 1 to 3, the swine moves that many spaces forward. On an outcome of 5 or 6, the butcher moves that many spaces forward. On the outcome 4, both advance one space. The swine wins if it reaches the river, located at space 12. The final roll does not have to be exact, moving past space 12 is OK. The butcher wins if he catches up with the swine (or moves past it).


**What are the probabilities of winning for the swine and the butcher?**

Your assignment is to create a mathematical or statistical model to find these probabilities, and implement the solution as a computer program in whatever language you like. Consider the following questions as well:

* Can you make your model easily extendable for different initial conditions (board size and initial positions)?
* Pros and cons of the approach?
* Can you say something about how long the game takes (also under different initial conditions)?


## Illustration of gameplay

![Output sample](https://github.com/MeekeRoet/swine-escape/blob/master/swine-escape.gif)


## Organization of the repository

I tackled the questions with 2 different approaches: by simulation (approximate) and using a Markov chain (exact).
