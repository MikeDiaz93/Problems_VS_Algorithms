
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if number == None or input_list == None or input_list == []:
        return -1

    index = find_pivot(input_list)

    find = binary_search(input_list[:index], number)

    if find != -1:
        return find

    find = binary_search(input_list[index:], number)

    if find != -1:
        return find + index

    return -1


def binary_search(input_list, number):

    start = 0
    end = len(input_list)
    while start < end:
        mid = start + end >> 1
        s = input_list[mid]
        if s < number:
            start = mid + 1
        elif s > number:
            end = mid
        else:
            return mid
    return -1


def find_pivot(input_list):

    start = 0
    end = len(input_list) - 1

    while start <= end:
        mid = int((start + end) / 2)
        if input_list[start] <= input_list[end]:
            return start
        elif input_list[start] <= input_list[mid]:
            start = mid + 1
        else:
            end = mid

    return start


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# original test
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# test 2

# expected output : 0
rotated_array_search([6, 7, 8, 1, 2, 3, 4], 6)

# expected output: -1
rotated_array_search([6, 7, 8, 9, 10, 1, 2], 3)

# expected output: 4
rotated_array_search([8, 9, 10, 1, 2, 3, 4, 5, 6], 2)

# expecte output: 2
rotated_array_search([5,3,4,], 4)

# expected output: -1
rotated_array_search([5,3,4,], -3)
