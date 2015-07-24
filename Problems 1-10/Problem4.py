def max_palindrome(min=100,max=999):
    """Find the largest product of two numbers between 100 and 1000, which is a palindrome"""
    max_palindrome = 0
    a = 999
    stopper = 99
    # Loop through for as long as the values are above the min, starting at the max. 
    # For the inner while loop, find the product and see if it's a palindrome. 
    # Stop after first one as it will be the one with the highest value.
    while a > stopper:
        b = 999
        while b >= stopper:
            product = a * b
            if product > max_palindrome and str(product)==(str(product)[::-1]):
                max_palindrome = product
                fac1 = a
                fac2 = b
                stopper = b
                break
            b -= 1
        a -= 1
    return max_palindrome
