# 16. Check whether two strings are anagrams.
# Example: "listen" and "silent" → True

def check_anagram(s1,s2):
  if len(s1) == len(s2):
    l1 = sorted(s1)
    l2 = sorted(s2)

    if l1 == l2:
      return True
    else :
      return False
  else :
    return False

s1 = input("Enter s1:")
s2 = input("Enter s2:")
print(f"Check anagram : {check_anagram(s1,s2)}")