import functools


def process_record(record, transforms):
    """
    Given an item and a dictionary mapping keys to functions,
    use the given functions to transform the item's values.

    NOTE: This code currently has a bug in it!

    Arguments:
        * record : dict[str, Any] - A dictionary with data to be modified.
                                    Every key in the dictionary is a string.
        * transforms : dict[str, Callable] - A dictionary mapping keys to functions.
                                             Every key in transforms is a key from record.
    """
    # This code maps each item in the dictionary to a tuple (key, new_value)
    #   item[0] is the key, item[1] is the value
    # calling dict() on an iterable of tuples creates a dictionary
    return dict(
        map(lambda item: (item[0], transforms.get(item[0], lambda x : x)(item[1])), record.items())
    )

def transform_data(data, **kwargs):
    """
    Input: takes in a list of dictionaries `data` and any number of keyword arguments.

    Output: should return a list of dictionaries where each dictionary has been modified according to the keyword arguments.

    The following guarantees are made:

    * Each dictionary in `data` will have the same keys.
    * Each keyword argument will be a key in the dictionaries in `data`.
    * The values of each keyword argument will be a function that takes in a single argument and returns a single value.
    
    """
    result = map(lambda list: process_record(list, kwargs), data)
    return list(result)
