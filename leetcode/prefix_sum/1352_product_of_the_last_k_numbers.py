class ProductOfNumbers:
    def __init__(self):
        self.tree = [1] * 4*10**6
        self.cont = 0
        self.last_zero = 0

    def add(self, num: int) -> None:
        self.cont += 1

        if num == 0:
            self.last_zero = self.cont
            return

        i = self.cont
        while i <= 4*10**6:
            self.tree[i] *= num
            i += i & -i

    def prefix_prod(self, i):
        result = 1
        while i > 0:
            result *= self.tree[i]
            i -= i & -i
        return result

    def getProduct(self, k: int) -> int:
        if self.cont - k < self.last_zero:
            return 0

        return self.prefix_prod(self.cont) // self.prefix_prod(self.cont - k)