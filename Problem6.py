def natural_less_squares(n):
    """
    Find the difference between the sum of squares and the sum 
    of the first n natural numbers squared.
    """
    natural = n * (n+1) / 2
    squares = (n * (n + 1) * (2 * n + 1)) / 6
    difference = natural ** 2 - squares
    return difference
