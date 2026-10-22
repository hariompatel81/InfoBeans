# 32. Find the longest palindromic substring.
# Example: "babad" → "bab" or "aba"

s = "babad"
if len(s) == 0 or len(s) == 1:
  print("String must have two charecter...")
else :
  max_len = 0
  longest_p = None
  for i in range(len(s)-1):
    for j in range(i,len(s)):
      pelindrom = s[i:j+1]

      l = list(pelindrom)
      left = 0
      right = len(l)-1
      while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
      temp = "".join(l)

      if pelindrom == temp:
        if max_len < len(pelindrom):
          max_len = len(pelindrom)
          longest_p = pelindrom

  print(max_len)
  print(longest_p)

