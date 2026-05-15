Roll = int(input("enter how many students: "))
students = []
name = "Enter the name"
for i in range(1, Roll + 1):
    user_input = input(f"Enter Name {i}: ")

    students.append(user_input)

print(students)
