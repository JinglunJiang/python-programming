[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ibtlKy13)
# Homework 6

The nature of our field is that there is always more to learn, and you will often need to teach yourself new things. This assignment is geared at giving practice with that, leveraging the skills you've learned in this class to explore new libraries and APIs.

## Problem 1

For this problem, you'll be making a request to a working API that provides historical weather information.

You may want to read through the section labeled "API Example" below before getting started.

A big part of this assignment will be learning to use some built-in modules that we haven't covered in class.

We will point you towards the modules/functions we expect you to use, but it'll be up to you to explore their usage.

You will need to build two pieces:

### `download.py`

First, open download.py and implement the `save_json` function. The steps listed in that file indicate classes and methods you will need to use.

Once you have a working version of `download.py` run the following (from your `homework6` directory) to get 100 days of Chicago weather:

`python3 problem1/download.py 41.85 -87.65 100`

Which will write a `weather.json` file to disk.

Note: In practice you'd often combine both of these parts into one program. We are splitting the program up to avoid having you repeatedly hit the open-meteo.com API unnecessarily. Do not run your `download.py` script repeatedly once it is working, it is using a free service.

### `stats.py`

Once you have a `weather.json` file, you should open `stats.py` and implement `process_weather_data` as indicated in the docstring and comments.

Running `python3 problem1/stats.py` should result in output like:

```
       Weather Report
===========================
2022-08-01       2022-11-09
===========================
High Temperature:     31.7
     Average:         22.1
     Std. Dev:         5.8
Low Temperature:       1.2
     Average:         13.6
     Std. Dev:         6.2
```

