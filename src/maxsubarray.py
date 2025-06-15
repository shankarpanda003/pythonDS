# Maximum Subarray Sum - Kadane's Algorithm
# Given an array arr[], the task is to find the subarray that has the maximum sum and return its sum.
#
# Examples:
#
# Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
# Output: 11
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
#
# Input: arr[] = {-2, -4}
# Output: -2
# Explanation: The subarray {-2} has the largest sum -2.
#
# Input: arr[] = {5, 4, 1, 7, 8}
# Output: 25
# Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.

#Brute force
def max_subarray_sum(arr):
    max_sum=arr[0]
    for i in range(len(arr)):
        sum_so_far=0
        for j in range(i,len(arr)):
            if i!=j:
                sum_so_far=sum_so_far+arr[j]
                if sum_so_far > max_sum:
                    max_sum=sum_so_far
    return max_sum

if __name__=="__main__":
    arr=[2, 3, -8, 7, -1, 2, 3]
    print(max_subarray_sum(arr))
# #Time Complexity: O(n²), for using two nested loops
# #Space Complexity: O(1), no extra space is used except for the input array

#Optimized approach - Kadane's Algorithm
def kadane_algorithm(arr):
    current_sum=0
    max_sum=0
    for i in range(len(arr)):
        current_sum=current_sum+arr[i]
        max_sum= max(max_sum,current_sum)
        if current_sum<0:
            current_sum=0
    return max_sum
if __name__=="__main__":
    arr=[-2, -3, -8, -7, -1, -2, -3]
    if max(arr)<0:
        print(max(arr))
    else:
        print(max_subarray_sum(arr))
