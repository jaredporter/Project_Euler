import re

def load_grid(location):
    """Load the file with the grid into a list of lists."""
    numFile = open(location, "r")
    grid = []
    for line in numFile.read().splitlines():
        grid.append([int(number) for number in re.split('\s+', line)])
    return grid

def largest_product(lst):
    """find the largest product of 4 consecutive numbers in any direction."""
    max_product = 0

    # Find the horizontal (first) and the vertical (second) products and check
    # to see if the new max, if it is, set max_product to the value.
    for i in range(20):
        for j in range(16):
            product = lst[i][j] * lst[i][j+1] * lst[i][j+2] * lst[i][j+3]
            if product > max_product:
                max_product = product
            product = lst[j][i] * lst[j+1][i] * lst[j+2][i] * lst[j+3][i]
            if product > max_product:
                max_product = product

    # Find the diagonal products (up and right then down and left) and check to
    # see if it's the new max. If so, set max_product to the value.
    for i in range(16):
        for j in range(16):
            product = lst[i][j] * lst[i+1][j+1] * lst[i+2][j+2] * lst[i+3][j+3]
            if product > max_product:
                max_product = product

    for i in range(3,20):
        for j in range(16):
            product = lst[i][j] * lst[i-1][j+1] * lst[i-2][j+2] * lst[i-3][j+3]
            if product > max_product:
                max_product = product

    return max_product
