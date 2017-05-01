from myFarm_PoultrySimulation import *
import random
class ducks (poultry) :
    """
    A model of chicken in the farm
    """
    def __init__ (self) :
        super().__init__(1,4,4)
        self._type = "ducks"

    def grow (self,water,food,numberOfWeeks) :
        """
        Alters the behaviour of the grow method for ducks
        """
        for week in range (numberOfWeeks) :
            randomisationFactor = numberOfWeeks // 10
            waterThisWeek = water + random.randint( - randomisationFactor , randomisationFactor)
            foodThisWeek = food + random.randint( - randomisationFactor , randomisationFactor)
            if waterThisWeek >= self._waterNeed and foodThisWeek >= self._foodNeed :
                if self._age < 24 :
                    self._growth += self._growthRate * 1.5
                else :
                    self._growth += self._growthRate
            else :
                averageGrowthRate = ( waterThisWeek / self._waterNeed + foodThisWeek / self._foodNeed ) / 2
                if averageGrowthRate > self._growthRate :
                    if self._age < 24 :
                        self._growth += self._growthRate * 1.5
                    else :
                        self._growth += self._growthRate
                else :
                    if self._age < 24 :
                        self._growth += averageGrowthRate * 1.5
                    else :
                        self._growth += averageGrowthRate
        self._updateStatus()
        self._age += numberOfWeeks
        
def ducksDisplayMenu () :
    """
    Displays the menu of options for the user so that he wouldn't have to deal with
    any of the technical details
    """
    print('1.Grow ducks')
    print('2.Report status')
    print('3.Display needs')
    print('0.Exit ducks management')
    print()
    print('Please choose an option from the above menu')
    
def getDucskDisplayMenuChoice ():
    """
    Gets the choice from the user
    """
    while True :
        try :
            choice = int(input('Select an option: '))
            if 0 <= choice <= 4 :
                break 
            else :
                print('Please enter a valid option')
        except ValueError :
            print('Please enter a valid option')
    return(choice)

def manageDucks () :
    """
    Manages the crop accroding to the suer choice
    """
    print('Welcome to chicken management')
    print()
    while True :
        ducksDisplayMenu ()
        option = getDucskDisplayMenuChoice ()
        print()
        Defaultducks = ducks()
        if option == 1 :
            while True :
                try:
                    numberOfWeeks = int(input('Enter number of weeks: '))
                    break
                except ValueError :
                    print('Value not valid.Please enter number of weeks')
            while True :
                try :
                    food = int(input('Enter the amount of food with a number between 1 and 10: '))
                    if 0 <= food <= 10 :
                        break
                    else :
                        print('Value not valid.Please enter the amount of food with a number between 1 and 10: ')
                except :
                    print('Value not valid.Please enter the amount of food with a number between 1 and 10: ')
            while True :
                try :
                    water = int(input('Enter the amount of water with a number between 1 and 10: '))
                    if 0 <= water <= 10 :
                        break
                    else :
                        print('Value not valid.Please enter the amount of water with a number between 1 and 10: ')
                except :
                    print('Value not valid.Please enter the amount of water with a number between 1 and 10: ')
            ducksToManage = ducks()
            ducksToManage.grow (water,food,numberOfWeeks)
        elif option == 2 :
            try :
                print(ducksToManage.report ())
            except :
                print(Defaultducks.report ())
        elif option == 3 :
            print(Defaultducks.needs ())
        elif option == 0 :
            break
    print()
    print('Thank you for using the ducks management program')  
    
