# 20. Remove duplicate characters while preserving their original order.
# Example: "programming" → "progamin"

def remove_duplicate(s):
  d = {}
  for ch in s:
    d[ch] = d.get(ch, 0)+1

  l = d.keys()
  return "".join(l)

s = input("Enter string:")
print(f"After removing duplicates : {remove_duplicate(s)}")