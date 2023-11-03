#number guessing game

def num_guess():
    #num_guess accepts no arguments
    #determines higher or lower
    #ouputs if they guess it or not
    minimum = int(input('Enter the minimum: '))
    maximum = int(input('Enter the maxiumum: '))
    
    #sets variables if nothing is entered
    if minimum == 0 or minimum == '':
        minimum = 1
    if maximum == 0 or maximum == '':
        maximum = 1000
    print (minimum, maximum)
        
    
    