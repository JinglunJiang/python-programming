import operator
import functools

def calc(op, a, b):
  """
  Input: takes in a string `op` representing an operation and two operands `a` and `b`
  Output: returns the result of a given calculation.
  """
  dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod
  }
  return dict[op](a, b)


  