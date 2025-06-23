# Given an array arr[] of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times. The task is to find the repeating numbers.
#
# Note: The repeating element should be printed only once.
#
# Example:
#
# Input: n = 7, arr[] = [1, 2, 3, 6, 3, 6, 1]
# Output: 1, 3, 6
# Explanation: The numbers 1 , 3 and 6 appears more than once in the array.
#
# Input : n = 5, arr[] = [1, 2, 3, 4 ,3]
# Output: 3
# Explanation: The number 3 appears more than once in the array.

#still a oprimises approach using hashmap
def find_duplicates(arr):
    hashmap={}
    for i in range(len(arr)):
        if arr[i] in hashmap:
            hashmap[arr[i]]=hashmap[arr[i]] + 1
        else:
            hashmap[arr[i]]=1
    return hashmap

if __name__ == "__main__":
    arr= [1, 2, 3, 6, 3, 6, 1]
    hashmap=find_duplicates(arr)
    duplicates = [key for key, value in hashmap.items() if value > 1]
    print(duplicates)

# Time Complexity: O(n), for using a single loop
# Space Complexity: O(n), for using a hash map to store the elements and their counts

#optimsed approach using marking technique
# src/duplicate.py

def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        index = abs(arr[i])
        if index >= len(arr):
            continue  # skip out-of-range values
        if arr[index] >= 0:
            arr[index] = -arr[index]
        else:
            if index not in duplicates:
                duplicates.append(index)
    return duplicates

if __name__ == "__main__":
    arr = [1,2,3,2,4,1]
    # The marking technique only works correctly if all elements are in the range 0 to n-1 (here, n=5, so valid values are 0 to 4).
    print(find_duplicates(arr))  # Output: [1, 3, 6]
