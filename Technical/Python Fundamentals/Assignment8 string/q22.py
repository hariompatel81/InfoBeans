# 22. Find the second most frequent character.

s = "my name is hariom patel"
d = {}
max_freq = 0
sec_max_freq = 0
max_ch = None
sec_max_ch = None
for ch in s:
  d[ch] = d.get(ch, 0)+1

for ch, freq in d.items():
  if freq > max_freq :
    sec_max_freq = max_freq 
    sec_max_ch = max_ch

    max_ch = ch
    max_freq = freq
  elif sec_max_freq < freq and freq < max_freq:
    sec_max_freq = freq
    sec_max_ch = ch

print("dictionary :",d)
print("Most frequent",max_ch)
print("secound most frequent",sec_max_ch)

  
