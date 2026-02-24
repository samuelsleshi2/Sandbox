n = 20
i = 1
while (i <= n):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
        i += 1
    elif i % 3 == 0:
        print("Fizz")
        i += 1
    elif i % 5 == 0:
        print("Buzz")
        i += 1
    else:
        print(str(i))
        i += 1