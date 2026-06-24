random_list = [1, 2, 1, 2, 3, 1, 3, 2, 4, 1, 5, 4, 5, 6]
my_list = []

for i in random_list:
    if i not in my_list:
        my_list.append(i)
    else:
        continue


print(my_list)
