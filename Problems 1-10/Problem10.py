from Problem7 import sieveOfEra

def sum_primes(n):
    """Retrun the sum of the prime numbers less than n."""
    total = 0
    for x in sieveOfEra():
        if x < n:
            total += x
        else:
            return total
