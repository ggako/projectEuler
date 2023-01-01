"""
Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
import math

def sumOfPrimes(maxNum):
    """
    Gets the sum of prime numbers below maxNum
    Algorithm used: Sieve of Eratosthenes

    Parameters
    ----------
    maxNum : int
        Upper bound of prime numbers to be considered
    """

    # Initialize empty list
    primesList = list()

    # Generate a list containing numbers from 2 to maxNum - 1 
    # Note: Index - represents the prime number
    # Note: If a number is prime: its value will be 1, otherwise will be 0 (initially all will be assumed to be primes)
    for index in range(maxNum):
        primesList.append(1)

    # Set 0 and 1 (known non-primes) to be 0
    primesList[0] = 0
    primesList[1] = 0

    

    # Loop index values up to the ceiling of the square root of maxNum 
    # (no need to loop up to maxNum since factors come in pair - number will be struck off by one of its factors)
    # e.g. 15 -> ceil(sqrt(15)) = 4 
    # Factors below 4 (excluding 1) -> 3 paired with 5 ; 15 will be knocked out knowing 3 is a factor - 3 * 5
    for index in range(2, int(math.ceil(pow(maxNum, 1/2)))):

        # Check if current index is a prime number
        if primesList[index] == 1:
            
            # Initialize index multiplier
            indexMultiplier = 2

            # Change for multiplicity of the current index
            while (index * indexMultiplier) < maxNum:
                
                # Set multiples as non-prime
                primesList[index * indexMultiplier] = 0
                
                # Increment index multiplier
                indexMultiplier += 1

    # Initialize sum of primes
    sumPrimes = 0


    # Loop through primesList and add the sum of primes the items with index of 1 (representing the prime numbers)
    for index in range(maxNum):

        if primesList[index] == 1:

            sumPrimes += index
            
    return sumPrimes





    
st = time.time() # Starting time

# print(sumOfPrimes(10)) # 17
print(sumOfPrimes(2000000)) # 142913828922

et = time.time() # Ending time

elapsed_time = et - st 

# Prints execution time (.670 seconds)
print(f"Execution Time: {elapsed_time:.3f} seconds")







