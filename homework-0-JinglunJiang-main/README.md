[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/bNUE_9mM)
# Homework 0

## Goals

This homework is shorter than most, the primary goal is to ensure you are familiar with your Python environment, running tests, and using GitHub Classroom and Gradescope.

* Ensure you have a working development environment
* Familiarize yourself with the course software
* Practice writing short Python functions.

## Reminders

### Git & GitHub
If you haven't already gotten set up with GitHub, you'll want to look at [Git Basics](https://uchicago-cs.github.io/student-resource-guide/tutorials/git-basics.html) from the UChicago CS Student Resource Guide.

### Environment 

As mentioned in class, the supported environment is provided on the CS Linux machines. If you are working via SSH you shouldn't need to do anything additional to get started.

Take a look at [Using VS Code and SSH](https://uchicago-cs.github.io/student-resource-guide/vscode/ssh.html) if you want to edit files on your machine and run them on the department Linux servers.

You should be able to run `pytest` from the command line and see the tests run.

If you decide to use your own environment, please refer to [Using Poetry](https://people.cs.uchicago.edu/~jturk/mpcs51042/assignments/general/#using-poetry) from the course site to get started.

You are always free to develop in a setup of your choosing, but due to the infinite possible variations stemming from different operating systems, versions of Python, etc. we will not be able to provide support for issues you may run into specific to your local environment.

### Style Guide

We expect you to follow the department [style guide](https://uchicago-cs.github.io/student-resource-guide/style-guide/python.html).

This is a significant portion of our grading, particularly on this assignment.  Using a [linter](https://uchicago-cs.github.io/student-resource-guide/style-guide/python.html#linters) can be helpful.

### Running `pytest`

Each problem comes with some helpful tests.  These are not guaranteed to be comprehensive, it may benefit you to consider other cases as well.

You can run `pytest` from this directory to run all tests for the homework.

To just run a subset of tests, you can specify the directory name, e.g. `pytest problem1`.

If you'd like `pytest` to stop after a single failure, add the `-x` flag.

For more pytest tips, see [pytest](https://people.cs.uchicago.edu/~jturk/mpcs51042/assignments/general/#pytest).

## Problems

### Problem 1

Open `problem1/leap_year.py`, implement the `is_leap_year` function according to the specifications provided.

### Problem 2

Open `problem2/duplicates.py`, implement the `find_duplicates` function according to the specifications provided.

### Problem 3

The Collatz conjecture is a famous unsolved problem in math that asks if the function

![](collatz.svg)

converges on 1 for all initial values of n.

(Source: https://en.wikipedia.org/wiki/Collatz_conjecture)

We're going to implement two functions that will allow us to test given values of n.

Open `problem3/collatz.py`, implement the two functions.

Note: Keep the difference between `/` and `//` in mind.

Reference: https://docs.python.org/3/glossary.html#term-floor-division