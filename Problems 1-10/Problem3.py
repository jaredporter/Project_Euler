def largest_prime_fac(n):
    """Calculate the largest prime factor of n"""
    divisor = 2
    # Start with lowest prime and work through prime factors until highest is left 
    while divisor ** 2 < n:
        while n % divisor == 0:
            n = n / divisor
        divisor += 1
    return n
