# 4. Count uppercase letters, lowercase letters, digits, and special characters.

s = "My name is Hariom Patel. and my email is hariompatel81204@gmail.com"

uc = 0
lc = 0
dc = 0
sc = 0

for i in s:
  if ord(i) >= 65 and ord(i) <= 90 :
    uc += 1
  elif ord(i) >= 97 and ord(i) <= 122 :
    lc += 1
  elif ord(i) >= 48 and ord(i) <= 57 :
    dc += 1
  else :
    sc += 1

print(uc)
print(lc)
print(dc)
print(sc)

