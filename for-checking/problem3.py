"""
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""



def maxPrimeFactor(number):

    # Initialize "global" prime factors list (global to the function maxPrimeFactor)
    primeFactorList = []


    def factorize(number):
        """
        Function that factorize and adds detected prime number to primeFactorList
        
        If number is not a prime number, calls itself using the factors obtained 
        """

        factor = 2

        while number % factor != 0:
            factor += 1

        factor_1 = factor
        factor_2 = number / factor
        
        # Check if unable to factorize (number is prime , factor is one and itself)
        if factor_1 == number and factor_2 == 1:
            primeFactorList.append(factor_1)
        # If still able to factorize , factorize both numbers (call same function)
        else:
            factorize(factor_1)
            factorize(factor_2)

    # Call factorize function
    factorize(number)

    # Returns maximum prime factor
    return max(primeFactorList)


# print(maxPrimeFactor(13195)) # Prints 29
print(maxPrimeFactor(600851475143)) # Prints 6857