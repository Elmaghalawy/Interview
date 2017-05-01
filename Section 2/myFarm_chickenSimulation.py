from myFarm_PoultrySimulation import *
import random
class chicken (poultry) :
    """
    A model of chicken in the farm
    """
    def __init__ (self) :
        super().__init__(1,3,4)
        self._type = "chicken"

    def grow (self,water,food,numberOfWeeks) :
        """
        Alters the behaviour of the grow method for chiken
        """
        for week in range (numberOfWeeks) :
            randomisationFactor = numberOfWeeks // 10
            waterThisWeek = water + random.randint( - randomisationFactor , randomisationFactor)
            foodThisWeek = food + random.randint( - randomisationFactor , randomisationFactor)
            if waterThisWeek >= self._waterNeed and foodThisWeek >= self._foodNeed :
                if self._age < 24 :
                    self._growth += self._growthRate * 1.25
                else :
                    self._growth += self._growthRate
            else :
                averageGrowthRate = ( waterThisWeek / self._waterNeed + foodThisWeek / self._foodNeed ) / 2
                if averageGrowthRate > self._growthRate :
                    if self._age < 24 :
                        self._growth += self._growthRate * 1.25
                    else :
                        self._growth += self._growthRate
                else :
                    if self._age < 24 :
                        self._growth += averageGrowthRate * 1.25
                    else :
                        self._growth += averageGrowthRate
        self._updateStatus()
        self._age += numberOfWeeks
        
def ChickenDisplayMenu () :
    """
    Displays the menu of options for the user so that he wouldn't have to deal with
    any of the technical details
    """
    print('1.Grow chicken')
    print('2.Report status')
    print('3.Display needs')
    print('0.Exit chicken management')
    print()
    print('Please choose an option from the above menu')
    
def getChcikenDisplayMenuChoice ():
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

def manageChicken () :
    """
    Manages the crop accroding to the suer choice
    """
    print('Welcome to chicken management')
    print()
    while True :
        ChickenDisplayMenu ()
        option = getChcikenDisplayMenuChoice ()
        print()
        DefaultChicken = chicken()
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
            chickenToManage = chicken()
            chickenToManage.grow (water,food,numberOfWeeks)
        elif option == 2 :
            try :
                print(chickenToManage.report ())
            except :
                print(DefaultChicken.report ())
        elif option == 3 :
            print(DefaultChicken.needs ())
        elif option == 0 :
            break
    print()
    print('Thank you for using the chicken management program')  
    
