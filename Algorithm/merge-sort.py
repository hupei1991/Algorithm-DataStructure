def merge(first_list, second_list):
    """
    merge two sorted list
    :param first_list: the first list
    :param second_list: the second list
    :return: merged list
    """
    merged_list = []
    i = 0 # for first list
    j = 0 # for second list
    while i < len(first_list) and j < len(second_list):
        if first_list[i] < second_list[j]:
            merged_list.append(first_list[i])
            i += 1
        else:
            merged_list.append(second_list[j])
            j += 1
    if i == len(first_list) - 1:
        merged_list.extend(second_list[j:])
    elif j == len(second_list) - 1:
        merged_list.extend(first_list[i:])
    return merged_list


def merge_sort_recursive(unsorted_list):
    """
    The core function of merge sort in recursive way
    :param unsorted_list: unsorted original list
    :return: sorted list
    """
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = len(unsorted_list) >> 1
    first_list = merge_sort_recursive(unsorted_list[:mid])
    second_list = merge_sort_recursive(unsorted_list[mid:])
    return merge(first_list, second_list)


def merge_sort_interative(unsorted_list):
    """
    The core function of merge sort in iterative way
    :param unsorted_list: unsorted list
    :return: sorted list
    """
    pace = 1
    sorted_list = []
    while pace < len(unsorted_list):
        first_list_start = 0
        while first_list_start < len(unsorted_list):
            second_list_start = min(first_list_start + pace, len(sorted_list))
            second_list_end = min(first_list_start + (pace << 1), len(sorted_list))
            unsorted_list[first_list_start: second_list_start] = merge(unsorted_list[first_list_start: second_list_start], unsorted_list[second_list_start: second_list_end])
            first_list_start += (pace << 1)
        pace <<= 1
    return sorted_list

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
        sorted_list = merge_sort_recursive(testcase)
        if not validate(sorted_list):
            passed = False
            break
    print("Passed " + str(len(testcases)) + " test cases (recursive)!" if passed else "Failed! (recursive)")
    print("Running Time: " + str(time.time() - start_time) + " second")

    passed = True
    for testcase in testcases:
        sorted_list = merge_sort_interative(testcase)
        if not validate(sorted_list):
            passed = False
            break
    print("Passed " + str(len(testcases)) + " test cases (iterative)!" if passed else "Failed! (iterative)")
    print("Running Time: " + str(time.time() - start_time) + " second")
