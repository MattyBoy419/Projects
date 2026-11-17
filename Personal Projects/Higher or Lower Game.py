import random

user_min = input("Welcome to the higher/lower game! \n Enter the lower bound: ")
user_max = input("Enter the upper bound: ")

upperBound = int(user_max)
lowerBound = int(user_min)
attempts = 0

if lowerBound < upperBound:
    guess = int(input(f"Great, now guess a number between {lowerBound} and {upperBound}!: "))
else:
    print("The lower bound must be less than the upper bound")

if guess > upperBound or guess < lowerBound:
    print("Please enter a number within the range")
    print(f"Guess a number between {lowerBound} and {upperBound}!: ", end = " ")
    int(input())
num = random.randrange(lowerBound, upperBound)

attempts = 0
while True:
    attempts += 1
    if guess < num:
        print("Your guess is too low")
        guess = int(input("Guess again: "))
    elif guess > num:
        print("Your guess is too high")
        guess = int(input("Guess again: "))
    if guess == num:
        print("Congratulations! You guessed the number!")
        break
