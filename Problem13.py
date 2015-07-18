def large_sum(location):
    """Find the first 10 numbers of the sum of the numbers in location."""
    content = []

    # Load all of the numbers into content.
    with open(location) as f:
        for line in f.read().splitlines():
            content.append(int(line))

    # Sum the numbers and return the first 10 digits.
    s = str(sum(content))
    return s[0:10]
