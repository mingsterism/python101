realNumber = 10
count = 0
print("The computer has selected a number from 1 to 100. Guess what is this number")
guess = int(input("Enter a guess: "))

while guess != realNumber:
    if guess > realNumber:
        print('You were too high')
    else:
        print("You were too low")
    guess = int(input("Guess Again: "))
else:
    print("Completed. You guessed right")
