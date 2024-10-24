# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

#solution

def grading_system():
     percentage_mark =int(input("Enter the student mark percentage mark: "))
     if  percentage_mark >= 90:
        print(f"Grade A")
     elif  percentage_mark >= 80:
         print(f"Grade B")
     elif percentage_mark >= 70:
         print(f"Grade C")
     elif percentage_mark >=60 :
         print(f"Grade D")
     elif percentage_mark >=50:
         print(f"Grade E")
     else :
         print("Grade F")
grading_system()