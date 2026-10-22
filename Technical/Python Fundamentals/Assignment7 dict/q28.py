# 28. Create a new dictionary containing only entries whose values are greater
#     than or equal to a given threshold. Do not modify the dictionary while
#     iterating over it.

marks = {
  "maths":23,
  "che":43,
  "phy":56,
  "hindi":80,
  "english":67
}

d = {}
threshold = 70
for key,value in marks.items():
  if value >= threshold:
    d[key] = value

print(f"marks dictionary {marks}")
print("Threshold",threshold)
print("resulten dictionary",d)