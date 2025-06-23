def group_anagrams(strs):
    anagram_map = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        print(s,sorted_s)
        anagram_map.setdefault(sorted_s, []).append(s)
    return list(anagram_map.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))