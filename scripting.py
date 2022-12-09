
names = input("enter name")
assignments = int(input("enter no of assignments missing"))
grades = int(input("enter the grades of the missing assignments"))
current_grade = grades - 20


# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {names},\n\nThis is a reminder that you have {assignments} assignments left to \
submit before you can graduate. You're current grade is {grade} and can increase \
to {grades} if you submit all assignments before the due date.\n\n"

print(message)

# write a for loop that iterates through each set of names, assignments, 
# and grades to print each student's message
