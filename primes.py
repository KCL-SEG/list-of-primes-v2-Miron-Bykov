"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(numOfPrimes):
    if numOfPrimes<1:
        raise ValueError("ValueError exception thrown")
    else:
        list = [2]
        numToTest=2
        while len(list)!=numOfPrimes:
            numToTest+=1
            if isPrime(numToTest, True):
                list.append(numToTest)
    return list

def isPrime(number, bool):
    prime=bool
    if number%2:
        for i in range (3,(number+1)//2,2):
            if number%i==0:
                prime=False
                break
        return prime