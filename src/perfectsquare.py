def is_perfect_square(num):
    if num < 0:
        return False
    left, right = 0, num
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Example usage:
n = 16
print(is_perfect_square(n))  # Output: True

n = 14
print(is_perfect_square(n))  # Output: False
