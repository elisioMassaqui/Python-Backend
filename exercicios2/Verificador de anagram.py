def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print(are_anagrams("listen", "silent"))
