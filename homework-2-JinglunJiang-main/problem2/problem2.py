import functools
import operator

def count_all(*lists):
  """
  Input: takes in any number of lists.
  Output: returns the total count of objects inside the lists.

  """
  newlist = functools.reduce(operator.add, lists, [])
  result = functools.reduce(lambda count, _: count + 1, newlist, 0)
  return result
