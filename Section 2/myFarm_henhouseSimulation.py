import random
from myFarm_chickenSimulation import *
from myFarm_duckSimulation import *
class henhouse (object) :
    def __init__(self,numberOfChicken,numberOfChicks,numberOfDucks,numberOfyoungDucks,numberOfٌRoasters,numberOfٌMaleDucks):
        self._numberOfChicken = numberOfChicken
        self._numberOfChicks = numberOfChicks
        self._numberOfDucks = numberOfDucks
        self._numberOfyoungDucks = numberOfyoungDucks
        self._numberOfRoasters = numberOfٌRoasters
        self._numberOfMaleDucks = numberOfٌMaleDucks
    def needs (self) :
        aRandomChicken = chicken()
        aRandomDuck = ducks()
        henhouseWaterNeed = aRandomChicken._waterNeed * self._numberOfChicken + aRandomDuck._waterNeed * self._numberOfDucks
        henhouseFoodNeed = aRandomChicken._foodNeed * self._numberOfChicken + aRandomDuck._foodNeed * self._numberOfDucks
        return ({'water need': henhouseWaterNeed,'food need':henhouseFoodNeed})
    def eggProduction (self,numberOfDays):
        chickenEggProduction = 0
        duckEggProduction = 0
        numberOfEggLayingChicken = self._numberOfChicken - (self._numberOfChicks + self._numberOfRoasters )
        numberOfEggLayingDucks = self._numberOfDucks - (self._numberOfyoungDucks + self._numberOfMaleDucks )
        randomisationFactor = ( numberOfEggLayingChicken + numberOfEggLayingDucks ) // 10
        for day in range(numberOfDays) :
            chickenEggProduction += numberOfEggLayingChicken + random.randint(-randomisationFactor,randomisationFactor)
            duckEggProduction += numberOfEggLayingDucks + random.randint(-randomisationFactor,randomisationFactor)
        return({'chicken egg production':chickenEggProduction,'duck egg production':duckEggProduction})

def henhouseDisplayMenu () :
    """
    Displays the menu of options for the user so that he wouldn't have to deal with
    any of the technical details
    """
    print('1.Predict egg production')
    print('2.Display needs')
    print('0.Exit henhouse management')
    print()
    print('Please choose an option from the above menu')
    
def getHenhouseDisplayMenuChoice ():
    """
    Gets the choice from the user
    """
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

def manageHenhouse () :
    """
    Manages the henhouse accroding to the suer choice
    """
    print('Welcome to henhouse management')
    print()
    while True :
        henhouseDisplayMenu ()
        option = getHenhouseDisplayMenuChoice ()
        print()
        DefaultHenHouse = henhouse(0,0,0,0,0,0)
        if option == 1 :
            while True :
                try:
                    numberOfChicken = int(input('Enter number of chicken: '))
                    break
                except ValueError :
                    print('Value not valid.Please enter number of chicken')
            while True :
                try:
                    numberOfChicks = int(input('How many of them are chicks (younger than 24 weeks)? '))
                    break
                except ValueError :
                    print('Value not valid.Please enter number of chicks')
            while True :
                try:
                    numberOfٌRoasters = int(input('How many of the mature chicken are roasters? '))
                    break
                except ValueError :
                    print('Value not valid.Please enter number of roasters')        
            while True :
                try:
                    numberOfDucks = int(input('Enter number of ducks: '))
                    break
                except ValueError :
                    print('Value not valid.Please enter number of ducks')
            while True :
                try:
                    numberOfyoungDucks = int(input('How many of them are yound ducks (younger than 24 weeks)? '))
                    break
                except ValueError :
                    print('Value not valid.Please enter number of young ducks')
            while True :
                try:
                    numberOfٌMaleDucks = int(input('How many of the mature ducs are males? '))
                    break
                except ValueError :
                    print('Value not valid.Please enter number of mail ducks') 
            while True :
                try:
                    numberOfDays = int(input('Enter number of days: '))
                    break
                except ValueError :
                    print('Value not valid.Please enter number of days')
            henHouseToManage = henhouse(numberOfChicken,numberOfChicks,numberOfDucks,numberOfyoungDucks,numberOfٌRoasters,numberOfٌMaleDucks)
            print()
            print(henHouseToManage.eggProduction (numberOfDays))
            print()
        elif option == 2 :
            try :
                print(henHouseToManage.needs ())
            except :
                print(DefaultHenHouse.needs ())
        elif option == 0 :
            break
    print()
    print('Thank you for using the henhouse management program')  