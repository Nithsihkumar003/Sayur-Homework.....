
num_subjects = int(input("Enter the number of subjects: "))


total_marks = 0
pass_count = 0


for i in range(1, num_subjects + 1):
    subject_name = input(f"Enter the marks for Subject {i}: ")
    marks = float(subject_name)
    total_marks += marks
    
   
    if marks >= 45:
        print(f"Subject {i}: Pass")
        pass_count += 1
    else:
        print(f"Subject {i}: Fail")


average = total_marks / num_subjects


print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average:.2f}")
print(f"Overall Result: {'Pass' if pass_count == num_subjects else 'Fail'}")