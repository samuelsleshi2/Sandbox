a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Give me a number: ").strip())
b = []
for i in a:
    if i < number: 
        b.append(i)
        print(i)