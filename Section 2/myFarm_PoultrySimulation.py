import random
class poultry (object) :
    """
    A model of a generic poultry in the farm
    """
    def __init__ (self,growthRate,foodNeed,waterNeed) :
        """
        growthRate (integer) : a number that indicates how much the poultry 
        grows for one day if its water and food needs are provided
        foodNeed (integer) : a number between 1 and 10 represinting the 
        amount of food needed for the poultry to grow by the growth rate
        waterNeed(integer) : a number between 1 and 10 represinting the
        amount of water needed for the poultry to grow by the growth rate
        """
        self._growthRate = growthRate
        self._foodNeed = foodNeed
        self._waterNeed = waterNeed
        self._age = 0
        self._growth = 0
        self._status = "Newly hatched"
        self._type = "Generic"
    def needs(self) :
        """
        Returns a dictionary indicating the food and water needs of the poultry 
        """
        return ({'water need':self._waterNeed,'food need':self._foodNeed})
    def report(self) :
        """
        Returns a dictionary indicating the status,type,growth and age in weeks
        """
        return({'status':self._status,'type':self._type,'growth':round(self._growth,0),'age':self._age})
    def _updateStatus (self):
        """
        Updates the status according to the level of growth achieved
        """
        if self._growth > 36 :
            self._status = 'Old'
        elif self._growth > 24 :
            self._status = 'Mature'
        elif self._growth > 12 :
            self._status = 'Young'
        elif self._growth > 0 :
            self._status = 'baby'
        else :
            self._status = "Newly hatched"
    def grow (self,water,food,numberOfWeeks) :
        """
        Mimics the real-life behaviour of the growing crops and predicts the result 
        after a certain amount of time
        water (integer) : a number indicating the average amount of water provided 
        for the crop over the time of the simulation . Varies by a randomisation 
        factor depending on the number of days
        food(integer) : a number indicating the average amount of food provided 
        for the crop over the time of the simulation . Varies by a randomisation 
        factor depending on the number of days
        numberOfweeks (integer) : number of weeks for simulation 
        """
        for week in range (numberOfWeeks) :
            randomisationFactor = numberOfWeeks // 10
            waterThisWeek = water + random.randint( - randomisationFactor , randomisationFactor)
            foodThisWeek = food + random.randint( - randomisationFactor , randomisationFactor)
            if waterThisWeek >= self._waterNeed and foodThisWeek >= self._foodNeed :
                self._growth += self._growthRate
            else :
                averageGrowthRate = ( waterThisWeek / self._waterNeed + foodThisWeek / self._foodNeed ) / 2
                if averageGrowthRate > self._growthRate :
                    self._growth += self._growthRate
                else :
                    self._growth += averageGrowthRate
        self._updateStatus()
        self._age += numberOfWeeks
        
 