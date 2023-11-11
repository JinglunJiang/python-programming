# File I/O Addendum

Problems 3 & 4 require you to read from files for the first time.

We'll be covering File I/O in more detail in class, but here's a quick primer that'll help you with the homework problems.

## pathlib

Python has a built in module called `pathlib` that makes working with files and directories easier.

Note: This module was added in Python 3.4, so you will still see code that uses the older `open` built-in function, which works with paths as strings instead. It is highly recommended you use `pathlib` for all new code.

To use `pathlib` you first need to import it:

```python
from pathlib import Path
```

Then you can create a `Path` object by passing a string to the constructor:

```python
path = Path("towing.csv")
```

This will create a `Path` object that represents the file `towing.csv` **in the current directory**.

If you are running your code from the homework1 directory instead of homework1/problem3 or similar, you'd need to modify this path to be `Path("problem3/towing.csv")`.

### Building an absolute path

Since ideally your code would run regardless of what directory you run from, you can use the `__file__` variable to get the path to the current file:

```python
from pathlib import Path

path = Path(__file__).parent / "towing.csv"
```

This line uses the special built-in variable `__file__` to get the path of the Python file itself.
It then gets this file's parent directory (`.parent`) and appends the filename "towing.csv" to it.

You'll want to use this technique in your code so that it works regardless of what directory you run it from.

### Reading from a file

To open a file for reading, you can use the `open` method on a `Path` object:

```python
from pathlib import Path

path = Path(__file__).parent / "towing.csv"
with path.open() as fd:
    # read entire file into one string
    contents = fd.read()
    # or to read the file line by line:
    lines = fd.readlines()
```

You can pick whichever of these you prefer for problems 3 and 4.  (Note you can only use one of them, not both.)

Once the data is read from the file you can process it using the various string methods we've already covered.

### Reading from a file multiple times

If you try to read from a file multiple times, you'll find that the second time you read from it you get an empty string.

This is why you should pick `read()` OR `readlines()`.

We'll discuss the `file` object more in class, including why this is the case.