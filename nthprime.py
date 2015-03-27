from math import log, floor
from collections import deque
from numba import jit

@jit
def sieve(n):
    # Using a deque for faster appends
    primes = deque()
    primes.append(2)

    # Instantiate the sieve. We flip it around
    # to make use of pop().
    sieve = list(reversed(range(3, int(n + 1), 2)))

    # Run this loop while we still have things in the sieve
    while sieve:
        # Grab the last element of the sieve, which is a prime
        primes.append(sieve.pop())

        # Run through our sieve and construct a new list out of it
        sieve = list(filter(lambda x: x % primes[-1] != 0, sieve))

    return list(primes)


def nth_prime(n):
    # Make sure that the input makes sense
    if n < 1:
        raise ValueError("Input ({0}) must be greater than 0".format(n))

    # Get the upper bound using our nice function
    upper_bound = upper_bound_on_nth_prime(n)

    # Sieve on everything up to the upper bound
    primes = sieve(upper_bound)

    # Grab the nth prime, which is n-1 on the list
    return primes[n - 1]


def upper_bound_on_nth_prime(n):
    """ Comes from wikipedia:
    http://en.wikipedia.org/wiki/Prime-counting_function#Inequalities
    """
    if n <= 6:
        return 15
    else:
        return floor(n * log(n * log(n)))
        
import unittest


class NthPrimeTests(unittest.TestCase):
    def test_first_prime(self):
        self.assertEqual(2, nth_prime(1))

    def test_sixth_prime(self):
        self.assertEqual(13, nth_prime(6))

    def test_first_twenty_primes(self):
        self.assertEqual([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71],
                         [nth_prime(n) for n in range(1, 21)])

    def test_prime_no_10000(self):
        self.assertEqual(104729, nth_prime(10000))


if __name__ == '__main__':
    unittest.main()
