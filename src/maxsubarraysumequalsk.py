def subarray_sum_equals_k(nums, k):
    count = 0
    curr_sum = 0
    sum_freq = {}
    print('before', sum_freq)
    sum_freq[0] = 1
    print('after', sum_freq)

    for num in nums:
        curr_sum = curr_sum + num
        if curr_sum - k in sum_freq:
            count = count + sum_freq[curr_sum - k]
        if curr_sum in sum_freq:
            sum_freq[curr_sum] = sum_freq[curr_sum] + 1
        else:
            sum_freq[curr_sum] = 1  # Initialize the count for new curr_sum

    return count

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, -2, 5]
    k = 5
    print(subarray_sum_equals_k(nums, k))  # Output: 3
