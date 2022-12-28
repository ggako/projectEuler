"""
Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
(1^2) + (2^2) + .... (10^2) = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + .... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def listSequenceGenerate(start, end, stepSize = 1):
    """
    Returns a list with the following inputs given:

    start - starting point
    end - ending point (included in the list)
    stepSize - step size

    e.g. listSequenceGenerate(1, 20, 1) creates 
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    """

    sequence = [] 

    for number in range(start, end + 1, stepSize):
        sequence.append(number)

    return sequence


def sumOfSquares(list):
    """
    Returns sum of squares given a list of numbers
    """

    # Initialize sum variable
    sum = 0

    # Add sum of squares of each number in the list to sum
    for number in list:
        sum += pow(number, 2)

    # Return the total sum of squares
    return sum


def squareOfSums(list):
    """
    Returns squares of sum of a given list of numbers
    """

    # Return the square of the sum of a list
    return pow(sum(list), 2)



# difference = squareOfSums(listSequenceGenerate(1, 10, 1)) - sumOfSquares(listSequenceGenerate(1, 10, 1))
# print(difference) # 2640

difference = squareOfSums(listSequenceGenerate(1, 100, 1)) - sumOfSquares(listSequenceGenerate(1, 100, 1))
print(difference) # 25164150