import random
'''
1=Snake
0=Gun
-1=Water
'''
def Play_Game(Com_Choice,Your_choice):
    if Com_Choice==Your_choice:
        print("It was a Draw ")
    else:
        if Com_Choice==1 and Your_choice==0:
            print("You Win ")
        elif Com_Choice==1 and Your_choice==-1:
            print("You Lose ")
        elif Com_Choice==-1 and Your_choice==0:
            print("You Lose ")
        elif Com_Choice==-1 and Your_choice==1:
            print("You Win ")
        elif Com_Choice==0 and Your_choice==1:
            print("You Lose ")
        elif Com_Choice==0 and Your_choice==-1:
            print("You Win")
        else:
            print("404")


Com_Choice=random.choice([-1,0,1])
You=input("Enter your Choice (S/W/G) : ")
Your_Dict={"s":1,"g":0,"w":-1,"S":1,"G":0,"W":-1}
Your_choice=Your_Dict[You]

reverse_Dict={0:"Gun",1:"Snake",-1:"Water"}
print(f'Comp_Choice : {reverse_Dict[Com_Choice]}\nYour_Choice : {reverse_Dict[Your_choice]}')

Play_Game(Com_Choice,Your_choice)


