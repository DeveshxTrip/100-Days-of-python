# More about "strings" today

# we can use [] brackets to access any element in the string

Str = "Devesh"
print(Str[2])  # out put will be "v"

# we can find length of the string using the len() function

Str1 = "Hello world"
print(len(Str1))  # output will be "11"

# len() function counts the element and not the index.

# To check if a given element is in the string or not, we can use the membership operator ("in")

print("Hell" in Str1)  # output will be "True"

# The opposite of "in" operator is "not in"

print("ellh" not in Str1)  # . output will be true


# SLICING In Strings (V.IMP)

# we use slicing to get a specific part of characters in a string
"""syntax: str[start index: end index : steps]

generally we don't use steps in the syntax : str[start index: End index]"""

string = "hello Devesh"

print(string[6:12])  # output will be "Devesh"

# How to use steps in slicing

print(string[0:5:2])  # output will be "hlo"

# how to reverse a string using slicing

# [::-1]

print(string[::-1])

# Negative slicing

# if we want to slice from the end to the beginning we can use negative slicing

# “-1” represents last index element and -2 represents second last elements and so on

string = "Devesh"

print(string[-4:-1])  # output will be "ves"
