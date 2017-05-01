numbersInput = input ()
listOfNumbers = numbersInput.split()
listOfNumbers = [int(number) for number in listOfNumbers]
minimumSum = sum(listOfNumbers) -  max(listOfNumbers)
maximumSum = sum(listOfNumbers) -  min(listOfNumbers)
print(str(minimumSum) + ' ' + str(maximumSum))