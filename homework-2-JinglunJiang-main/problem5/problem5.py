def list_range(bounds, values):
  """
  Input: takes a two-element tuple `bounds` and a list of integer lists `values`
  Output: return a list that includes each integer list from `values` where every member is within `bounds`
  
  `bounds` should be inclusive on both ends, so if `bounds = (1, 3)`, the list `[1, 2, 3]` is within bounds
  the first component of bounds is always less than or equal to the second component
  """
  def within_range(list):
    "checks if a single list is within the range"
    sorted_list = sorted(list)
    return (not list) or (sorted_list[0] >= bounds[0] and sorted_list[-1] <= bounds[1])
  return list(filter(within_range, values))



