# 16. Check whether two strings are anagrams.
# Example: "listen" and "silent" → True

s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2) :
  print("anagram")
else :
  print("Not a anagram")