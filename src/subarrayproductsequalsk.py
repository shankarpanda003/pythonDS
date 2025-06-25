def subarray_product_equals_k(nums, k):
    if k == 0:  # Handle edge case where k is 0
        return 0

    count = 0
    product = 1
    start = 0

    for end in range(len(nums)):
        product = product * nums[end]

        while start <= end and product > k:
            product = product / nums[start]
            start += 1

        if product == k:
            count += 1

    return count

# Example usage
if __name__ == "__main__":
    nums = [10, 2, 2, 20, 10]
    k = 20
    print(subarray_product_equals_k(nums, k))  # Output: 3