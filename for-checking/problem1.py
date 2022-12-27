"""
Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def sumOfMultiples(upperBoundExclusive):
    """
    Gets sum of multiples of 3 and 5 from 0 to a non-exclusive upperbound (upperBoundExclusive)
    """

    # Create empty set to store multiples
    multiples = set()

    # Loop from 0 to 999
    for number in range(upperBoundExclusive):
        # Check if multiple of 3
        if number % 3 == 0:
            multiples.add(number)
        # Check if multiple of 5
        if number % 5 == 0:
            multiples.add(number)

    # Get sum of multiples
    sumOfMultiples = sum(multiples)

    return sumOfMultiples

print(sumOfMultiples(10)) #Prints 23
print(sumOfMultiples(1000)) #Prints 233168


