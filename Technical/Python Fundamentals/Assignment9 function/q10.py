# 10. Replace every space with a hyphen (-).

def replace(s) :
  l = s.split(" ")
  return "-".join(l)

s = input("Enter string :")
print(f"Replace ' ' with '-' : {replace(s)}")
