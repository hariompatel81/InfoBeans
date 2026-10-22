# 22. Find the second most frequent character.

def secmfc(s):
  d = {}
  for ch in s:
    d[ch] = d.get(ch, 0)+1

  print(d)

  max_freq = 0
  sec_max_freq = 0
  max_ch = None
  sec_max_ch = None
  for ch,freq in d.items():
    if freq > max_freq :
      sec_max_freq = max_freq
      sec_max_ch = max_ch

      max_freq = freq
      max_ch = ch
    elif freq > sec_max_freq and freq < max_freq:
      sec_max_freq = freq
      sec_max_ch = ch

  return sec_max_ch

s = input("Enter string :")
print(f"Secound max frequent charecter is : {secmfc(s)}")
       


