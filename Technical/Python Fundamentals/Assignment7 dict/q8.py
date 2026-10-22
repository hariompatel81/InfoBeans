# 8. Calculate the sum of all numeric values in a dictionary.

d = {
  1:"one",
  2:"two",
  "three":3,
  2.5:"float"
}
sum = 0
for value in d.values() :
  if type(value) in [int, float] :
    sum += value

print(d)
print(sum)

