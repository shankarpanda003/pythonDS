# Insert and Merge Interval
# Last Updated : 26 Mar, 2025
# Given a set of non-overlapping intervals and a new interval, the task is to insert the interval at the correct position such that after insertion, the intervals remain sorted. If the insertion results in overlapping intervals, then merge the overlapping intervals. Assume that the set of non-overlapping intervals is sorted based on start time.
#
# Examples:
#
# Input: intervals[][] = [[1, 3], [4, 5], [6, 7], [8, 10]], newInterval[] = [5, 6]
# Output: [[1, 3], [4, 7], [8, 10]]
# Explanation: The intervals [4, 5] and [6, 7] are overlapping with [5, 6]. So, they are merged into one interval [4, 7].
#
# Input: intervals[][] = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval[]  = [4, 9]
# Output: [[1, 2], [3, 10], [12, 16]]
# Explanation: The intervals [ [3, 5], [6, 7], [8, 10] ] are overlapping with [4, 9]. So, they are merged into one interval [3, 10].

#bruteforce
#1. if end of interval < start of interval which means non over lapping portion
#2. If start of array < end of interval then merge
#3. append rest portion

def insertinterval(arr, newinterval):

    res=[]
    n=len(arr)
    i=0
    while i < n and arr[i][1] < newinterval[0] :
        res.append(arr[i])
        i=i+1

    while i < n and arr[i][0] <= newinterval[1]:
        newinterval[0]=(min(arr[i][0],newinterval[0]))
        newinterval[1]=(max(arr[i][1],newinterval[1]))
        i=i+1

    res.append(newinterval)

    while i < n:
        res.append(arr[i])
        i=i+1
    return res
if __name__ == "__main__":
    arr=[[1, 3], [4, 5], [6, 7], [8, 10]]
    newinterval=[2, 3]
    print(insertinterval(arr,newinterval))


