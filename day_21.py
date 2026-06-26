random_set = {2, 3, 4, 5, 6, 7, 8, 9, 10, 23}
new_set = set()

for i in random_set:
    if i & (i - 1) == 0:
        print(f"the num:{i} is power of 2")
    else:
        print("Not a power of 2")