(Note: Your values will not match exactly since you won't be running on the same day.)

### API Example

If you open your browser to the URL: https://archive-api.open-meteo.com/v1/era5?latitude=41.85&longitude=-87.65&start_date=2022-01-01&end_date=2022-07-13&daily=temperature_2m_max,temperature_2m_min&timezone=auto

You'll get a response that looks like this:

```
{"latitude":41.75,"longitude":-87.75,"generationtime_ms":0.7529258728027344,"utc_offset_seconds":-18000,"timezone":"America/Chicago","timezone_abbreviation":"CDT","elevation":192.0,"daily_units":{"time":"iso8601","temperature_2m_max":"°C","temperature_2m_min":"°C"},"daily":{"time":["2022-01-01","2022-01-02","2022-01-03","2022-01-04","2022-01-05","2022-01-06","2022-01-07","2022-01-08","2022-01-09","2022-01-10","2022-01-11","2022-01-12","2022-01-13","2022-01-14","2022-01-15","2022-01-16","2022-01-17","2022-01-18","2022-01-19","2022-01-20","2022-01-21","2022-01-22","2022-01-23","2022-01-24","2022-01-25","2022-01-26","2022-01-27","2022-01-28","2022-01-29","2022-01-30","2022-01-31","2022-02-01","2022-02-02","2022-02-03","2022-02-04","2022-02-05","2022-02-06","2022-02-07","2022-02-08","2022-02-09","2022-02-10","2022-02-11","2022-02-12","2022-02-13","2022-02-14","2022-02-15","2022-02-16","2022-02-17","2022-02-18","2022-02-19","2022-02-20","2022-02-21","2022-02-22","2022-02-23","2022-02-24","2022-02-25","2022-02-26","2022-02-27","2022-02-28","2022-03-01","2022-03-02","2022-03-03","2022-03-04","2022-03-05","2022-03-06","2022-03-07","2022-03-08","2022-03-09","2022-03-10","2022-03-11","2022-03-12","2022-03-13","2022-03-14","2022-03-15","2022-03-16","2022-03-17","2022-03-18","2022-03-19","2022-03-20","2022-03-21","2022-03-22","2022-03-23","2022-03-24","2022-03-25","2022-03-26","2022-03-27","2022-03-28","2022-03-29","2022-03-30","2022-03-31","2022-04-01","2022-04-02","2022-04-03","2022-04-04","2022-04-05","2022-04-06","2022-04-07","2022-04-08","2022-04-09","2022-04-10","2022-04-11","2022-04-12","2022-04-13","2022-04-14","2022-04-15","2022-04-16","2022-04-17","2022-04-18","2022-04-19","2022-04-20","2022-04-21","2022-04-22","2022-04-23","2022-04-24","2022-04-25","2022-04-26","2022-04-27","2022-04-28","2022-04-29","2022-04-30","2022-05-01","2022-05-02","2022-05-03","2022-05-04","2022-05-05","2022-05-06","2022-05-07","2022-05-08","2022-05-09","2022-05-10","2022-05-11","2022-05-12","2022-05-13","2022-05-14","2022-05-15","2022-05-16","2022-05-17","2022-05-18","2022-05-19","2022-05-20","2022-05-21","2022-05-22","2022-05-23","2022-05-24","2022-05-25","2022-05-26","2022-05-27","2022-05-28","2022-05-29","2022-05-30","2022-05-31","2022-06-01","2022-06-02","2022-06-03","2022-06-04","2022-06-05","2022-06-06","2022-06-07","2022-06-08","2022-06-09","2022-06-10","2022-06-11","2022-06-12","2022-06-13","2022-06-14","2022-06-15","2022-06-16","2022-06-17","2022-06-18","2022-06-19","2022-06-20","2022-06-21","2022-06-22","2022-06-23","2022-06-24","2022-06-25","2022-06-26","2022-06-27","2022-06-28","2022-06-29","2022-06-30","2022-07-01","2022-07-02","2022-07-03","2022-07-04","2022-07-05","2022-07-06","2022-07-07","2022-07-08","2022-07-09","2022-07-10","2022-07-11","2022-07-12","2022-07-13"],"temperature_2m_max":[4.1,-1.0,-5.6,1.5,1.5,-10.8,-10.6,1.3,2.0,-8.2,2.5,4.4,4.2,2.1,-2.8,-2.1,-1.7,5.8,5.4,-7.5,-3.8,0.5,-4.8,-2.4,-10.9,-11.7,-0.4,-2.3,-5.7,-1.0,0.3,6.4,1.4,-3.9,-4.6,-8.9,-1.0,-1.4,3.0,4.4,1.8,7.3,-0.5,-7.1,-3.3,4.0,11.7,9.2,0.3,0.7,9.2,9.6,9.7,-4.0,-2.7,-1.4,0.6,5.1,10.8,9.8,12.9,2.5,4.2,18.8,15.4,3.3,3.2,5.8,-1.1,-0.1,-5.3,10.3,14.7,10.0,18.3,17.6,7.4,5.6,15.4,20.3,12.8,13.2,8.0,7.7,2.1,1.2,-0.3,5.7,14.8,11.3,5.5,5.2,8.3,10.6,12.2,12.6,7.7,4.7,7.4,15.6,15.2,18.4,19.0,9.9,10.9,8.4,4.2,4.8,8.6,11.2,18.2,15.0,25.5,21.4,13.9,10.0,4.4,11.6,16.5,18.5,14.1,12.6,9.7,9.8,11.7,10.5,14.3,17.8,24.9,28.9,29.2,28.8,28.7,24.6,21.8,23.3,16.6,16.3,26.7,28.3,17.0,15.9,14.3,16.9,23.6,23.7,18.2,21.5,26.3,28.8,28.3,23.4,23.3,25.9,19.3,23.6,24.1,17.4,18.6,24.7,22.8,22.9,19.6,29.0,33.9,33.0,31.8,27.7,19.9,27.5,31.5,33.6,29.3,25.7,29.5,25.9,25.7,23.0,27.6,27.7,30.8,25.1,26.0,27.9,29.5,31.2,24.6,26.5,23.5,22.7,27.4,28.9,28.3,26.5],"temperature_2m_min":[-0.8,-7.5,-14.6,-5.7,-11.2,-13.8,-18.3,-10.4,-9.9,-12.7,-13.3,-0.6,-0.5,-2.3,-6.1,-11.6,-4.1,-4.6,-9.2,-12.7,-10.3,-7.2,-12.9,-14.6,-16.6,-22.0,-11.4,-11.7,-15.8,-11.6,-8.7,-0.3,-5.2,-5.0,-9.5,-14.8,-9.0,-9.6,-9.9,-0.2,-2.4,-0.5,-8.7,-9.6,-9.7,-5.8,4.8,-6.2,-15.1,-12.4,-7.7,0.1,-3.8,-7.6,-4.2,-5.0,-9.3,-2.5,-2.0,1.1,-0.4,-2.1,-2.7,3.7,3.4,-0.2,-3.1,-1.4,-4.1,-6.6,-11.5,-6.7,2.5,0.9,2.0,7.5,4.3,2.6,-0.2,4.9,8.9,8.6,4.6,2.8,-1.1,-3.8,-4.2,-1.9,5.5,1.7,-0.6,0.4,-0.1,5.1,2.3,8.1,4.4,1.8,0.6,-0.1,9.2,2.0,7.0,2.3,4.4,1.2,-0.8,1.4,2.0,5.4,10.0,8.8,13.3,14.9,6.1,3.5,1.4,3.3,9.5,10.8,10.4,8.8,6.2,5.0,5.9,8.8,7.6,8.1,12.6,18.7,20.9,21.1,18.0,16.7,14.4,12.5,11.1,11.9,11.7,17.8,12.3,10.8,8.7,9.8,14.0,18.3,10.6,9.3,16.7,20.2,22.1,15.0,14.9,14.9,12.6,14.5,16.0,13.0,13.9,11.6,14.7,14.6,14.2,13.7,22.8,25.2,21.9,20.4,13.9,12.5,18.8,21.3,24.1,19.1,17.1,20.3,20.2,15.9,14.8,19.3,21.4,19.6,17.0,18.7,19.9,24.0,19.8,19.7,20.8,18.6,16.1,20.9,20.6,19.2]}}
```

(your browser may reformat it for readability)

Though messy, this looks a lot like Python's dictionaries & lists!

This is a format known as JSON (JavaScript Object Notation) that is widely used for the interchange of data online.
The specifics of JSON syntax differ slightly from Python, you can look at the [JSON specification here](https://www.json.org/json-en.html) if you want.

For our purposes though, we'll be receiving this data as one big string, and then using the [`json`](https://docs.python.org/3/library/json.html) module to convert that data into Python objects.

Tips:
  * If you'd like to see the JSON output formatted nicely, `python -m json.tool weather.json` will print the data neatly formatted.  This can be useful to figure out the nested structure of the data.
  * The data will likely have `null` values in it.  `null` is the JSON equivalent of `None` and when you load the data into Python you'll wind up with `None` values.  Be sure to filter those out!

## Problem 2

For this assignment you will be looking at a third party library, and getting it running on your own machine.

Whichever library you choose you will be doing the following:

1) Install the library: `poetry add <library name>` (e.g. `poetry add click`) . Be sure to commit `pyproject.toml` and `poetry.lock` after installing.
2) Read through the library's provided tutorial, following along by running the example code they provide and modifying it to better understand how it works.
3) Write a short demo program using some of the concepts you've learned.  Specific requirements may be given below, but all demo programs must:
  - *NOT* just be code from the tutorial, modify it in some way to make it your own -- add in your own test data, etc.
  - Aim for 50 lines of code minimum.  Lines of code is typically a bad metric, but we're mentioning this so nobody feels like they need to write 500 lines, or thinks that 10 lines is adequate.
  - Be runnable if the required package is installed.
