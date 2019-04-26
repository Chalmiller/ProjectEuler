# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?

def isPrime(num):

    if (num < 2):
        return False
    elif (num == 2):
        return True
    else:
        for i in range(2, num-1):
            if (num%i != 0):
                continue
            else:
                return False
        return True

def numberPrime(index):
    iterator = 1
    count = 1

    while (count <= index):
        if (isPrime(iterator)):
            if (count == index):
                print iterator

                return iterator
            else:
                count += 1
                iterator += 1
        else:
            iterator += 1



if __name__ == '__main__':
    answer = numberPrime(10001)
    print(answer)
