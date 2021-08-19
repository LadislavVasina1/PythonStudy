low = 1
high = 1000

print(f"Please think of a number between '{low}' and '{high}'")
input("Press ENTER to start.")

steps = 1

while low != high:
    print(f"\tGuessing in the range of {low} to {high}.")
    guess = low + (high - low) // 2
    high_low = input(f"My guess is '{guess}'.\n Should I guess higher or lower?\n"
                     f"Enter h or l, or c if my guess was correct.\n").casefold()

    if high_low == 'h':
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == 'l':
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == 'c':
        print(f"I got it in {steps}")
        break
    else:
        print("Please enter h, l or c.")
    steps += 1
else:
    print(f"You thought of the number {low}")
    print(f"I got it in {steps}")
