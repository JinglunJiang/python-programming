def get_sector(grid, row_bounds, col_bounds):
    """
    Get all the values within a sector.

    A sector is defined by a row and column boundary.

    A row boundary is a tuple of two integers in the range [0, numRows).
    A column boundary is a tuple of two integers in the range [0, numColumns).

    Note that the upper bounds are exclusive!

    Based on the boundary specified, this function returns a list of all values
    found in the specified sector.

    Order in the list does matter!
    Start at the top-left of the sector and work your way down towards the bottom-right corner.
    You'll go through one column at a time.
    Once you finish with a row then you move to the next row (i.e., increase by 1).

    You can assume the the first component of the boundary is always less than the second component.

    For a grid like:
    [
        [A, B, C],
        [D, E, F],
        [G, H, I]
    ]
    If your bounds were (0, 2) and (0, 2) you'd return [A, B, D, E].

    Inputs:
        grid(list of list of bools): the status of the homes
        row_bounds(tuple of ints): the row boundary for the sector
        col_bounds(tuple of ints): the column boundary for the sector

    Outputs:
        Returns a list of the values contained within the specified bounds.
    """
    result = []

    for i in range(row_bounds[0], row_bounds[1]):
        for j in range(col_bounds[0],col_bounds[1]):
            result.append(grid[i][j])

    return result