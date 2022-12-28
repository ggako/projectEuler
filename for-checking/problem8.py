"""
Problem 7: 10001st prime

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

import math

def processStringToNum(filename):
    """
    Converts string from text to an integer 
    """

    # Create empty string to store text
    numberText = ""

    # Open text file
    with open(f"{filename}.txt") as f:

        # Read text file per line
        for line in f.readlines():

            # Add each line to the end of numberText
            numberText += line.strip()

    # Return integer form of text
    return int(numberText)

def greatestAdjacentProduct(number, digits):
    """
    Gets the greatest product of adjacent n-digits in a number

    Parameters
    ----------
    number : int
        Number to be scanned

    digits : int
        Number of digits adjacent to be considered when solving for the product
    """

    # Part 1: Initialization

    # Get string format of number (used to access index of a digit)
    stringNumber = str(number)

    # Get total number of digits
    totalDigits = len(str(number))

    # Get adjacent count - number of adjacent digits to be considered - how many products there will be
    adjacentCount = totalDigits - digits + 1

    # Initalize maximum product (arbitrarily set to negative)
    maxProduct = -math.inf

    # Initialize maximum adjacent digits
    maxAdjacent = ""



    # Part 2: Determining the maximum product

    # Loop through each index
    for currentIndex in range(adjacentCount):

        # Initialize product for current adjacent digits considered
        product = 1

        # Loop through each index adjacent digits (solving for the product of the adjacent digits)
        for n in range(digits):
            product *= int(stringNumber[currentIndex + n])

        # Update max product as needed
        if product > maxProduct:
            maxProduct = product

            # Reinitialize maxAdjacent to empty string (to clear maxAdjacent)
            maxAdjacent = ""

            # If max product is updated, loop through again and store the value of the adjacent digits
            for n in range(digits):
                maxAdjacent += stringNumber[currentIndex + n]
    
    # Return greatest product
    return (maxProduct, int(maxAdjacent))


# print(greatestAdjacentProduct(processStringToNum("for-checking/problem8"), 4)) # (5832, 9989)
print(greatestAdjacentProduct(processStringToNum("for-checking/problem8"), 13)) # (23514624000, 5576689664895)



"""
Equation for adjacentCount:

Pattern of digits to adjacent digits to be considered
111111111
total digits - 9
1 digits - 9 adjacent
2 digits - 8 adjacent
3 digits - 7 adjacent

adjacentCount = totalDigits - digits + 1
e.g. for product of 2 adjacent digits
adjacentCount = 9 - 2 + 1 = 8 adjacent to be considered when solving for the product   
"""