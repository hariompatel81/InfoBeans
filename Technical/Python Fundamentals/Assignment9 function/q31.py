# 31. Find the longest substring without repeating characters.
# Example: "abcabcdbb" → 3 ("abc")

def find_longest_substring(s):
  bucket = set()
  left = 0
  right = 0
  max = 0
  substring = None
  for ele in s:
    if ele not in bucket:
      bucket.add(ele)
      right += 1
    else :
      if len(s[left:right]) > max:
        max = len(s[left:right])
        substring = s[left:right] 
      while left < right and ele in bucket:
        bucket.discard(s[left])
        left += 1

      bucket.add(ele)
      right += 1

  return substring

s = input("Enter string :")
print(f"longest substring : {find_longest_substring(s)}")

# l = ["1","2","3","4"]
# s = " + ".join(l)
# print(s)
