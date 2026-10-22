# 21. Find the most frequent character in a string.

s = "my name is hariom patel"
d = {}
max = 0
max_ch = ""
for ch in s:
  d[ch] = d.get(ch, 0)+1
  if d[ch] > max and ch != " ":
    max = d[ch]
    max_ch = ch

print(d)
print(f"Most frequent charecter is {max_ch} and its frequency is {max}")

