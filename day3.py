import csv
from collections import Counter

# Read the CSV file
grades = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        grades.append(row["Grade"])

# Count frequency of each grade
grade_frequency = Counter(grades)

# Display the result
print("Grade Frequency:")
for grade, count in grade_frequency.items():
    print(f"{grade}: {count}")

# Write summary to a new file
with open("grade_summary.txt", "w") as file:
    file.write("Grade Frequency Summary\n")
    file.write("=======================\n")

    for grade, count in grade_frequency.items():
        file.write(f"{grade}: {count}\n")

print("\nSummary saved to grade_summary.txt")
