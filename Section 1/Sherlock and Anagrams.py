numberOfTestcases = int(input())
outputList = [] 
for testcase in range(numberOfTestcases) :
    s = input()  
    numberOfAnagrams = 0
    instances = {}
    for beginning in range(len(s)) :
        for length in range (1,len(s)+1-beginning) :
            tempList = sorted(s[beginning : beginning + length])
            tempString = ''.join(tempList)
            if tempString in instances :
                instances[tempString] += 1
            else :
                instances[tempString] = 1
            numberOfAnagrams+= instances[tempString] - 1
    outputList.append(str(numberOfAnagrams))
output = ('\n').join(outputList)
print (output)   