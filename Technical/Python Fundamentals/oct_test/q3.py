'''
Q3. Lists — Second-Largest Distinct Element (5 Marks)

Given a list of integers, find the second-largest distinct element without using sort(), sorted(), or max().

numbers = [12, 45, 7, 45, 30, 22, 30]

Expected output: 30
'''

def find_sec_lar_dis(l):
  if len(l)<2:
    return "List must contain two elements."
  else :
    max = float('-inf')
    sec_max = float('-inf')
    for ele in l:
      if ele > max:
        sec_max = max
        max = ele
      elif ele > sec_max and ele < max :
        sec_max = ele

    return sec_max




l = [12,45,7,45,30,22,30]
print(f"Second-Largest Distinct Element Is : {find_sec_lar_dis(l)}")