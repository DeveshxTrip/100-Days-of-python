# sets

S1 = set()
S2 = {10}
S = {[1, 2], [3, 4]}

print(S)
print(type(S1))
print(type(S2))
n = 0
while n <= 4:
    name = input("Enter the names: ")
    S2.add(name)
    n += 1
print(S2)

S3 = {"Hello", (1, 2, 4)}
print(S3)

# print((1, 2, 4) in S3)
