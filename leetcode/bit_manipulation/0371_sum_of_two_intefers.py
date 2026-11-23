class Solution:
    def getSum(self, a: int, b: int) -> int:
        num1 = bin(a & 0xFFFFFFFF)[2:].zfill(32)
        num2 = bin(b & 0xFFFFFFFF)[2:].zfill(32)

        f = ""
        aca = 0

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(32):
            p = [int(num1[i]), int(num2[i]), aca]
            l = p.count(1)

            if l == 3:
                f += "1"
                aca = 1
            elif l == 2:
                f += "0"
                aca = 1
            elif l == 1:
                f += "1"
                aca = 0
            else:
                f += "0"
                aca = 0

        f = f[::-1]
        resultado = int(f, 2)
        if resultado > 0x7FFFFFFF:
            resultado = resultado ^ 0xFFFFFFFF
            resultado = ~resultado

        return resultado