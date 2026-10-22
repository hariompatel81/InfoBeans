# 17. Find the first non-repeating character in a string.
# Example: "aabbcddee" → c

def fnon_rep_ch(s):
  d = {}
  for ch in s:
    d[ch] = d.get(ch,0)+1

  for key, value in d.items():
    if value == 1:
      return key
  else :
    return None

s = input("Enter string : ")
print(f"First non-repeating charecter is :{fnon_rep_ch(s)}")
  