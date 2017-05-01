import math
def get_next_prime_number() :
    number = 2
    while True :
        test = True
        for x in range(2, int(math.sqrt(number) + 1)):
            test = test and number % x != 0
        if test :
            yield number
            number+= 1
        else :
            number+=1
            
prime =  get_next_prime_number()
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))