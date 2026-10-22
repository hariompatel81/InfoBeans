# 3. Count the number of vowels and consonants in a string.

s = "my name is hariom patel."
vc = 0
cc = 0
for i in range(len(s)) :
  if s[i] in {'a','e','i','o','u','A','E','I','O','U'} :
    vc += 1
  else :
    cc += 1

print(vc)
print(cc)
