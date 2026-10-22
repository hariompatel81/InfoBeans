# 23. Reverse the order of words in a sentence.
# Example: "Python is easy" → "easy is Python"

s = "Reverse the order of words in a sentence"
l = s.split(" ")
left = 0
right = len(l)-1
result = ""
while left < right:
  l[left],l[right] = l[right],l[left]
  left += 1
  right -= 1

# for w in l:
#   result = result + w + " "
result = " ".join(l)
  
print(result)