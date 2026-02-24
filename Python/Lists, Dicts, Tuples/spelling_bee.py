WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}

def main():
    print("Welcome to the Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        guess = input("Guess a word: ")
        if guess in WORDS.keys():
            print(f"Good job! You scored {WORDS[guess]} points")
            WORDS.pop(guess)
    
    print("That's the game!")

main()