import controller

def player_amount():
    #player_amount accepts no arguments
    #prompts user for player amount
    #returns amount
    amount=-1
    while amount<1:
        amount = int(input('Enter amount of players: '))
    return amount

def player_names():
    #player_names accepts amount
    #prompts users for there names
    #returns players names
    name = (input('Enter name of player: '))
    controller.cont()
    return name