# Merge Overlapping Intervals
# Last Updated : 26 Mar, 2025
# Given an array of time intervals where arr[i] = [starti, endi], the task is to merge all the overlapping intervals into one and output the result which should have only mutually exclusive intervals.
#
# Examples:
#
# Input: arr[] = [[1, 3], [2, 4], [6, 8], [9, 10]]
# Output: [[1, 4], [6, 8], [9, 10]]
# Explanation: In the given intervals, we have only two overlapping intervals [1, 3] and [2, 4]. Therefore, we will merge these two and return [[1, 4]], [6, 8], [9, 10]].
#
# Input: arr[] = [[7, 8], [1, 5], [2, 4], [4, 6]]
# Output: [[1, 6], [7, 8]]
# Explanation: We will merge the overlapping intervals [[1, 5], [2, 4], [4, 6]] into a single interval [1, 6].

def mergeinterval(arr):
    arr=sorted(arr)
    i=0
    res=[]
    res.append(arr[0])
    n=len(arr)
    for i in range(1,n):
        curr=arr[i]
        if res[-1][1] >= curr [0]:
            res[-1][1] = max(curr[1],res[-1][1])
        else:
            res.append(curr)
    return res


if __name__ == "__main__":
    arr=[[1, 3], [2, 4], [6, 8], [9, 10]]
    print(mergeinterval(arr))