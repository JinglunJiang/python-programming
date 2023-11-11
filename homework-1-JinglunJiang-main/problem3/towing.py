from pathlib import Path
import datetime

path = Path(__file__).parent/"towing.csv"
number_vehicles = {}
with path.open() as fd:
    lines = fd.readlines()
    for line in lines[1:]:
        date = line.split(',')[0]
        number_vehicles[date] = number_vehicles.get(date, 0) + 1
vehicles_list = list(number_vehicles.items())   

def top_days(n):
    """
    Returns the top days that vehicles were towed.

    Inputs:
        n (int): Number of days to return.

    Output:
        A list of tuples where the first item is a date and the second item the number of vehicles towed on that date.
        There should only be 'n' elements, ordered by vehicles towed on the day.

        For example:
            [
              ("06/15/2022", 82),
              ("05/01/2022", 51),
              ("05/11/2022", 39),
            ]
    """
    result = []
    sorted_list_descending = sorted(vehicles_list, key=lambda x: x[1], reverse=True)
    for i in range(n):
        result.append(sorted_list_descending[i])
    return result

def day_summary():
    """
    Return a list of all days in chronological order, along with the number of cars towed for
    each day.

    Output:
        A list of tuples where the first item is a date and the second item the number of vehicles towed on that date.

        For example:
            [
              ("07/01/2022", 5),
              ("07/02/2022", 30),
              ... # truncated
              ("09/29/2022", 76),
            ]
    """
    sorted_list = sorted(vehicles_list, key=lambda x: x[0])
    return sorted_list