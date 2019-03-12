def quick_sort_recursive(unsorted_list):
    """
    quick sort unsorted list recursively
    :param unsorted_list: unsorted list
    :return: sorted list
    """
    if not unsorted_list:
        return []
    pivot_index = len(unsorted_list) - 1
    pivot_val = unsorted_list[pivot_index]
    i = 0
    j = len(unsorted_list) - 1
    while i < j:
        while unsorted_list[i] < pivot_val and i < j:
            i += 1
        while unsorted_list[j] >= pivot_val and i < j:
            j -= 1
        unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    if unsorted_list[i] >= pivot_val:
        unsorted_list[i], unsorted_list[pivot_index] = unsorted_list[pivot_index], unsorted_list[i]
    else:
        i += 1
    left = quick_sort_recursive(unsorted_list[0:i])
    right = quick_sort_recursive(unsorted_list[i + 1:])
    return left + [pivot_val] + right


import random
def makeTestCase(n):
    """
    making test case of an array with length of n
    :param n: length of the test array
    :return: the array
    """
    return random.sample(range(random_minimum, random_maximum), n)


def validate(sorted_list):
    """
    result validator
    :param sorted_list: list for validation
    :return: boolean value if valid or not
    """
    previous = float('-inf')
    for e in sorted_list:
        if e < previous:
            return False
        previous = e
    return True

import time

testcases_num = 1000
testcase_length = 1000
random_maximum = 10000
random_minimum = 0
if __name__ == "__main__":
    loop_count = testcases_num
    testcases = [makeTestCase(testcase_length) for _ in range(loop_count)]
    start_time = time.time()
    passed = True
    for testcase in testcases:
        sorted_list = quick_sort_recursive(testcase)
        if not validate(sorted_list):
            passed = False
            break
    print("Passed " + str(len(testcases)) + " test cases (recursive)!" if passed else "Failed! (recursive)")
    print("Running Time: " + str(time.time() - start_time) + " second")