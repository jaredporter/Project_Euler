def fib(n):
    """Calulate the sum of even Fibonacci numbers less than n."""
    # Create list of Fibonacci numbers.
    fib_nums = [0, 1]
    # Set a and b to initial values
    a, b = 0, 1
    # As long as the next number is less than n, increase a and b and add it
    # to the list.
    while b + a  < n:
        a, b = b, a + b
        fib_nums.append(b)

    # Eliminate odd numbers, then sum them.
    fib_nums = [value for value in fib_nums if value % 2 == 0]
    return sum(fib_nums)
