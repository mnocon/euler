from math import ceil
from math import sqrt

class Math():
    def __init__(self):
        self.primes = {}
        self.tests()

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
