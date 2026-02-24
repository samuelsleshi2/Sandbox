from time import sleep
import random

while True:
    sleep(1)
    print("Welcome to Rock Paper Scissors!")
    sleep(2)
    print("Rock...")
    sleep(1)
    print("Paper...")
    sleep(1)
    print("Scissors...")
    sleep(1)
    print("Shoot!")
    player = str(input("Choice: ")).strip().title()
    cpu_choices = ["Rock", "Paper", "Scissors"]
    cpu = random.choice(cpu_choices)
    if player == "Rock" and cpu == "Scissors" or player == "Paper" and cpu == "Rock" or player == "Scissors" and cpu == "Paper":
        sleep(0.5)
        congrats = input(f"My choice was {cpu}☹️. Congrats! You won! Do you want to play again?\n").strip().title()
        if congrats == "Yes":
            continue
        else:
            break
    elif player == cpu:
        tie = input(f"My choice was also {cpu}. It's a tie! Do you want to play again?\n")
        if tie == "Yes":
            continue
        else:
            break
    else:
        sleep(0.5)
        fail = input(f"My choice was {cpu}. Ha! You lost. Do you want to play again?\n")
        if fail == "Yes":
            continue
        else:
            break