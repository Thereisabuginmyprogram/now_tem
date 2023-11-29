import random

try:
    number_generated = random.randint(1,9)
    
    while True:
        try:
            guess = int(input("Guess the number: "))
            if guess == number_generated:
                print("Well guessed")
                break
            else:
                print("Please try again")
                guess = int(input("Guess the number: "))
        except ValueError:
            print("Invalid input")

except KeyboardInterrupt:
    print("\nGame interrupted by player")