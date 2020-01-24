from random import randint;

options=["rock","paper","scissor"]
computer=options[randint(0,2)]

u=False
while u==False:
    u=input("Rock, Paper, Scissor? ")
    if u==computer:
        print("Tie!")
        
        
    elif u=="rock":
        if computer == 'paper':
            print("Computer chose ",computer)
            print("You Lose!! Winner is Computer")
        else:
            print("Computer chose ",computer)
            print("You Win!!")
        
            
    
    elif u == "scissor":
        if computer=="rock":
            print("Computer chose ",computer)
            print("You Lose!! Winner is Computer!")
        else:
            print("Computer chose ",computer)
            print("You Win!!")
            
            
    elif u=="paper":
        if computer=='scissor':
            print("Computer chose ",computer)
            print("You Lose!! Winner is Computer")
        else:
            print("Computer chose ",computer)
            print("You Win!!")
            
    else:
        print("That's not a valid play. Check your spelling!")
        
    u=False
    computer=options[randint(0,2)]

        
            
    
        
    
   



