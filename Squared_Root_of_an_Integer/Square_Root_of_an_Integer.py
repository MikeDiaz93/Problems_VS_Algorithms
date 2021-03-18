
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == None:
        return None

    if number < 0:
        print('Error, cant squared a negative number')
        return -1

    min_ = 1
    max_ = number

    old = min_
    new = max_

    while old != new:
        old = new
        squared = old**2

        if squared < number:
            min_ = old
        elif squared > number:
            max_ = old

        new = int((min_ + max_) / 2)

    return new


# original test
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# test 2


#expected output: 1
print ("Pass" if  (1 == sqrt(1)) else "Fail")

#expected output: 6
print ("Pass" if  (6 == sqrt(36)) else "Fail")

#expected output: 11
print ("Pass" if  (11 == sqrt(125)) else "Fail")

#expected output: 25
print ("Pass" if  (25 == sqrt(626)) else "Fail")



# test 3
# expected output: None
print("Pass" if (sqrt(None) is None) else "Fail")

# expected output = 99999
print("Pass" if (99999 == sqrt(9999999999)) else "Fail")
