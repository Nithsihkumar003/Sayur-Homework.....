#calculate_salary(base_salary, final_bonus):

def calculate_salary(base_salary, final_bonus):
    salary_list = []
    
    for i in range(12):
        salary_list.append(base_salary)
        final_bonus += base_salary * 0.05 
        if final_bonus >= 100000:  
            base_salary += base_salary * 0.05 
            final_bonus = 0  
        
    return salary_list

current_month_salary = float(input("Enter your current month's salary: "))

final_bonus = 0

salary_for_each_month = calculate_salary(current_month_salary, final_bonus)

for month, salary in enumerate (salary_for_each_month , start=1):
    
    print(f"Month {month}: Salary = {salary:.2f}")