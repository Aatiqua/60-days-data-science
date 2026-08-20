# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))

# Calculating yearly salary
yearly_salary = salary * 12

# Storing data in a dictionary
employee = {
    "name": name,
    "age": age,
    "monthly_salary": salary,
    "yearly_salary": yearly_salary
}

# Displaying the data
print("\nEmployee Details:")
print(employee)
