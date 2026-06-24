random_list = []
my_list = []

for i in random_list:
    if i not in my_list:
        my_list.append(i)
    else:
        print("already in the list")
        continue


print(my_list)
