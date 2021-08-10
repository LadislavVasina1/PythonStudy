import random

answer = random.randint(1, 10)

print("Please guess a number between 1 an 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher.")
    else:
        print("Please guess lower.")
    guess = int(input())
    if guess == answer:
        print("Good job, you have guessed it.")
    else:
        print("Sorry, you have not guessed it correctly.")
else:
    print("You got it first time.")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("You have not guessed it correctly")
#         print(f"Correct answer is: {answer}")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("You have not guessed it correctly")
#         print(f"Correct answer is: {answer}")
# else:
#     print("You have guess the right number")


