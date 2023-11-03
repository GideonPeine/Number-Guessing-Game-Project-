#number guessing game

def minimum():
    #num_guess accepts no arguments
    #determines minimum and maximum
    #returns minimum and maximum 
    
    #grabs variables from users
    minimum = int(input('Enter the minimum: '))
    
    
    #sets variables if nothing is entered
    if minimum == 0:
        minimum = 1
        
    #returns value
    return minimum

def maximum():
    #maximum accepts no arguments
    #prompts user for maximum
    #returns maximum
    
    #grabs variables from users
    maximum = int(input('Enter the maxiumum: '))
    
    #sets variables if nothing is entered
    if maximum == 0:
        maximum = 1000
        
    #returns value
    return maximum 
        
def player_amount():
    #player_amount accepts no arguments
    #prompts user for player amount
    #returns amount
    amount = int(input('Enter amount of players: '))
    
    return amount
        
        
    
    