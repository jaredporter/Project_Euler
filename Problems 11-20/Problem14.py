def collatz(n):
    """Find the starting number less than n which produces the largest chain."""
    # Create a tempory memory to store sequence lengths and initialize the 
    # starting location and longest sequence.
    mem = {1:0}
    best_start = 0
    longest_seq = 0
    
    # Loop through all the numbers from 2 to n. Generate the Collatz chain and
    # see if it is longer than the longest chain. If so, set as new longest and
    # either way store value in memory.
    for i in range(2,n):
        count = 0
        num = i
        
        while num != 1 and num >= i:
            if num % 2 == 0:
                num = num / 2
            else:
                num = (3 * num) + 1
            count += 1
        
        mem[i] = count + mem[num]
        
        if mem[i] > longest_seq:
            longest_seq = mem[i]
            best_start = i
    
    return best_start, longest_seq
