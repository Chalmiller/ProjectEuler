"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Helper function to determine if the number is a palindrome
def isPalindrome(num):

    numStr = str(num)
    reverseOrder = ""

    for i in range(1, len(numStr)+1):
        reverseOrder += numStr[-i]

    if (reverseOrder == numStr):
        return True
    else:
        return False

def largestPalindromeProduct():

    palindrome = []

    for i in range(100,1000):
        for j in range(100,1000):
            if isPalindrome(i*j):
                print i, j
                palindrome.append(i*j)

    return max(palindrome)

largestPalindromeProduct()
