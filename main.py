student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"
#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
    score = student_scores[name]
    print(name)
    print(score)
    if score >= 90 and score < 100:
        student_grades[name] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        student_grades[name] = "Acceptable"
    elif score <= 70:
        student_grades[name] = "Fail"
    
    
    

# 🚨 Don't change the code below 👇
print(student_grades)





