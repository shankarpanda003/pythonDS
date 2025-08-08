def get_permutations(s):
    # Base case: if string length is 1, only one permutation
    if len(s) == 1:
        return [s]

    perms = []
    for i in range(len(s)):
        # Choose 1 character
        char = s[i]
        # Remaining string after removing the chosen character
        remaining = s[:i] + s[i+1:]
        print("remaining",remaining)
        # Recurse to get permutations of the remaining string
        for p in get_permutations(remaining):
            perms.append(char + p)
            print(perms)

    return perms

if __name__ == "__main__":
    s = "abc"
    result = get_permutations(s)
    print(result)
    print(f"Total permutations: {len(result)}")
