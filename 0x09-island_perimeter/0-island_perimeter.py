#!/usr/bin/python3
"""
def  returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # check sides
                if r == 0 or grid[r-1][c] == 0:  # top side
                    perimeter += 1
                if r == rows-1 or grid[r+1][c] == 0:  # bottom side
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:  # left side
                    perimeter += 1
                if c == cols-1 or grid[r][c+1] == 0:  # right side
                    perimeter += 1

    return perimeter
