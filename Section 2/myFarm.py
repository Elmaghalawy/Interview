from myFarm_pickCropType import *
from myFarm_pickPoultryType import *
from myFarm_henhouseSimulation import *
   
def farmDisplayMenu () :
    print('1.Manage crops')
    print('2.Manage poultry')
    print('3.Manage henhouse')
    print('0.Exit farm management')
    print()
    print('Please choose an option from the above menu')
def getFarmDisplayMenuChoice ():
    while True :
        try :
            choice = int(input('Select an option: '))
            if 0 <= choice <= 3 :
                break 
            else :
                print('Please enter a valid option')
        except ValueError :
            print('Please enter a valid option')
    return(choice)

def manageFarm () :
    print('Welcome to farm management')
    print()
    while True :
        farmDisplayMenu ()
        option = getFarmDisplayMenuChoice ()
        print()
        if option == 1 :
            pickCropType ()
        elif option == 2 :
            pickPoultryType ()
        elif option == 3 :
            manageHenhouse ()
        elif option == 0 :
            break
    print()
    print('Thank you for using the farm management program')
manageFarm ()