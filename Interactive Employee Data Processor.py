name= []
age= []
salaries= []
for i in range(3):
    name.append(input("Enter employee name: "))
    age.append(int(input("Enter employee age: ")))
    salaries.append(float(input("Enter employee salary: ")))

total_ages= sum(age)
average_age= total_ages / len(age)
total_salaries= sum(salaries)
max_salary= max(salaries)
max_salary_index= salaries.index(max_salary)
max_salary_name= name[max_salary_index]

print("--- FINAL EMPLOYEE REPORT ---")
print(f"Average age of employees: {round(average_age, 2)} years.")
print(f"Total combined salaries: ${round(total_salaries, 2)}.")
print(f"Highest salary is ${round(max_salary, 2)}, earned by {max_salary_name}.")
print(name + age + salaries)

