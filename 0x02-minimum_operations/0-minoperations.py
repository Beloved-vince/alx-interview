#!/usr/bin/python3
"""
    Minimum operations coding challenge.
    Prototype: def minOperations(n)
    
    Example:
    n = 9
    H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
    Number of operations: 6
"""
def minOperations(n):
    """
         method that calculates the fewest number of operations needed
         to result in exactly n H characters in the file.
    """
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            done += clipboard
            ops_count += 1
    
    return ops_count