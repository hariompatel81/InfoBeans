# 30. Find the longest common prefix among a list of strings.
# Example: ["flower", "flow", "flight"] → "fl"

l = ["flower","flow","flowht"]

if not l:
  print("list is empty.")
elif len(l) == 1:
  print(l[0])
else :
  flag = False
  var = l[0]
  prefix = []
  min = float('inf')
  for ele in l:
    if len(ele) < min:
      min = len(ele)
  for i in range(min) :
    for ele in l :
      if ele[i] != var[i] :
        flag = True
        break
    else :
      prefix.append(var[i])
    if flag:
      break

  result = "".join(prefix)
  print(result)