4) Write reasonable tests for your program, placed in `problem2/test_problem2.py`.  These tests should be runnable with `pytest`.  Your tests should follow the best practices outlined in the testing notes discussed in class.
5) Be sure to answer the questions provided in problem2/questions.md.

## Recommended Libraries

You may pick any of these libraries:

### [Click](https://click.palletsprojects.com/en/8.1.x/)

This is a library to help parse command line options and make your own command line utilities.

First, follow along with the Quickstart: https://click.palletsprojects.com/en/8.1.x/quickstart/

Second, write a short original program that uses the library.  The program should do at least two different things depending on what parameters it is called with. It should use the features shown in the quickstart and any other `click` features you'd like to experiment with.

It should be possible for us to run your program by running `python problem2/problem2.py`.

### [Pillow](https://pillow.readthedocs.io/en/stable/)

This is a library for manipulating images, which we've used in Homework #5.

First, take a look at the [tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html).

Second, write a short original program that uses the library.  The program should at minimum load an image from disk and manipulate it in some way.  Be sure to check in any required image(s) you use so we can run your program.

It should be possible for us to run your program by running `python problem2/problem2.py`.

### [Flask](https://flask.palletsprojects.com)

Flask is a library to write web applications.  If you choose this project you should be at least somewhat familiar with HTML.

First, follow the [quickstart](https://flask.palletsprojects.com/en/2.2.x/quickstart/).

Second, write a short original program that has at least two endpoints, one of which should use a variable rule as shown in the quickstart.

It should be possible for us to run your program by running `python problem2/problem2.py`

### [networkx](https://networkx.org/documentation/stable/index.html)

NetworkX is a library for graph/network analysis in Python.

First, read through the first half of the [tutorial](https://networkx.org/documentation/stable/tutorial.html) (You can stop when you get to Multigraphs if you like, everything below there is more advanced than you'll need.)

Second, write a short original program that explores some of the features shown in the tutorial.

### Others

If there is a library you're aware of that you'd like to explore, you may request permission to do so.

Please submit your request early so that I can make sure it is appropriate for the assignment.

You may *not* choose `pandas`, `scipy`, `matplotlib`, or `seaborn`.
