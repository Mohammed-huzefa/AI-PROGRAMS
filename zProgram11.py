import random

n=random.randint(1,10)

attempts=3

while attempts>0:
    try:
        g=int(input("Guess a number (1-10): "))

        if g<1 or g>10:
            print("Enter a number between 1 and 10")
            continue

        if g==n:
            print("You Win!")
            break

        elif g<n:
            print("Too Low!")

        else:
            print("Too High!")

        attempts-=1
        print("Attempts left:",attempts)

    except ValueError:
        print("Invalid input! Enter a number.")

if attempts==0 and g!=n:
    print("You Lose!")
    print("The number was",n)
