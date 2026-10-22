# 11. Count how many times a particular character occurs.

def charecter_occurence_cs(s,ch) :
  d = {ch:0}
  for ele in s:
    if ele in d :
      d[ch] = d.get(ch)+1

  return d

def charecter_occurence_ci(s,ch):
  s = s.lower()
  ch = ch.lower()
  d = {ch:0}
  for ele in s:
    if ele in d:
      d[ch] = d.get(ch)+1

  return d
  
s = input("Enter string :")
ch = input("Enter charecter :")
print(f"Charecter occurence case sencitive: {charecter_occurence_cs(s,ch)}")
print(f"Charecter occurence case insencitive: {charecter_occurence_ci(s,ch)}")



