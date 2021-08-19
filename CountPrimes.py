from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosthenes approach
        # O(nloglogn) time and O(n) space
        
        if n <= 1:
            return 0
        
        num_primes = 0
        primes = [False,False] + [True]*(n-2)
        for i in range(2, int(sqrt(n)) + 1):
            if primes[i]:
                factor = 0
                j = (i**2) + (i * factor)
                while j < n:
                    primes[j] = False
                    factor += 1
                    j = (i**2) + (i * factor)
        
        # count the number of primes now
        for prime in primes:
            if prime:
                num_primes += 1
        return num_primes