# .#Admission to a professional course is subject to the following conditions:
#a) Marks in mathematics >=60
#b) Marks in physics >=50
#c) Marks in chemistry >=40
#d) Total in all three subjects >=200
#Or
#Total in mathematics and physics>=150
#Given the marks in three subjects, write a program to process the applications to list eligible candidates.

physics=float(input("enter the marks of physics"))
maths=float(input("enter the marks of maths"))
chemistry=float(input("enter the marks of chemistry"))
total=physics+maths+chemistry


if physics >=50 and maths>=60 and chemistry>=40 or total>=200 or (maths+chemistry)>=150:
    print("you are eligible")
else:
    print("you are not eligible")
