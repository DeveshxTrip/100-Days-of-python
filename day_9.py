# LIST


L = [[[1, 2], [3, [4, 10]], [5, 6], [7, 8]]]

print(L[0][1][1][1])


# questions on list

sample = "abc@gmail.com"

print(sample[: sample.find("@")])

L1 = [1, 2, 3, 5, 5, 1]
L2 = []

for i in L1:
    if i not in L2:
        L2.append(i)
print(L2)
