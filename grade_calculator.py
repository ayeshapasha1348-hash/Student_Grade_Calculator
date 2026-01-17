# grade_calculator.py
# Week 2: Student Grade Calculator
# Beginner Python Project
# Day-wise program combined in one file

# =========================
# Day 1: Understand Grading System
# Grading Logic:
# A: 90-100 → Excellent! Keep it up! 🌟
# B: 80-89  → Very Good! 👍
# C: 70-79  → Good! You can improve
# D: 60-69  → Fair! Work harder
# F: 0-59   → Failed! Don’t give up, try again
# =========================

# =========================
# Day 2: Create Input System
print("📚 Welcome to Student Grade Calculator 📚\n")

# Get student name
name = input("Enter student name: ")

# =========================
# Day 4: Add Validation & Loop (input marks safely)
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Invalid input! Marks must be between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 100.")

# =========================
# Day 3: Add Grading Logic (if-elif-else)
# =========================
# Day 5: Create Function for Reusability
def calculate_grade(marks):
    """
    Function to calculate grade and return grade with encouraging message
    """
    if 90 <= marks <= 100:
        return "A", "Excellent! Keep it up! 🌟"
    elif 80 <= marks < 90:
        return "B", "Very Good! 👍"
    elif 70 <= marks < 80:
        return "C", "Good! You can improve"
    elif 60 <= marks < 70:
        return "D", "Fair! Work harder"
    else:
        return "F", "Failed! Don’t give up, try again"

# Calculate grade using function
grade, message = calculate_grade(marks)

# =========================
# Day 5: Display Result (Final Program)
# =========================
print(f"\n📊 RESULT FOR {name.upper()}:")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")

# =========================
# End of Program
# =========================
