class Solution:
    def shortestPalindrome(self, s: str) -> str:
        letras = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
            'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
            'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
            'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
            'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
            'z': 26
        }

        base = 27
        mod = 10**9 + 7
        n = len(s)

        hash_s = 0
        hash_rev = 0
        potencia = 1
        mas = 0

        for i in range(n):
            hash_s = (hash_s + letras[s[i]] * potencia) % mod
            hash_rev = (hash_rev * base + letras[s[n - 1 - i]]) % mod

            # Comparar el prefijo con su reverso
            if hash_s == hash_rev:
                mas = i + 1

            potencia = (potencia * base) % mod

        return s[mas:][::-1] + s
