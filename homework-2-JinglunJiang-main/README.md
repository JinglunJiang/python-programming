[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/xxkst2ud)
# Homework 2

The purpose of this homework is to practice functional programming.

As a result, there are special restrictions in place for this homework.

You may not use:

- `while`
- `len`
- the `in` operator (`x in y`)
- indexing such as `seq[n]` or `seq[n:m]`
- sequence methods like `list.append`, etc.
- `seq * N` for repetition
- `for` or `if` keyword (including in comprehensions)
- global variables
- the ternary operator syntax `X if Y else Z`
- max(), min(), sum(), all(), any()
- `import` statements other than `functools` and `operator`

You may use:

- helper functions, but they too must obey these restrictions
- `functools.reduce`
    - https://docs.python.org/3/library/functools.html#functools.reduce
    - https://realpython.com/python-reduce-function/
- `functools.partial`
    - https://docs.python.org/3/library/functools.html#functools.partial
    - https://www.learnpython.org/en/Partial_functions
- All other builtin functions like `map`, `filter`, `tuple`, `bool`, `list` are allowed. (e.g. `list(...)` can be useful to convert the result of a map/filter into a `list`.)
- Unpacking syntax like `a, b = (1, 2)`.

If in doubt about a function or language feature, you should ask on Ed and we will gladly clarify for everyone.

Please take special care to follow these instructions, use of a disallowed function or construct will result in significant deductions.

**You will also notice that most problems require you to create a new file, in contrast to the function stubs we provided previously.  Be sure to document your functions!**

## Problems

### Problem 1

Implement the `satisfy` and `satisfy_all` functions in a new file named `problem1/problem1.py`.

`satisfy` takes in two predicate functions (`func1` and `func2`) and a list of integers (`values`).

The function should return a list of two-element tuples. The first component of the tuple should be the integer from `values` and the second is `True` if both predicate functions return `True` and `False` otherwise.

Example:

```python
>>> import problem1
>>> problem1.satisfy(lambda x: x > 10, lambda y: y < 100, [1, 20, 200])
[(1, False), (20, True), (200, False)]

>>> problem1.satisfy(lambda x: x > 10, lambda y: y < 100, [])
[]

>>> problem1.satisfy(lambda x: x > 10, lambda y: y < 100, [2])
[(2, False)]
```

`satisfy_all` takes a list of predicates (`funcs`) and a list of integers (`values`).

The function should return a list of two-element tuples.
The first component is an integer from `values` and the second is a list of the return values from calling each predicate function with the integer.

```python
>>> import problem1
>>> funcs = [lambda x: x > 10, lambda y: y < 100]

>>> problem1.satisfy_all(funcs, [1, 20, 200])
[(1, [False, True]), (20, [True, True]), (200, [True, False])]

>>> problem1.satisfy_all(funcs, [])
[]

>>> funcs = [lambda x: x > 10, lambda y: y < 100, lambda z: False]
>>> problem1.satisfy_all(funcs, [1, 20, 200])
[(1, [False, True, False]), (20, [True, True, False]), (200, [True, False, False])]
```

Tests are provided in `problem1/test_problem1.py`.

### Problem 2

Implement a `count_all` function that takes in any number of lists and returns the total count of objects inside the lists.

```python
>>> import problem2

>>> problem2.count_all([1, 2, 3], ["a"], [3, 4, 5])
7
>>> problem2.count_all()
0
>>> problem2.count_all([], [])
0
>>> problem2.count_all([1], [], [3])
2
```

**Restriction**

Remember, you may not use `len`, you may want to use `functools.reduce` to reimplement it.

### Problem 3

Implement a `duplicate` function that takes a list of integers `values` and an additional integer `num`.

This function returns a list of tuples where each tuple contains an integer from `values` duplicated `num` times.

Example:
```python
>>> import problem3

>>> problem3.duplicate([1,2,3], 3)
[(1, 1, 1), (2, 2, 2), (3, 3, 3)]

>>> problem3.duplicate([], 3)
[]

>>> problem3.duplicate([1,2,3], 0)
[(), (), ()]

>>> problem3.duplicate([1,2,3], 1)
[(1,), (2,), (3,)]
```

