# 19. Count the frequency of every character using a dictionary.
# Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}

s = "hello"
d = {}

for ch in s :
  d[ch] = d.get(ch, 0) +1

print(d)
