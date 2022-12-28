"""
Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import time

def generatePrimeList(size):
    """
    Generates a list of prime number of given size

    Parameters
    ----------
    size : int
        Size of resulting prime numbers array
    """

    # Initialize primesList
    primesList = [2]

    # Set value to be investigated (starts with 3)
    numberCurrent = primesList[-1] + 1

    # Append prime numbers to primes list up to given size
    while len(primesList) < size:

        # Count occurences of number being divisible by another prime number
        primeFactors = 0

        # Divide number by existing numbers in primesList
        for prime in primesList:
            
            # If remainder is zero after divididing by a prime
            if numberCurrent % prime == 0:
                primeFactors += 1

        # If number is not divisible by any primes, append to primes list (number is a prime number)
        if primeFactors == 0:
            primesList.append(numberCurrent)

        # Increment to investigate the next number (Incremented by 2 to bypass even numbers, which are non-prime)
        numberCurrent += 2

    return primesList



st = time.time() # Starting time

print(generatePrimeList(10001)[10000]) # 104743

et = time.time() # Ending time

elapsed_time = et - st 

# Prints execution time (11 seconds)
print(f"Execution Time: {elapsed_time:.2f} seconds")




