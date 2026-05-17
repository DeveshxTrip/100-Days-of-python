# sets

S1 = set()
S2 = {10}
print(type(S1))
print(type(S2))
n = 0
while n <= 4:
    name = input("Enter the names: ")
    S2.add(name)
    n += 1
print(S2)
