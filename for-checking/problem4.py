"""
Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

import math

def isPalindrome(number):
    """
    Checks if number is a palindrome

    Note: Only works for non-negative values
    """

    # Reverse digits of number
    # Note: Typecasted number to string, used the [::]  method for slicing string to get the reverse, then typecasted back to integer
    reversedNumber = int(str(number)[::-1])

    # Compare with original number
    if number == reversedNumber:
        return True
    else:
        return False

def getMaxPalindrome(digitSize):
    """
    Returns the maximum palindrome from product of 2 sized n digits
    """
    # Initialize maxPalindromeFromProduct (arbitrarily negative infinity)
    maxPalindromeFromProduct = -math.inf

    # Loop through all numbers of digitSize
    for digit1 in range(pow(10, digitSize - 1), pow(10, digitSize)):
        for digit2 in range(pow(10, digitSize - 1), pow(10, digitSize)):

            # Get the  product of two digitSize-digit numbers
            product = digit1 * digit2

            # Check if the product is a palindrome
            if isPalindrome(product):
                maxPalindromeFromProduct = product

    return maxPalindromeFromProduct


# print(getMaxPalindrome(2)) # 9009
print(getMaxPalindrome(3)) # 580085