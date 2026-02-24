name = input("What's your name? ").strip()
age = int(input("How old are you? ").strip())
number = int(input("Give me a number: ").strip())

year = 2026
for i in range(number):
    print(f"You will turn 100 in the year {year + (100 - age)}")