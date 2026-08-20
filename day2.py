# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)


# Function to classify grade
def classify_grade(average):
    if average >= 75:
        return "Distinction"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"


# Taking number of subjects
num_subjects = int(input("Enter number of subjects: "))

# Taking marks
marks = []

for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

# Calculate average
average = calculate_average(marks)

# Classify grade
grade = classify_grade(average)

# Display results
print("\nStudent Result")
print("Marks:", marks)
print("Average Marks:", round(average, 2))
print("Grade:", grade)
