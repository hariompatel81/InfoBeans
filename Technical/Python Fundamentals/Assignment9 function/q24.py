# 24. Reverse every word without changing the word order.
# Example: "Python is easy" → "nohtyP si ysae"

def reverce_ch(s):
  l = s.split(" ")
  result = []
  for word in l:
    l1 = list(word)
    left = 0
    right = len(l1)-1
    while left < right :
      l1[left], l1[right] = l1[right], l1[left]
      left += 1
      right -= 1
    result.append("".join(l1))

  return " ".join(result)

s = input("Enter string :")
print(f"After reversing charecter : {reverce_ch(s)}")
    