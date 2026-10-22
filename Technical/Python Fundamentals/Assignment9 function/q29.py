# 29. Remove a particular character from a string without using replace().

def remove_ch(s,ch):
  l = list(s)
  for ele in s:
    if ele == ch:
      l.remove(ele)

  return "".join(l)

s = input("Enter string :")
ch = input("Enter charecter :")
print(f"After removing {ch} from string : {remove_ch(s, ch)}")
