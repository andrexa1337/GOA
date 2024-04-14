grade = int(input("Enter the grade obtained in the school test: "))

if grade == 10:
    print("Congratulations! The student performed exceptionally well. The teacher will praise the student with the parent.")
elif grade == 8 or grade == 9:
    print("Well done! The student performed above average. The teacher will give a small note to the parent.")
elif grade == 5:
    print("The student's performance is satisfactory. The teacher will give a note to the parent.")
elif grade < 5:
    print("Unfortunately, the student's performance is below expectations. The teacher will expel the student from the school.")
else:
    print("Invalid grade entered.")
