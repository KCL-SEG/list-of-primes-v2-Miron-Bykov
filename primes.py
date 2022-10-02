"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [ ]
    total = 0
    if number_of_primes < 1:
        raise ValueError("You must enter a positive integer")

    while total < number_of_primes:
        if len(list) == 0:
            for i in range(2, number_of_primes + 1):
                count = 0
                for j in range(1, i + 1):
                    if i % j == 0:
                        count += 1
                if count < 3:
                    list.append(i)
                    total += 1
        else:
            #quite inefficient
            for i in range(list[-1] + 1, list[-1] + 20):
                if total >= number_of_primes:
                    break
                count = 0
                for j in range(1, i + 1):
                    if i % j == 0:
                        count += 1
                if count < 3:
                    list.append(i)
                    total += 1
    return list
