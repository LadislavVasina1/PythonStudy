import random

answer = random.randint(1, 10)

print("Please guess a number between 1 an 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("You have not guessed it correctly")
        print(f"Correct answer is: {answer}")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("You have not guessed it correctly")
        print(f"Correct answer is: {answer}")
else:
    print("You have guess the right number")
