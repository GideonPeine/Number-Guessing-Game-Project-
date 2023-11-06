#controller runs the programs, and makes the functional system
import guess
import def_val
def cont():
    mini=0
    maxi=1000
    lop='t'
    print("\t", "Number Guessing Game")
    print("----------------------------------------")
    print("")
    print("1. set players")
    print("2. set maximun and minimum for range")
    print("3. play game")
    print("")
    print("")
    while lop=='t':
        activ=int(input("Enter input: "))
        if activ==1:
            ()
        elif activ==2:
            minmax=def_val.def_val()
            mini=minmax[0]
            maxi=minmax[1]
        elif activ==3:
            guess.guessnum(mini, maxi)
        
        
    
    
    