#Given an array arr[] of n integers and a target value,
# the task is to find whether there is a pair of elements in the array whose sum is equal to target
#nput: arr[] = [0, -1, 2, -3, 1], target = -2
#Output: true
#Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2.

#brute force
def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            print(arr[i], arr[j])
            if arr[i]+ arr[j] == target:
                return (True, (arr[i], arr[j]))

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target =  -2
    if len(arr) < 2:
        print("Array must contain at least two elements")
    else:
        print(two_sum(arr,target))

#Time Complexity: O(n²), for using two nested loops
#Space Complexity: O(1), no extra space is used except for the input array

#Optimized approach
def oprimised_two_sum(arr, target):
    prevMap= {}
    for i ,n in enumerate(arr):
        print(prevMap) #debugging line
        diff= target - n
        print(target,n, diff)
        if diff in prevMap:
            print("target found")
            return [prevMap[diff],i]
        else:
            prevMap[n]=i

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target =  -2
    if len(arr) < 2:
        print("Array must contain at least two elements")
    else:
        print("Optimized approach")
        print(oprimised_two_sum(arr,target))
#Time Complexity: O(n), for using a single loop
#Space Complexity: O(n), for using a hash map to store the elements and their indices


