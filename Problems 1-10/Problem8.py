from operator import mul
from collections import deque

def loadNum():
    # Import file with 1000 digit number
    numFile = open("longNum.txt", "r")
    # Read number into list, spliting by digit. Then convert all to ints
    num = numFile.readlines()
    num = list(str(num[0]))
    num = list(map(int, num))
    return num

def window(iterable, n):
    """Sliding window generator"""
    # Make list into iterator object
    it = iter(iterable)
    # Create a double-ended queue of length n with iterator object it.
    d = deque((next(it) for Null in range(n-1)), n)
    # Generate a list of size n as it slides through the queue.
    for elem in it:
        d.append(elem)
        yield list(d)

def largestMult(lst):
    """Calculate the 13 consecutive digits which produce the highest product"""
    product = 0
    # Run through the generator, if the subset doesn't contain a zero, multiply it
    # all together and check to see if it's the new max. Retun the highest value.
    for x in window(lst, 13):
        if 0 not in x:
            prod = reduce(mul, x, 1)
            if prod > product:
                product = prod
        else:
            pass
    return product

