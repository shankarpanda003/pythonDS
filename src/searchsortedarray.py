def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid  # Key found, return index
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # Key not found

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
key = 4
result = binary_search(arr, key)
print(f"Index of {key}:", result)
