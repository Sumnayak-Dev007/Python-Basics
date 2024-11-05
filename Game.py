import random

secret_Num=random.randint(1,100)
Guess_Num=int(input("Guess a number between 1 and 100 : "))
while secret_Num!=Guess_Num:
    if Guess_Num<secret_Num:
        print("Your Guess is Too Low")
    else:
        print("Your Guess is Too High")
    Guess_Num=int(input("Guess a number between 1 and 100 : "))
print("\nCongratulations! You guessed the number correctly :)")
