# Search in a Sorted and Rotated Array
# Given a sorted and rotated array arr[] of n distinct elements,
# the task is to find the index of given key in the array. If the key is not present in the array, return -1.
#
# Examples:
#
# Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
# Output: 8
# Explanation: 3 is present at index 8 in arr[].
#
# Input: arr[] = [3, 5, 1, 2], key = 6
# Output: -1
# Explanation: 6 is not present in arr[].
#
# Input: arr[] = [33, 42, 72, 99], key = 42
# Output: 1
# Explanation: 42 is found at index 1.

# src/searchrotatedsortedarray.py

def search_in_rotated_sorted_array(arr, key):
    low,high=0,len(arr)-1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == key:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low]<=key<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<key<=arr[low]:
                low=mid+1
            else:
                high=mid-1
    return -1

if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    print(search_in_rotated_sorted_array(arr, key))  # Output: 8
