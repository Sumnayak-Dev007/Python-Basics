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

'''Another Version'''
Py_Number=random.randint(10,50)

i=1
while i<=5:
    user = int(input("Guess the number in range 10..50 : "))
    if Py_Number==user:
        print("You Win ")
        break
    else:
        i+=1
if not i<=5:
    print("You lose :( \nThe number was",Py_Number)