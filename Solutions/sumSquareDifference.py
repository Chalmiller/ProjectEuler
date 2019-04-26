# """
# The sum of the squares of the first ten natural numbers is,
#
# 1**2 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# """

def sumOfSquares(num):
    sumOfSquares = 0

    for i in range(num+1):
        sumOfSquares += i**2

    return sumOfSquares

def squareOfSums(num):
    squareOfSums = 0

    for i in range(num+1):
        squareOfSums += i

    return squareOfSums**2

def differenceOfSquares(num):

    print (squareOfSums(num) - sumOfSquares(num))

    return (squareOfSums(num) - sumOfSquares(num))


if __name__ == '__main__':
    differenceOfSquares(100)
