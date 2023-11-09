import controller

def def_val():
    #finds minimum and maximum
    mini = int(input('Enter the minimum: '))
    maxi='b'
    while maxi=='b' or maxi< mini:
        maxi = int(input('Enter the maxiumum: '))
    controller.cont()
    #sets variables if nothing is entered
    minmax=[mini, maxi]
  
    return(minmax)
        
    