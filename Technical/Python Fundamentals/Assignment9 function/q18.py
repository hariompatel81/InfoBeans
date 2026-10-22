# 18. Find the first repeating character.
# Example: "programming" → r

def frepch(s):
  d = {}
  for ch in s:
    d[ch] = d.get(ch, 0)+1
    if d[ch] > 1:
      return ch
  else :
    return None

s = input("Enter string:")
print(f"First repeating element is : {frepch(s)}")

  

