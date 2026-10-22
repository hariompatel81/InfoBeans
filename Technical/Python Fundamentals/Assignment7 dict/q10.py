# 10. Merge two dictionaries. If a key exists in both dictionaries, use the value from the second dictionary.

d1 = {1:1,2:2,3:3}
d2 = {3:5,2:6,4:6}

print(d1)
print(d2)
for key in d2:
  d1[key]=d2[key]
print("After merging the two list the value of d1 and d2 is : ")
print(d1)
print(d2)


# print(d1|d2)
