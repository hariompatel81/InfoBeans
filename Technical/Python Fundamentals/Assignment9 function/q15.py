# 15. Find the ASCII/Unicode value of each character using ord().

def find_ascii(s) :
  for ele in s:
    print(ord(ele))

s = input("Enter string :")
find_ascii(s)