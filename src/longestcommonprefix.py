def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as a prefix
    prefix = strs[0]
    
    for s in strs[1:]:
        # Reduce the prefix until it matches the beginning of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

# Example usage:
words = ["flower", "flow", "flight"]
print(longest_common_prefix(words))  # Output: "fl"
