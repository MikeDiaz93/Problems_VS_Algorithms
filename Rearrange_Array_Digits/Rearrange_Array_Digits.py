def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list == None or input_list == []:
        return -1, -1

    if len(input_list) == 1:
        return input_list[0], 0

    input_list = mergeSort(input_list)
    input_list.reverse()

    num1 = ''
    num2 = ''

    for i in range(len(input_list)):
        if i % 2 == 0:
            num1 += str(input_list[i])
        else:
            num2 += str(input_list[i])

    return int(num1), int(num2)


def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L)
        # Sorting the second half
        mergeSort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# original test

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


# test 2

#expected output :  (9831,962)
test_function([[9,3,2,9,6,1,8], [9831,962]])

#expected output :  (98760,9871)
test_function([[9,9,8,8,7,7,6,1,0], [98760,9871]])

#expected output :  (20,20)
test_function([[0,0,2,2], [20,20]])

#expected output :  (-1, -1)
test_function([[], []])
