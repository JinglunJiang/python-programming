def find_duplicates(name_list):
    """
    This function compares two lists, and finds any values that occur more than once.

    The output list should only contain names that occurred more than once.
    No name should appear more than once in the output list, no matter how many times it appears.

    Inputs:
            name_list(list): A list of names.

    Output:
            A new list containing each value that was duplicated once and only once.
    """
    new_list = []

    for name in name_list:
        if name_list.count(name) > 1 and name not in new_list:
            new_list.append(name)

    return new_list