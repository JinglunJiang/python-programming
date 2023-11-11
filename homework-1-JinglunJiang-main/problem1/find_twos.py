def find_twos(str1, str2):
    """
    This function takes in two strings that only contain integers, commas and whitespace and
    returns a list of integers, where each integer:
       1. Appears in both strings
       2. Contains a 2 as a digit in the number.

    Inputs:
        str1, str2 (string): strings that contains integers, commas, and whitespace.
        You can assume each integer is separated by a single comma followed by
        zero or more whitespaces.

    Output:
        A list of integers, where the list contents is described by above. The returned list
        must not contain duplicates.

        The order of items in the list should match the order of the inputs in str1.
    """
    second = [] 
    for num in str2.split(','):
        if '2' in num:
            second_num = int(num.strip())
            if second_num not in second:
                second.append(second_num)

    first = []
    for num in str1.split(','):
        num = num.strip()
        if int(num) in second and int(num) not in first:
            first.append(int(num))

    return first
