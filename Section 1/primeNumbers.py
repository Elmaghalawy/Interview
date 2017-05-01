import math
class PrimeNumbers (object):
    def __init__ (self):
        self.number = 2
    def get_next_prime_number(self) :
        while True :
            test = True
            for x in range(2, int(math.sqrt(self.number) + 1)):
                test = test and self.number % x != 0
            if test :
                print(self.number)
                self.number+= 1
                break
            else :
                self.number+=1
                
prime = PrimeNumbers()
prime.get_next_prime_number()
prime.get_next_prime_number()
prime.get_next_prime_number()
prime.get_next_prime_number()
prime.get_next_prime_number()