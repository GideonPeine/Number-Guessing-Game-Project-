#controller runs the programs, and makes the functional system
import guess
import def_val
import player_names
def cont():
    #playerlist is Xnull to identify empty list
    playerlist=['Player']
    #mini and maxi determine range for random number
    mini=0
    maxi=1000
    lop='t'
    #all prints show design
    print("\t", "Number Guessing Game")
    print("----------------------------------------")
    print("")
    print("1. set players")
    print("2. set maximun and minimum for range")
    print("3. play game")
    print("")
    print("")
    #next determines input and activates corrisponding function
    while lop=='t':
        activ=int(input("Enter input: "))
        if activ==1:
            total=player_names.player_amount()
            playerlist=[]
            for count in range(total):
                name=player_names.player_names()
                playerlist.append(name)
        elif activ==2:
            minmax=def_val.def_val()
            mini=minmax[0]
            maxi=minmax[1]
        elif activ==3:
            playercount=0
            guess.guessnum(mini, maxi, playerlist, playercount)
        
        
    
    
    