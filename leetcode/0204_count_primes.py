class Solution:
    def countPrimes(self, n: int) -> int:
        def criba(n):
            primos = [True]*n

            if n > 0:
                primos[0] = False

            if n > 1:
                primos[1] = False

            i = 2
            while i*i < n:
                if primos[i]:
                    j = i*i
                    while j < n:
                        primos[j] = False
                        j += i
                i += 1

            return primos

        return sum(criba(n))