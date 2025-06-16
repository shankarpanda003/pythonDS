# Minimum in a Sorted and Rotated Array
# Given a sorted array of distinct elements arr[] of size n that is rotated at some unknown point, the task is to find the minimum element in it.
#
# Examples:
#
# Input: arr[] = [5, 6, 1, 2, 3, 4]
# Output: 1
# Explanation: 1 is the minimum element present in the array.
#
# Input: arr[] = [3, 1, 2]
# Output: 1
# Explanation: 1 is the minimum element present in the array.
#
# Input: arr[] = [4, 2, 3]
# Output: 2
# Explanation: 2 is the only minimum element in the array.

def sortedrotatedarray(arr):
    low,high=0,len(arr)-1
    while low < high:
        mid=(low+high) //2
        print("mid",mid)
        if arr[mid] < arr[high]:
            high=mid
        else:
            low=mid+1
    return arr[low]

if __name__ == "__main__":
    arr=[12,13,14,9,10,11]
    print(sortedrotatedarray(arr))

#put this as table Graphical Table Example:
```markdown
| low | mid | high | arr[mid] | arr[high] | Action                                 |
|-----|-----|------|----------|-----------|----------------------------------------|
| 0   | 2   | 5    | 1        | 4         | arr[mid] < arr[high], move high to mid |
| 0   | 1   | 2    | 6        | 1         | arr[mid] > arr[high], move low to mid+1|
| 2   | 2   | 2    | 1        | 1         | low == high, found minimum             |
```