import random as ran
import controller
#operation guessnum gets random number and asks for guess
def guessnum(mini, maxi):
    print(mini)
    print(maxi)
    val=ran.randint(mini, maxi)
    run='t'
    count=0
    while run=='t':
        count+=1
        guess=int(input("What is your guess? "))
        if guess==val:
            print("Yay! you got it right! And it only took you", count, "Guesses!")
            go_again=input("Do you want to go again? (y/n)")
            if go_again=='n' or go_again=='N':
                run='f'
                contoller.cont()
            else:
                guessnum(maxi, mini)
        else:
            dist=val-guess
            if dist>0:
                print("That is wrong, it is Higher")
            else:
                print('That is wrong, it is Lower')
            
        
    
                
                
                
                
            
        
        
        
        
    
    