import random
firstLine = input()
numberOfCities = int(firstLine[:firstLine.index(' ')])
numberOfRoads = int(firstLine[firstLine.index(' ')+1:])
possibleRoads = []
for road in range (numberOfRoads) :
    Line = input()
    possibleRoads.append((int(Line[:Line.index(' ')]),int(Line[Line.index(' ')+1:])))
    possibleRoads.append((int(Line[Line.index(' ')+1:]),int(Line[:Line.index(' ')])))
cities = []
for i in range(1,numberOfCities+1) :
    cities.append(i)
paths = {}
for city in cities :
    for road in possibleRoads :
        if city == road[0] :
            try :
                paths[city] += (road[1],)
            except :
                paths[city] = (road[1],)

allPossiblePaths = []
lengths = {}
checkedBefore = []
def getAllpossiblePaths (city,beginning=0) :
    if city not in checkedBefore :
        checkedBefore.append(city)
        if city == beginning :
            allPossiblePaths.append((city,))
        possibleCities = paths[city]
        for anotherCity in possibleCities :
            for possiblePath in allPossiblePaths :
                if possiblePath[-1] == city and anotherCity not in possiblePath:
                    newPath = possiblePath + (anotherCity,)
                    if newPath not in allPossiblePaths :
                        allPossiblePaths.append(newPath)
                        try :
                            lengths[len(newPath)] += (newPath,)
                        except :
                            lengths[len(newPath)] = (newPath,)
            if numberOfCities not in lengths.keys() :
                getAllpossiblePaths (anotherCity)
            else :
                return(allPossiblePaths)
    return(allPossiblePaths)


for city in cities :
    allPaths = getAllpossiblePaths(city,city)
    if numberOfCities in lengths :
        break
bestlength = 0
for length in lengths :
    if length > bestlength :
        bestlength = length
longest = random.choice(lengths[bestlength])
print(len(longest))
for cityNumber in longest :
    print(cityNumber,end=' ')
        
