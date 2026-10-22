# 26. Find the longest word in a sentence.

def find_lword(s):
  l = s.split(" ")
  max = 0
  longest_word = None
  for word in l:
    if len(word) > max:
      max = len(word)
      longest_word = word

  return longest_word

s = input("Enter string :")
print(f"longest word is : {find_lword(s)}")

