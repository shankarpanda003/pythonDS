# Given an array arr[] of size n, the task is to find the length of the Longest Increasing Subsequence (LIS) i.e., the longest possible subsequence
# in which the elements of the subsequence are sorted in increasing order.
#
# Examples:
#
# Input: arr[] = [3, 10, 2, 1, 20]
# Output: 3
# Explanation: The longest increasing subsequence is 3, 10, 20
#
# Input: arr[] = [30, 20, 10]
# Output:1
# Explanation: The longest increasing subsequences are [30], [20] and [10]
#
# Input: arr[] = [2, 2, 2]
# Output: 1
# Explanation:  We consider only strictly increasing.
#
# Input: arr[] = [10, 20, 35, 80]
# Output: 4
# Explanation: The whole array is sorted

def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom
    # -up manner
    for i in range(1, n):
        for prev in range(0, i):
            if arr[i] > arr[prev]:
                lis[i] = max(lis[i], lis[prev] + 1)
        print(lis)
    # Return the maximum of all LIS values
    return max(lis)

if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(lis(arr))