def satisfy(func1, func2, values):
  """
  Input: `satisfy` takes in two predicate functions (`func1` and `func2`) and a list of integers (`values`).
  Output: The function should return a list of two-element tuples. The first component of the tuple should be the integer from `values` and the second is `True` if both predicate functions return `True` and `False` otherwise.
  
  """
  result = map(lambda value: (value, func1(value) and func2(value)), values)
  return list(result)

def satisfy_all(funcs, values):
  """
  Input: `satisfy_all` takes a list of predicates (`funcs`) and a list of integers (`values`).
  Output: The function should return a list of two-element tuples.
  The first component is an integer from `values` and the second is a list of the return values from calling each predicate function with the integer.
  
  """
  result = map(lambda value: (value, list(map(lambda func: func(value), funcs))), values)
  return list(result)