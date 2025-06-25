def subarray_sum_equals_k(nums, k):
    count=0
    sum_freq={}
    sum_freq[0]=1
    curr_sum=0
    for i in range(len(nums)):
        curr_sum=curr_sum+nums[i]
        if curr_sum-k in sum_freq:
            count=count+sum_freq[curr_sum-k]
        elif curr_sum in sum_freq:
            sum_freq[curr_sum]=sum_freq[curr_sum]+1
        else:
            sum_freq[curr_sum]=1
    return count

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, -2, 5]
    k = 5
    print(subarray_sum_equals_k(nums, k))  # Output: 3


