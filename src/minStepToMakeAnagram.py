def min_steps_to_anagram(s1, s2):
    freq = [0] * 26  # for lowercase English letters

    for ch in s1:
        freq[ord(ch) - ord('a')] += 1

    for ch in s2:
        freq[ord(ch) - ord('a')] -= 1

    steps = sum(abs(x) for x in freq)
    return steps

# Example
s1 = "bcadeh"
s2 = "hea"
print("Minimum steps:", min_steps_to_anagram(s1, s2))
