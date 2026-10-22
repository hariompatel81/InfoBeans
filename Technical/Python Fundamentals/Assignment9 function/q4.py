# 4. Count uppercase letters, lowercase letters, digits, and special characters.

def ucount(s):
  count = 0
  for ele in s:
    if ord(ele)>=65 and ord(ele)<=90 :
      count += 1
  return count

def lcount(s):
  count = 0
  for ele in s:
    if ord(ele)>=97 and ord(ele)<=122 :
      count += 1
  return count

def dcount(s) :
  count = 0
  for ele in s :
    if ord(ele)>= 47 and ord(ele) <= 56 :
      count += 1
  return count

def sccount(s) :
  count = 0
  for ele in s :
    if not (ord(ele)>=65 and ord(ele)<=90 or ord(ele)>=97 and ord(ele)<=122 or ord(ele)>=47 and ord(ele)<=56) :
      count += 1
  return count

s = input("Enter string :")
print(f"Uppercase count : {ucount(s)}")
print(f"Lowercase count : {lcount(s)}")
print(f"Digit count : {dcount(s)}")
print(f"Spacial charecter count : {sccount(s)}")
