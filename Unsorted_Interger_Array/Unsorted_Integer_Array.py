import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == None or len(ints) == 0:
        return None

    if len(ints) == 1:
        return (ints[0], ints[0])

    min_ = ints[0]
    max_ = ints[0]

    for i in range(1, len(ints)):
        if ints[i] > max_:
            max_ = ints[i]
        elif ints[i] < min_:
            min_ = ints[i]

    return (min_, max_)


# original test

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# test 2
# expected output: (1,2)
print("Pass" if ((1, 2) == get_min_max([2, 1])) else "Fail")

# expected output: (0,7)
print("Pass" if ((0, 7) == get_min_max([7, 6, 5, 4, 3, 2, 0])) else "Fail")

# expected output: (1,1)
print("Pass" if ((1, 1) == get_min_max([1, 1])) else "Fail")

# expected output: (0,0)
print("Pass" if ((0, 0) == get_min_max(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) else "Fail")

# expected output: (1000,5000)
print("Pass" if ((1000, 5000) == get_min_max(
    [1000, 3000, 2000, 5000, 4000])) else "Fail")
