# 21. Find the most frequent character in a string.

def most_fre_ch(s):
  d = {}
  max = 0
  mfc = None
  for ch in s:
    d[ch] = d.get(ch, 0)+1

  for key, value in d.items():
    if max < value :
      max = value
      mfc = key

  return mfc

s = input("Enter string:")
print(f"Most frequent charecter : {most_fre_ch(s)}")