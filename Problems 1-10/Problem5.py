from Problem7 import sieveOfEra
from math import log, floor

def smallest_dividable(n):
    """
    Find the smallest number which is dividable by all numbers from 1 to n
    utilizing prim factorization
    """
    primes = []
    smallest = 1

    # Add all of the primes to the list primes, which are less than n.
    for num in sieveOfEra():
        if num <= n:
            primes.append(num)
        else:
            break

    # a calculates the highest power each prime can be raised to and still
    # be less than n. Then we raise it to that power and multiply it by the 
    # smallest number place holder for each prime on the list.
    for prime in primes:
        a = floor(log(n) / log(prime))
        smallest *= int(prime ** a)

    return smallest
