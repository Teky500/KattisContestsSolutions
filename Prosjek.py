import random
import fractions
### The idea is to get the simplest fraction form of the given number.
# The minimum number of pages needed is always the denominator, and the sum of the numbers needed is the numerator
# We will simply choose as many 5's as possible, then fill the rest with ones and pick one of 2, 3, 4 if needed.
# This will work by solving the equation TOPVALUE-5*NumberOfFives = BOTTOMVALUE - NumberOfFives
# Will simplify to (TOPVALUE - BOTTOMVALUE)//4 = NumberOfFives, and (TOPVALUE - BOTTOMVALUE)%4 = Remainder
inputAsString = input()
Fraction = fractions.Fraction(inputAsString).as_integer_ratio()

fiveValue = (Fraction[0] - Fraction[1]) // 4
remainder = (Fraction[0] - Fraction[1]) % 4
oneValue = Fraction[1] - fiveValue
if remainder == 0:
    answer = [oneValue, 0, 0, 0, fiveValue]
if remainder == 1:
    answer = [oneValue - 1, 1, 0, 0, fiveValue]
if remainder == 2:
    answer = [oneValue - 1, 0, 1, 0, fiveValue]
if remainder == 3:
    answer = [oneValue - 1, 0, 0, 1, fiveValue]
for i in answer:
    print(i, end = ' ')

