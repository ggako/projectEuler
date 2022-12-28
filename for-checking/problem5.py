"""
Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import time

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



def condenseDivisibleList(list):
    """
    Removes list items for numbers already divisible by another

    e.g. if a number is divisible by 20 , no need to check if a number is divisible by 1,2,3,4,5,10

    e.g. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] is condensed into
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
    """

    # Create a copy of list to avoid mutation of original list
    listCopy = list.copy()

    # Create a reverse sorted copy of list to avoid mutation of original list (will start checking at the largest number)
    listCopySorted = sorted(list, reverse=True)

    # Loop throughout list and check if a larger number is divisible by that number which should be omitted in listCopy 
    for number in list:
        
        # Loop each number in reverse sorted list and check for divisibility
        for largerNumber in listCopySorted:

            # Stops checking further the sorted list when largerNumber is now the same as number
            if largerNumber == number:
                break

            # Removes if detected divisibility
            if largerNumber % number == 0:
                if number in listCopy:
                    listCopy.remove(number)

    # Return condensed version of list
    return listCopy



def smallestDivisibleByAll(list):
    """
    Returns the smallest number that is divisible by all the numbers in the list
    """

    # Initialize number (set as a multiple of the minimum of the list)
    
    numberCurrent = min(list)

    while numberCurrent < max(list):
        numberCurrent += min(list)
    
    # Use the minimum as an increment to the numbers to be investigated (to retain divisibility by this number)
    increment = min(list)

    # Flag variable that stops while loop if number is found
    numberFound = False

    while numberFound != True:
        
        # Create a copy of list to avoid mutation of original list
        listCopy = list.copy()

        # Loop through all numbers in list
        for numInList in list:

            # Removes from list copy if divisible
            if numberCurrent % numInList == 0:
                listCopy.remove(numInList)
            
            # Break the for loop for non-divisible case
            else:
                break

        # Check if length of listCopy is zero (implies number is divisible by all numbers in list)
        if len(listCopy) == 0:
            numberFound = True
        # If not completely divisible, increment for next iteration (next to be investigated)
        else:
            numberCurrent += increment
    
    # Return first number found that is divisble by all the numbers in list
    return numberCurrent


        

# print(smallestDivisibleByAll(condenseDivisibleList(listSequenceGenerate(1, 10, 1)))) # 2520

st = time.time() # Starting time

print(smallestDivisibleByAll(condenseDivisibleList(listSequenceGenerate(1, 20, 1)))) # 232792560

et = time.time() # Ending time

elapsed_time = et - st 

# Prints execution time (between 6 to 7 seconds)
print(f"Execution Time: {elapsed_time:.2f} seconds")