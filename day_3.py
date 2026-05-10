word = input("Enter The Word: ")
temp = ""
for i in word:
    if i.isalpha():
        temp += i
    else:
        continue

print(temp)
