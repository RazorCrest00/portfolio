# CODE_RUNNER: 3.17 Popcorn - Search growth
import math

def search_counts(n):
    if type(n) is not int or n < 0:
        raise ValueError("Book count must be a nonnegative whole number")
    binary = 0 if n == 0 else math.floor(math.log2(n)) + 1
    return n, binary

for n in [8, 16, 1000]:
    linear, binary = search_counts(n)
    print("Books:", n)
    print("Linear worst-case checks:", linear)
    print("Binary worst-case checks:", binary)
