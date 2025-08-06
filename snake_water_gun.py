import random
'''
1 for Snake 
-1 for water
0 for gun
'''
Computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict= {"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}

you=youDict[youstr]

#By now we have 2 numbers(variables) that is you and computer

print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[Computer]}")

if(Computer==you):
    print("It's a draw")
else:
    if(Computer==-1 and you==1):
        print("You Win!")
    elif(Computer==-1 and you==0):
        print("You Lose!")
    elif(Computer==1 and you==-1):
        print("You Lose!")
    elif(Computer==1 and you==0):
        print("You Win!")
    elif(Computer==0 and you==-1):
        print("You Win!")
    elif(Computer==0 and you==-1):
        print("You Lose!")

    else:
        print("Something Went Wrong")

