# 26. Find the longest word in a sentence.

s = "Find the longest word in a sentence1"

l = s.split(" ")
max = 0
word = None
for i in l:
  if i.isalpha():
    if len(i) > max:
      max = len(i)
      word = i

print(f"longest word in a string is '{word}' and its length is {max}.")
