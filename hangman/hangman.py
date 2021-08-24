print("PLAYER 1")
guessing_word = input("Type a word you want to guess: ").lower()
print(guessing_word)

for i in range(0, 10):
    print("*" * 69)

lives = 4
print("PLAYER 2")
print(f"YOU START WITH {lives} lives")
print("For each missed guess you will lose 1 life.\n")

wrong_guesses = []
guessing_word_list = []
for char in guessing_word:
    guessing_word_list.append(char)
#print(guessing_word_list)
while True:
    print(f"YOU HAVE {lives} lives")
    current_char = input("Enter a char that you want to guess: ").lower()
    print(current_char)
    if current_char in guessing_word:
        guessing_word_list = [value for value in guessing_word_list if value != current_char]
        print(guessing_word_list)
    elif current_char not in guessing_word:
        lives -= 1
        if current_char in wrong_guesses:
            print("You have already made a wrong guess with this character!")
        elif current_char not in wrong_guesses:
            wrong_guesses.append(current_char)
        print("Wrong guesses:")
        print(wrong_guesses)
    if len(guessing_word_list) == 0:
        print("You WON!!!")
        break
    if lives == 0:
        print(f'YOU HAVE LOST THIS GAME\nWORD YOU SHOULD GUESS WAS "{guessing_word}"')
        break
