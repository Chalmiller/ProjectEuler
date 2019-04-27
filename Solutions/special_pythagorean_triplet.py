# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def isPythagoreanTriplet(a, b, c):
    if (a < b and b < c and equalToMagicNumber(a, b, c)):
        if (squareValue(a) + squareValue(b) == squareValue(c)):
            return True
        else:
            return False
    else:
        return False

def squareValue(num):
    return num**2

def equalToMagicNumber(a, b, c):
    if (a + b + c == 1000):
        return True
    else:
        return False

def iterator():
    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                if (isPythagoreanTriplet(k,j,i)):
                    return (i*j*k)
                else:
                    continue

if __name__ == '__main__':
    pythagoreanProduct = iterator()
    print pythagoreanProduct


