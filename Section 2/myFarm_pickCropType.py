from myFarm_cropSimulation import *
# Hypthetically the crops aren't differnet in the way thery behave but they just have different values
# That's why I created a dictionary with the crop names as keys and the values associated with them
cropDictionary = {'Potato':(2,4,5),'Wheat':(3,3,5),'Rice':(1,5,3),'Tomato':(2,3,4)}    
IndexDictionary = {}
   
def cropTypeDisplayMenu () :
    counter = 0
    for cropType in cropDictionary :
        counter += 1
        IndexDictionary[counter] = cropType
        print(str(counter) + '.' +cropType)
    print(str(counter+1)+'.'+'Another crop')
    print('0.Exit the program')
    print()
    print('Please choose an option from the menu above')

def getCropTypeDsplayMenuChoice () :
    """
    Displays the menu of options for the user so that he wouldn't have to deal with
    any of the technical details
    """
    while True :
        try :
            print()
            choice = int(input('Select an option: '))
            if 0 <= choice <= len(cropDictionary) + 1 :
                break
            else :
                print('Value not valid.Please enter a number between 0 and ' + str(len(cropDictionary)+1))
        except ValueError :
            print('Value not valid.Please enter a number between 0 and ' + str(len(cropDictionary)+1))
    return(choice)

def pickCropType () :
    """
    If the user chooses a crop from the menu it starts the crop management program . If the user 
    wants to manage a new crop that isn't in the dictionary it asks for the values for the new
    crop and adds it to the crop dictionary for future use
    """
    print('Please choose a crop to manage')
    print()
    while True :
        cropTypeDisplayMenu ()
        option = getCropTypeDsplayMenuChoice ()
        if 1 <= option <= len(cropDictionary) :
            cropTypeName = IndexDictionary[option]
            cropTypeToManage = crop(cropDictionary[cropTypeName][0],cropDictionary[cropTypeName][1],cropDictionary[cropTypeName][2])
            crop._updateType (cropTypeToManage,cropTypeName)
            manageCrop(cropTypeToManage)
        elif option == len(cropDictionary) + 1 :
            cropTypeName = input('Please enter the name of the new crop type: ')
            cropGrowthRate = int(input('Please enter the growth rate of the new crop type: '))
            cropLightNeed = int(input('Please enther the light need of the new crop type with a number between 1 and 10: '))
            cropWaterNeed = int(input('Please enter the water need of the new crop type with a number between 1 and 10: '))
            cropDictionary[cropTypeName] = (cropGrowthRate,cropLightNeed,cropWaterNeed)
            cropTypeToManage = crop(cropGrowthRate,cropLightNeed,cropWaterNeed)
            crop._updateType (cropTypeToManage,cropTypeName)
            manageCrop(cropTypeToManage)
        elif option == 0 :
            break
    print()
    print('Thank you for using our program')