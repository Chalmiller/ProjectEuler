"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def isPrime(x):
    for i in range(2,x/2):
        if (x%i == 0):
            return False
    else:
        return True

def largestPrimeFactor():
    divisors = []
    prime_factors = []
    magic_number = 600851475143

    for magic_num_factors in range(5, magic_number/2):
        if (magic_number%magic_num_factors == 0):
            divisors.append(magic_num_factors)
        else:
            continue

    for factors in divisors:
        if (isPrime(factors)):
            prime_factors.append(factors)

    return prime_factors[-1]


if __name__ == '__main__':
    largestPrimeFactor()
