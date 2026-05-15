# creating a program where I take name as an input then I convert that into a list and arrange the alphabet in ascenting order


user_input = input("Enter The Name: ")

process = list(user_input)

"""process.sort()
print(process)"""


new_process = sorted(process)

print(new_process)

string = "".join(new_process)

print(string)
