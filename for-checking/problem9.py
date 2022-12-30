"""
Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time


def solveProblem():
    """
    Returns the product of a Phytagorean triplet which satisifies the condition below

    "There exists exactly one Pythagorean triplet for which a + b + c = 1000."

    Note:

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
    """

    # Initial guess (first Phytagorean Triple)
    a = 3 
    b = 4 
    c = 5 

    # Loop through values of b
    while (b <= 1000):

        # Create list of valid a values from 3 to (b - 1) : uses unpacking operator
        valid_a = [*range(3, b, 1)]

        # Loop through all values of valid a values   
        for a in valid_a:
            
            # Solve for c_squared
            c_squared = (a * a) + (b * b)

            # Solve for c 
            c = pow(c_squared, 1/2)

            # Converting c into an integer type (from a float type) if c is an integer
            if c.is_integer():
                c = int(c)
                c_squared = c * c

            # For debugging: Print only those triples where c is an integer
            # if type(c) == int:
            #     print(a, b, c)

            # Return product of a,b and c if constraint is met
            if constraintSatisfied(a, b, c):
                return a*b*c

        # Increment b
        b += 1


    # No solution detected
    return None


def constraintSatisfied(a, b, c):
    """
    Checks if constraint (a + b + c = 1000) is satisfied
    """

    if (a + b + c) == 1000:
        return True

    else:
        return False


st = time.time() # Starting time

print(solveProblem()) # 31875000

et = time.time() # Ending time

elapsed_time = et - st 

# Prints execution time (.024 seconds)
print(f"Execution Time: {elapsed_time:.3f} seconds")

# Note: For improvement, determine upper bound when looping the values for b (instead of setting as 1000)