"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def isPrime(x):
    for i in range(2,x-1):
        if (x%i == 0):
            return False
    else:
        return True

def largestPrimeFactor():
    prime_factors = []
    magic_number = 600851475143

    for magic_num_factors in range(5, magic_number/2):
        if (magic_number%magic_num_factors == 0 and magic_num_factors%2 != 0
                and magic_num_factors%3 != 0 and magic_num_factors%5 != 0):
            if (isPrime(magic_num_factors)):
                prime_factors.append(magic_num_factors)
                print(magic_num_factors)
        else:
            continue

    return prime_factors[-1]


if __name__ == '__main__':
    largestPrimeFactor()
