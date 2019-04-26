"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    elif n >=0:
        return 1

def isMultiple(input_num):
    for i in range(1,21):
        if (input_num%i == 0):
            continue
        else:
            return False
    return True

def smallestNum(n):
    for i in range(n, factorial(n) + 1, n):
        if isMultiple(i):
            print i
            return i
        else:
            continue

if __name__ == '__main__':
    smallestNum(15)