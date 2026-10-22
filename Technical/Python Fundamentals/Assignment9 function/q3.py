# 3. Count the number of vowels and consonants in a string.

def vcount(s):
  d = {'a','e','i','o','u','A','E','I','O','U'}
  count = 0
  for ch in s:
    if ch in d:
      count +=1
  return count

def ccount(s):
  count = 0
  d = {'a','e','i','o','u','A','E','I','O','U'}
  for ch in s:
    if (ord(ch)>=65 and ord(ch)<= 90) or (ord(ch) >= 97 and ord(ch)<=122) :
      if ch not in d:
        count += 1
  return count


s = input("Enter string :")
print(f"Vowel count is : {vcount(s)}")
print(f"Consonent count is : {ccount(s)}")


