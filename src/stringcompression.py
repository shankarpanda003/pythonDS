def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))  # append last set

    result = ''.join(compressed)
    # Optional: return the original string if compression does not reduce size
    return result if len(result) < len(s) else s

# Example usage:
s = "aabcccccaaa"
print(compress_string(s))  # Output: a2b1c5a3
