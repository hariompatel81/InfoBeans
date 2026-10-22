# 32. Find the longest palindromic substring.
# Example: "babad" → "bab" or "aba"

def longest_palindromic_substring(s):
  if len(s) == 0 and len(s) == 1:
    print("Invalid string")
    return None
  else :
    max = float('-inf')
    longest = None
    for i in range(len(s)-1):
      for j in range(i+1,len(s)):
        subs = s[i:j+1]
        print(subs)
        if subs == subs[::-1]:
          if len(subs) > max:
            max = len(subs)
            longest = subs
    return longest

s = input("Enter element :")
print(f"Longest palindromic substring is : {longest_palindromic_substring(s)}")