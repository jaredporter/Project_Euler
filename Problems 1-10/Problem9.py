from math import ceil, sqrt

def gcd(a, b):
    """Simple function to find the greatest common divisor when neither number is prime"""
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a

    while x % y != 0:
        y = x % y

    return y

def pythag_trip(n):
    """Find the product of the pythagorean triple which adds to n"""
    found = False
    for m in range(2, int((ceil(sqrt(n / 2)) + 1))):
        if (n / 2) % m == 0:    # found m
            k = m + 1           # make sure k is odd
        else:
            k = m + 2
        # k must satify the conditions below, and if it does, calculate a, b, c, d, and n
        # using the formulas after the if statement
        while k < (2 * m) and k <= (n /( 2 * m )):
            if (n / (2 * m)) % k == 0 and gcd(k, m) == 1:
                d = n / 2 / (k * m)
                n = k - m
                a = d * ((m ** 2) - (n ** 2))
                b = 2 * d * n * m
                c = d * (m ** 2 + n ** 2)
                found = True
                return a * b * c
                break
            k += 2
        # if the Pythagorean triple was found, stop the loop
        if found:
            break

pythag_trip(1000)
