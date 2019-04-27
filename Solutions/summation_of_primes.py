# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def isPrime(num):
    for i in range(2, num-1):
        if (num == 2):
            return True
        elif (num%i != 0):
            continue
        else:
            return False
    return True

def sumPrimes(num):
    sum_of_primes = 2

    for i in range(2, num):
        if (i%2 != 0 and isPrime(i)):
            sum_of_primes += i
        else:
            continue

    return sum_of_primes

if __name__ == '__main__':
    sum = sumPrimes(2000000)
    print sum