# 31. Find the longest substring without repeating characters.
# Example: "abcabcbb" → 3 ("abc")

s = "abcabcbb"

if not s:
  print("String is empty.")
elif len(s) == 1:
  print(f"longest substring without repeating characters is -->{s}")
else :
  left = 0
  buket = set()
  max_length = 0
  longest_subsequence = ""
  for right in range(len(s)):
    ch = s[right]
    if ch in buket :
      while ch in buket :
        buket.remove(s[left])
        left += 1

    buket.add(ch)
    if max_length < (right - left + 1):
      max_length = (right-left + 1)
      longest_subsequence = s[left:right+1]

  print(max_length)
  print(longest_subsequence)
