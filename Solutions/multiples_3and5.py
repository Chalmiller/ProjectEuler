"""
The problem is stated as:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""


class Multiples:

    def __init__(self, multiple):
        # Place holder init until more problems are solved.
        self.multiple = multiple

    @staticmethod
    def multiples_3and5(self):

        multiples_list = []
        sum_multiples = 0

        for i in range(1, 1000):
            if i%3 == 0 or i%5 == 0:
                multiples_list.append(i)
            else:
                continue
        for i in multiples_list:
            sum_multiples += i

        return sum_multiples
