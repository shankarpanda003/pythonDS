def group_anagrams(words):
    groups = {}

    for word in words:
        key = ''.join(sorted(word))  # Sort the word to create a key
        print(word,key)
        if key not in groups:
            groups[key] = []
        groups[key].append(word)     # Add the word to the group

    return list(groups.values())

# Example usage
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
