# 23. Reverse the order of words in a sentence.
# Example: "Python is easy" → "easy is Python"
def reverse_word(s):
  l = s.split(" ")
  left = 0
  right = len(l)-1
  while left < right:
    l[left], l[right] = l[right], l[left]
    left += 1
    right -= 1

  return " ".join(l)

s = input("Enter string :")
print(f"After reverse word order : {reverse_word(s)}")