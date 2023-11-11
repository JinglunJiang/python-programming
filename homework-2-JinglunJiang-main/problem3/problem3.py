import functools
import operator

def duplicate(values, num):
  """
  Input: akes a list of integers `values` and an additional integer `num`.
  Output: This function returns a list of tuples where each tuple contains an integer from `values` duplicated `num` times.
  
  """
  result = map(lambda value : helper(value, num), values)
  return list(result)

def helper(value, num):
  """
  iteration helper

  """
  result = functools.reduce(lambda a, _: a + (value,), range(num), ())
  return tuple(result)