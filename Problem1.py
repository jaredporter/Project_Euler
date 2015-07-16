def largest_mult(val1, val2, n):
    """Find the sum of all multiples of val1 or val2 below n."""
    lst = [value for value in range(1,n) if value % val1 == 0 or value % val2 == 0]
    total = sum(lst)
    return total
