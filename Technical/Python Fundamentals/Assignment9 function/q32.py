# 32. Find the longest palindromic substring.
# Example: "babad" → "bab" or "aba"

def longest_palindromic_substring(s):
  if not s:
    print("String is empty")
    return ""
  elif len(s) == 1:
    return s
  else :
    max = float('-inf')
    longest = None
    for i in range(len(s)-1):
      for j in range(i+1,len(s)):
        subs = s[i:j+1]       
        if subs == subs[::-1]:
          if len(subs) > max:
            max = len(subs)
            longest = subs
    return longest

s = input("Enter element :")
print(f"Longest palindromic substring is : {longest_palindromic_substring(s)}")