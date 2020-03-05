'''
Problem:
Given five positive integers, find the minimum and maximum values that can be calculated by summing
exactly four of the five integers. Then print the respective minimum and maximum values as a single
line of two space-separated long integers.
For example, arr = [1, 3, 5, 7, 9]. Our minimum sum is 1+3+5+7=16 and our maximum sum is 3+5+7+9= 24.
We would print:
16 24

Output format:
Print two space-separated long integers denoting the respective minimum and
maximum values that can be calculated by summing exactly four of the five integers.
(The output can be greater than a 32 bit integer.)
'''


def miniMaxSum(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted) - 1
    print(sum(arr_sorted[:n]), sum(arr_sorted[-n:]))


if __name__ == '__main__':

    arr = [1, 3, 5, 7, 9]
    miniMaxSum(arr)