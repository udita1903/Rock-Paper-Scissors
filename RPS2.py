import random
pw,cw=0,0 
options=[1,2,3]
flag=1
while flag:
    print("Options:")
    print("1.ROCK")
    print("2.PAPER")
    print("3.SCISSORS")
    print("4.To End")
    try:
        x=int(input("Enter your choice number i.e 1,2,3,4 : "))
    except:
        print("Invalid input")
    
    y=random.randint(1,3)
    if x==1 or x==2 or x==3:
        if y==x:
            print("--------------------------")
            print("It's a tie")
            print("--------------------------")
        elif (x==1 and y==2) or (x==2 and y==3) or (x==3 and y==1):
            print("--------------------------")
            print("       You Win! ")
            print("--------------------------")
            pw+=1
        else:
            print("--------------------------") 
            print("       You Lose:") 
            print("--------------------------")
            cw+=1   
    elif x==4:
        flag=0      
        print("_________________________________________________________")
        print("          Number of times the player wins: ", pw)  
        print("          Number of times the computer wins: ", cw)  
        print("_________________________________________________________")
    else:
        print("INVALID INPUT ")    