**Restriction**

Remember, you may not use the `*` repetition operator for sequence types for this problem. You are free to write a helper function to perform this for you.

### Problem 4

Implement a `calc` function that takes in a string `op` representing an operation and two operands `a` and `b` and returns the result of a given calculation.

Example:
```python
>>> import problem4

>>> problem4.calc("+", 1, 2)
3

>>> problem4.calc("/", 5, 2)
2.5

>>> problem4.calc("*", "!", 4)
"!!!!"
```

Possible values for `op` are: `"+"`, `"-"`, `"*"`, `"/"`, and "%".

Note: You do not need to handle cases where the operation performed would be illegal (e.g. `calc("/", "!", "4")`).

**Restrictions**

Remember, you may not use an `if` statement.


### Problem 5

Implement the function `list_range` which takes a two-element tuple `bounds` and a list of integer lists `values`.

The function should return a list that includes each integer list from `values` where every member is within `bounds`.

`bounds` should be inclusive on both ends, so if `bounds = (1, 3)`, the list `[1, 2, 3]` is within bounds.

You may assume that the first component of bounds is always less than or equal to the second component.

Examples:
```python
>>> problem5.list_range((1, 3), [[1, 3, 2], [9, 3, 1], [2, 1]])
[[1, 3, 2], [2, 1]]

>>> problem5.list_range((1, 100), [[1, 3, 2], [9, 3, 1], [2, 1]])
[[1, 3, 2], [9, 3, 1], [2, 1]]

>>> problem5.list_range((1, 3), [])
[]

>>> problem5.list_range((1, 1), [[1, 3, 2], [9, 3, 1], [2, 1]])
[]
```

### Problem 6

You have been tasked with writing a function `transform_data` that takes in a list of dictionaries `data` and any number of keyword arguments.

The function should return a list of dictionaries where each dictionary has been modified according to the keyword arguments.

The following guarantees are made:

* Each dictionary in `data` will have the same keys.
* Each keyword argument will be a key in the dictionaries in `data`.
* The values of each keyword argument will be a function that takes in a single argument and returns a single value.

Example:
```python
>>> import problem6
>>> data = [
... {"name": "scott", "age": 29, "salary": 100000},
... {"name": "lauren", "age": 27, "salary": 200000},
... {"name": "paul", "age": 50, "salary": 84000},
]
# increment ages by 1
>>> new_data = problem6.transform_data(data, age=lambda x: x + 1)
>>> print(new_data)
[{'name': 'scott', 'age': 30}, {'name': 'lauren', 'age': 28}, {'name': 'paul', 'age': 51}]
# double salaries & fix name case
>>> new_data = problem6.transform_data(data, name=lambda x: x.title(), salary=lambda x: x * 2)
>>> print(new_data)
[{'name': 'Scott', 'salary': 200000, 'age': 29}, {'name': 'Lauren', 'salary': 400000, 'age': 27}, {'name': 'Paul', 'salary': 168000, 'age': 50}]
```

**Note**: The underlying dictionaries in `data` should not be modified.

To assist you in this, you are provided with a `process_record` function that modifies a single record.

```python
>>> import problem6
>>> data = {"name": "scott", "age": 29, "salary": 100000}
>>> problem6.process_record(data, dict(age=lambda x: x + 1, name=lambda s: s.title(), salary=lambda x: x * 2))
{'name': 'Scott', 'age': 30, 'salary': 200000}
```

This function has a bug in it though:
```python
>>> import problem6
>>> data = {"name": "scott", "age": 29, "salary": 100000}
>>> problem6.process_record(data, {"age": lambda x: x + 1})
KeyError: 'name'
```

It seems as if the function is not handling the case where a key is not present in the dictionary.

First, fix the bug in `process_record`. You may not modify the function signature.

(Hint: it is possible to fix this without adding any lines of code!)

Second, implement `transform_data` using `process_record`.

Tests are provided for both functions in `problem6/test_problem6.py`.