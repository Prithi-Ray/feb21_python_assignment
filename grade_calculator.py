# Grade calculator program

score = float(input("Enter your score: "))

grade_A = 90
grade_B = 80
grade_C = 70
grade_D = 60
grade_F = 50

if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    if score >= grade_A:
        grade = "A"
        message = "Excellent!"
    elif score >= grade_B:
        grade = "B"
        message = "Good job!"
    elif score >= grade_C:
        grade = "C"
        message = "You passed!"
    elif score >= grade_D:
        grade = "D"
        message = "You barely passed!"
    else:
        grade = "F"
        message = "You failed. Better luck next time!"

    print(f"Your grade is: {grade}")
    print(message)

if grade == "A":
    scholarship = "Eligible for Full Scholarship"
elif grade == "B":
    scholarship = "Eligible for Partial Scholarship"
else:
    scholarship = "No Scholarship Available"

print(f"Your scholarship status: {scholarship}")

if score >= 60:
    passing_message = "You passed the course!"
else:
    passing_message = "You did not pass the course."

print(passing_message)

if grade == "A" or grade == "B":
    feedback = "Keep up the good work!"
elif grade == "C":
    feedback = "Try to improve your performance next time."
else:
    feedback = "Study harder for better results!"

print(feedback)
