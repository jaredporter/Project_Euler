def comb_path_length(n):
    """Using combinatorics, find how many paths there are in an n x n grid."""
    
    num_paths = 1
    # Using the Binomial Coefficient, find number of combinations.
    for i in range(n):
        num_paths *= 2 * n - i
        num_paths /= i + 1

    return num_path

def dynamic_paths(n):
    """
    Using a dynamic solution, find how many paths there are in an n x n
    grid.
    """
    
