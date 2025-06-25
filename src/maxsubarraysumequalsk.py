def subarray_sum_equals_k(nums, k):
    from collections import defaultdict
    count = 0
    curr_sum = 0
    sum_freq = defaultdict(int)
    sum_freq[0] = 1

    for num in nums:
        curr_sum += num
        count += sum_freq[curr_sum - k]
        sum_freq[curr_sum] += 1

    return count

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, -2, 5]
    k = 5
    print(subarray_sum_equals_k(nums, k))  # Output: 3
