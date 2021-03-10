def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list == None:
        return None

    if input_list == []:
        return []

    aux1 = 0
    aux2 = 0
    middle = 1

    L = len(input_list) - 1

    while aux2 <= L:
        if input_list[aux2] < middle:
            swap(input_list, aux1, aux2)
            aux1 += 1
            aux2 += 1

        elif input_list[aux2] > middle:
            swap(input_list, aux2, L)
            L -= 1

        else:
            aux2 += 1

    return input_list


def swap(input_list, i, j):
    temp = input_list[i]
    input_list[i] = input_list[j]
    input_list[j] = temp


# original test
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# test 2
print(sort_012([0, 0, 2, 2, 2, 1, 1, 2, 0]))
#expected output: [0, 0, 0, 1, 1, 2, 2, 2, 2]
test_function([0, 0, 2, 2, 2, 1, 1, 2, 0])
print('---------------------------------')


print(sort_012([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]))
#expected output: [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
test_function([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2])
print('---------------------------------')


print(sort_012([2,2,2,2,2,2,2]))
#expected output: [2, 2, 2, 2, 2, 2, 2]
test_function([2, 2, 2, 2, 2, 2,])
print('---------------------------------')

print(sort_012([]))
#expected output: []
test_function([])
print('---------------------------------')