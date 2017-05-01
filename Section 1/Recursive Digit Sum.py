def findSuperDigit (n,k) :
    if len(str(n)) == 1:
        superDigit = n
    else :
        total = 0
        for digit in str(n) :
            total += int(digit) 
        newValue = total * k
        superDigit = findSuperDigit(newValue,1)
    return(superDigit)
userInput = input()
n = int(userInput[:userInput.index(' ')])
k = int(userInput[userInput.index(' ')+1:])
print( findSuperDigit(n,k))