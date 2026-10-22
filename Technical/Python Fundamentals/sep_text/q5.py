'''

Q5. Student Result Menu — match-case + loops + if-else

Write a menu-driven Python program for managing the result of N students.

The program should repeatedly display:

1. Enter student marks
2. Display average marks
3. Display highest marks
4. Display lowest marks
5. Display result
6. Exit

Use match-case for menu selection.

For each student, marks are entered for:

Python
Database
Programming

A student passes only if:

Marks in each subject >= 40
Overall percentage >= 50

For the Display Result option, print:

Student 1: Pass
Student 2: Fail
Student 3: Pass

The menu should continue until the user selects 6. Exit.

Concepts being tested
Question	Main Concepts
Q1	if-elif-else, arithmetic
Q2	match-case, operators
Q3	while, if-else, digit manipulation
Q4	for, nested loop, if
Q5	match-case, loops, if-else, lists
'''

while True :
  print("1. Enter student marks")
  print("2. Average marks")
  print("3. Highest marks")
  print("4. Lowest marks")
  print("5. Result")
  print("6. Exit")

  sel = int(input("Select any option :"))

  match sel :
    case 1 :
      python = int(input("Enter python marks"))
      database = int(input("Enter database marks"))
      programming = int(input("Enter programming marks"))

    case 2 :

    case 3 :

    case 4 :  

    case 5 :

    case 6 :

