# 34. Compress a string by counting consecutive repeated characters.
# Example: "aaabbccccd" → "a3b2c4d1"

def compress_string(s):
  if not s:
    return ""
  else :
    count = 1
    s1 = ""
    for i in range(len(s)-1):
      
      if s[i] == s[i+1]:
        count += 1
      else :
        s1 += s[i]+ str(count)
        count = 1
    s1 += s[i] + str(count)
    return s1

s = input("Enter a string: ")
print(f"Compress String : {compress_string(s)}")

  

  