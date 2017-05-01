from myFarm_chickenSimulation import *
from myFarm_duckSimulation import *
   
def poultryTypeDisplayMenu () :
    print('1.Manage chicken')
    print('2.Manage ducks')
    print('0.Exit poultry management')
    print()
    print('Please choose an option from the above menu')
def getPoultryTypeDisplayMenuChoice ():
    while True :
        try :
            choice = int(input('Select an option: '))
            if 0 <= choice <= 2 :
                break 
            else :
                print('Please enter a valid option')
        except ValueError :
            print('Please enter a valid option')
    return(choice)

def pickPoultryType () :
    print('Welcome to poultry management')
    print()
    while True :
        poultryTypeDisplayMenu ()
        option = getPoultryTypeDisplayMenuChoice ()
        print()
        if option == 1 :
            manageChicken ()
        elif option == 2 :
            manageDucks ()
        elif option == 0 :
            break
    print()
    print('Thank you for using the poultry management program')  
