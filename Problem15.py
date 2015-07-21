def comb_path_length(n):
    """Using ombinatorics, find how many paths there are in an n x n grid."""
    
    num_paths = 1
    # Using the Binomial Coefficient, find number of combinations.
    for i in range(n):
        num_paths *= 2 * n - i
        num_paths /= i + 1

    return num_paths
