# 30. Find the longest common prefix among a list of strings.
# Example: ["flower", "flow", "flight"] → "fl"

def find_longest_prefix(l):
  if not l:
    return ""
  elif len(l) == 1:
    return l[0]
  else :
    l1 = []
    min = float('inf')
    for i in range(len(l)):
      if min > len(l[i]):
        min = len(l[i])

    for i in range(min):
      temp = l[0][i]
      for ele in l:
        if temp != ele[i]:
          return "".join(l1)

      l1.append(temp)
    return "".join(l1)

def flp(l):
  prifix = ""
  for i in range(len(l[0])):
    ch = l[0][i]
    count = 0
    for word in l:
      if i<len(word) and word[i] == ch:
        count += 1

    if count == len(l):
      prifix += ch
    else :
      return prifix

l = ["flower", "flow", "flight"]
print(f"Longest sub string : {find_longest_prefix(l)}")
print(f"Longest sub string : {flp(l)}")





      


