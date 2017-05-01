import random
class crop (object) :
    """
    A model of a generic crop in the farm
    """
    def __init__ (self,growthRate,lightNeed,waterNeed) :
        """
        growthRate (integer) : a number that indicates how much the crop 
        grows for one day if its water and light needs are provided
        lightNeed (integer) : a number between 1 and 10 represinting the 
        amount of light needed for the crop to grow by the growth rate
        waterNeed(integer) : a number between 1 and 10 represinting the
        amount of water needed for the crop to grow by the growth rate
        """
        self._growthRate = growthRate
        self._lightNeed = lightNeed
        self._waterNeed = waterNeed
        self._age = 0
        self._growth = 0
        self._status = "Seed"
        self._type = "Generic"
    def needs(self) :
        """
        Returns a dictionary indicating the light and water needs of the crop 
        """
        return ({'water need':self._waterNeed,'light need':self._lightNeed})
    def report(self) :
        """
        Returns a dictionary indicating the status,type,growth and age in days
        """
        return({'status':self._status,'type':self._type,'growth':round(self._growth,0),'age':self._age})
    def _updateType (self,cropType) :
        """
        Alters the crop type . A private method not to be used directly but only through 
        other methods
        cropType (string) : the name of the crop
        """
        self._type = cropType
    def _updateStatus (self):
        """
        Updates the status according to the level of growth achieved
        """
        if self._growth > 60 :
            self._status = 'Old'
        elif self._growth > 40 :
            self._status = 'Mature'
        elif self._growth > 20 :
            self._status = 'Young'
        elif self._growth > 0 :
            self._status = 'Seeding'
        else :
            self._status = 'Seed'
    def grow (self,water,light,numberOfDays) :
        """
        Mimics the real-life behaviour of the growing crops and predicts the result 
        after a certain amount of time
        water (integer) : a number indicating the average amount of water provided 
        for the crop over the time of the simulation . Varies by a randomisation 
        factor depending on the number of days
        light (integer) : a number indicating the average amount of light provided 
        for the crop over the time of the simulation . Varies by a randomisation 
        factor depending on the number of days
        numberOfDays (integer) : number of days for simulation 
        """
        for day in range (numberOfDays) :
            randomisationFactor = numberOfDays // 10
            waterThisDay = water + random.randint( - randomisationFactor , randomisationFactor)
            lightThisDay = light + random.randint( - randomisationFactor , randomisationFactor)
            if waterThisDay >= self._waterNeed and lightThisDay >= self._lightNeed :
                self._growth += self._growthRate
            else :
                averageGrowthRate = ( waterThisDay / self._waterNeed + lightThisDay / self._lightNeed ) / 2
                if averageGrowthRate > self._growthRate :
                    self._growth += self._growthRate
                else :
                    self._growth += averageGrowthRate
        self._updateStatus()
        self._age += numberOfDays
        
def cropDisplayMenu () :
    """
    Displays the menu of options for the user so that he wouldn't have to deal with
    any of the technical details
    """
    print('1.Grow crop')
    print('2.Report status')
    print('3.Display needs')
    print('0.Exit crop management')
    print()
    print('Please choose an option from the above menu')
    
def getCropDisplayMenuChoice ():
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

def manageCrop (cropType) :
    """
    Manages the crop accroding to the user choice
    """
    print('Welcome to crop management')
    print()
    while True :
        cropDisplayMenu()
        option = getCropDisplayMenuChoice ()
        print()
        if option == 1 :
            while True :
                try:
                    numberOfDays = int(input('Enter number of days: '))
                    break
                except ValueError :
                    print('Value not valid.Please enter number of days')
            while True :
                try :
                    light = int(input('Enter the amount of light with a number between 1 and 10: '))
                    if 0 <= light <= 10 :
                        break
                    else :
                        print('Value not valid.Please enter the amount of light with a number between 1 and 10: ')
                except :
                    print('Value not valid.Please enter the amount of light with a number between 1 and 10: ')
            while True :
                try :
                    water = int(input('Enter the amount of water with a number between 1 and 10: '))
                    if 0 <= water <= 10 :
                        break
                    else :
                        print('Value not valid.Please enter the amount of water with a number between 1 and 10: ')
                except :
                    print('Value not valid.Please enter the amount of water with a number between 1 and 10: ')
            crop.grow (cropType,water,light,numberOfDays)
        elif option == 2 :
            print(crop.report (cropType))
        elif option == 3 :
            print(crop.needs (cropType))
        elif option == 0 :
            break
    print()
    print('Thank you for using the crop management program')   