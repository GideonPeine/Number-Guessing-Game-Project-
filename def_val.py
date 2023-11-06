def def_val():
    #de_val accepts no arguments
    #determines higher or lower
    #ouputs if they guess it or not
    mini = int(input('Enter the minimum: '))
    maxi=1000
    while maxi<mini:
        maxi = int(input('Enter the maxiumum: '))
    
    #sets variables if nothing is entered
    if mini == 0 or mini == '':
        mini = 1
    if maxi == 0 or maxi == '':
        maxi = 1000
    minmax=[mini, maxi]
    return(minmax)
        
    