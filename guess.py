import random as ran
import controller
#operation guessnum gets random number and asks for guess
def guessnum(mini, maxi, playerlist, playercount):
    #print maxi and mini
    print("The minium is", mini)
    print("The maximum is",maxi)
    val=ran.randint(mini, maxi)
    if playerlist==['Player ']:
        playerlist==["Player"]
    run='t'
    count=0
    #runs the guessing game
    while run=='t':
        count+=1
        if playercount>=len(playerlist):
            playercount=0
        print('')
        print((playerlist[playercount]), " ", end='')
        guess=int(input( "What is your guess? "))
        if guess==val:
            print(playerlist[playercount], "You got it right!", "and it took", count, "turns!")
            retur=input("Do you want to return to the menu (y/n) ")
            if retur=='Y' or retur=='y' or retur=="yes":
                for count in range(25):
                    print('')
                controller.cont()
            else:
                banish()
                
        else:
            dist=val-guess
            if dist>0:
                print("That is wrong, it is Higher")
            else:
                print('That is wrong, it is Lower')
        if playercount>=(len(playerlist)):
            playercount=0
        else:
            playercount+=1
                
def restart(playerlist, playercount, mini, maxi):
    playercount+=1
    guessnum(mini, maxi, playerlist, playercount)
            
            
def banish():
    while 0<1:
        print(" ")
    
        
    
                
                
                
                
            
        
        
        
        
    
    