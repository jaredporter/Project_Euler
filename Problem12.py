from Problem7 import sieveOfEra

def prime_factorial(number, lst):
    """Find the number of prime divisors of a number using a list of primes."""
    num_prime_divisors = 1
    remainder = number

    for i in lst:
        if i ** 2 > number:
            return num_prime_divisors * 2

        exponential = 1
        while remainder % i == 0:
            exponential += 1
            remainder = remainder / i
        num_prime_divisors *= exponential

        if remainder == 1:
            return num_prime_divisors

def primes_list():
    """Generator for a list of first 1500 prime numbers"""
    it = sieveOfEra
    cnt = 0
    for x in it:
        if cnt < 1500:
            cnt += 1
            yield x
        else:
            break

def tri_num_factor(n):
    """Find the first triangle number with n divisors."""
    k = 2
    DN = 2
    DN1 = 2
    count = 0

    while count < 500:
        if k % 2 == 0:
            DN = prime_factorial(k + 1, primes_list())
        else:
            DN1 = prime_factorial((k + 1) / 2, primes_list())
        count = DN * DN1
        k += 1

    return(k * (k - 1) / 2)
