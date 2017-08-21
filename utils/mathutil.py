from math import ceil
from math import sqrt
from math import log10
from collections import defaultdict

class Math():
    def __init__(self):
        self.primes = {}
        self.divisors = defaultdict(list)
        self.tests()

    def get_prime_divisors(self, n):
        original_n = n
        if self.primes[n]:
            self.divisors[n].append(n)
            return [n]
        factor = 2
        while n != 1:
            if not self.primes[factor]:
                factor += 1
                continue
            if n % factor == 0:
                self.divisors[n].append(factor)
                old_n = n
                n = int(n / factor)
                if len(self.divisors[n]) > 0:
                    self.divisors[old_n].extend(self.divisors[n])
                    return self.divisors[old_n]
            else:
                factor += 1

        return self.divisors[original_n]

    def number_of_digits(self, n):
        return int(log10(n)) + 1

    def get_digits(self, n):
         return set(sorted([int(x) for x in str(n)]))

    def get_primes(self, start_range, end_range):
        primes = {}
        primes[1] = False
        for x in range(start_range, end_range):
            if x not in primes:
                primes[x] = True
                self.primes[x] = True
                for x in range(2 * x, end_range, x):
                    primes[x] = False
                    self.primes[x] = False

        return (x for x in primes if primes[x])        

    def is_prime(self, n):
            if n in self.primes:
                return self.primes[n]
            else:
                if n < 2:
                    self.primes[n] = False
                elif n == 2:
                    self.primes[n] = True
                elif n % 2 == 0:
                    self.primes[n] = False
                else:
                    for x in range(3, int(ceil(sqrt(n))) + 1):
                        if n % x == 0:
                            self.primes[n] = False
                            break

            if not n in self.primes:
                self.primes[n] = True

            return self.primes[n]

    def tests(self):
        assert len(list(self.get_primes(2, 1000))) == 168

        assert self.is_prime(2)
        assert self.is_prime(3)
        assert self.is_prime(5)
        assert self.is_prime(7)
        assert self.is_prime(11)
        assert self.is_prime(13)

        assert not self.is_prime(9)
        assert not self.is_prime(15)
        assert not self.is_prime(100)
        assert not self.is_prime(4)
        assert not self.is_prime(1)

        assert self.number_of_digits(133) == 3

        assert self.get_digits(123) == {1, 2, 3}
        assert self.get_digits(122233) == {1, 2, 3}
        assert self.get_digits(312) == {1, 2, 3}
