# 25. Given a nested dictionary of students and their subject marks, calculate each student's total marks and find the topper.

students = {
  "Hariom" : {"maths":80, "physics":50, "chemistry":33},
  "sujal" : {"maths":70, "physics":52, "chemistry":43},
  "yogita" : {"maths":50, "physics":40, "chemistry":63}
}


topper = None
max = float('-inf')
for i in students.keys():
  marks = 0
  for j in students[i].keys() :
    marks += students[i][j] 
  if max < marks:
    max = marks
    topper = i
  
print("Topper : ",topper)
print("Topper Marks :",max)