def hello():
    print("hello world")


hello()


def oddEven(num):
    if num % 2 == 0:
        print("Even")
        return "even"
    else:
        print("Odd")
        return "odd"


result = oddEven(4)
print(result)
