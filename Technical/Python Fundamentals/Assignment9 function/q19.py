# 19. Count the frequency of every character using a dictionary.
# Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def frequency_count(s):
  d = {}
  for ch in s:
    d[ch] = d.get(ch, 0)+1

  return d

s = input("Enter string:")
print(f"Frequency : {frequency_count(s)}")