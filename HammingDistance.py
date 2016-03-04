
# Code credit: Course's default

# Sample Input:
# GGGCCGTTGGT
# GGACCGTTGAC
# Sample Output:
# 3


def HammingDistance(s1, s2):
    # your code here
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1, s2))