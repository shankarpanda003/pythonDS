def longest_unique_subarray(arr):
    seen = set()
    left = 0
    max_len = 0
    start_index = 0  # to track where the longest subarray starts

    for right in range(len(arr)):
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1
        seen.add(arr[right])

        # Update max length and starting index
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_index = left

    # Extract the subarray
    longest_subarr = arr[start_index : start_index + max_len]
    return max_len, longest_subarr


# Example usage
arr = [5, 1, 3, 5, 2, 3, 4, 1]
length, subarr = longest_unique_subarray(arr)
print("Length:", length)
print("Subarray:", subarr)
