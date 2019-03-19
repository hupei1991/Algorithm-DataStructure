def quick_select(unsorted_list, start, end, k):
    """
    quick select utilizing partition
    :param unsorted_list: the unsorted list
    :param start: start index
    :param end: end index
    :param k: the kth
    :return: the kth smallest number of the unsorted array
    """
    if start == end:
        return unsorted_list[start]
    left, right = start, end
    pivot = unsorted_list[left + ((right - left) >> 1)]
    while left <= right:
        while left <= right and unsorted_list[left] < pivot:
            left += 1
        while left <= right and unsorted_list[right] > pivot:
            right -= 1
        if left <= right:
            unsorted_list[left], unsorted_list[right] = unsorted_list[right], unsorted_list[left]
            left += 1
            right -= 1
    if right >= k and start <= right:
        return quick_select(unsorted_list, start, right, k)
    elif left <= k and left <= end:
        return quick_select(unsorted_list, left, end, k)
    return unsorted_list[k]


import random
def makeTestCase(n):
    """
    making test case of an array with length of n
    :param n: length of the test array
    :return: the array
    """
    return random.sample(range(random_minimum, random_maximum), n)

def makeTestCases(testcase_num, testcase_length):
    """
    making test cases
    :param testcase_num: number of test cases
    :param testcase_length: length of the testcase
    :return: a list of testcases of tuple containing testcase and a k
    """
    return [(makeTestCase(testcase_length), random.randint(0, testcase_length))for _ in range(testcase_num)]


def validate(testcase, ans):
    """
    validate answer
    :param testcase_index: the testcase including k
    :param ans:  ans from the algorithm
    :return:
    """
    t, k = testcase
    return sorted(t)[k] == ans

import time

testcases_num = 1000
testcase_length = 1000
random_maximum = 10000
random_minimum = 0
if __name__ == "__main__":
    testcases = makeTestCases(testcases_num, testcase_length)
    total_time = 0
    passed = True
    for testcase in testcases:
        start_time = time.time()
        ans = quick_select(testcase[0], 0, len(testcase[0]) - 1, testcase[1])
        total_time += time.time() - start_time
        if not validate(testcase, ans):
            passed = False
            break
    print("Passed " + str(len(testcases)) + " test cases (recursive)!" if passed else "Failed! (recursive)")
    print("Running Time: " + str(total_time) + " second")