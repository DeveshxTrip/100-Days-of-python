# dictionary

from sys import getrefcount

D1 = {"name": ["Devesh", "Sara", "Somya", "Ashita"], "Age": 22, "Country": "India"}

a = 6

# print(D1)
# print(D1.keys())
# print(D1.values())
# print(D1.items())

# for i in D1:
#     print(i)

for i in D1["name"]:
    if i == "Devesh":
        print(f"Madarchod {i}")
    else:
        print(f"Cutie {i}")
print(D1["name"])


for i in range(len(D1["name"])):
    if D1["name"][i] == "Devesh":
        D1["name"][i] = "Vedesh"
    else:
        continue
print(D1["name"])


D = {"a": 1, "b": 2}


D = {"a": 1, "b": 2}


print(getrefcount(a))
