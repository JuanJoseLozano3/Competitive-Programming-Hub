
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        ini = 1
        t = len(nums)
        base = max(nums)+1
        fin = t
        mod = 10**9 + 7
        inv = pow(base, mod-2, mod)

        while ini < fin:
            mitad = (fin+ini)//2
            set1 = set()
            set2 = set()
            rol = 0

            for i in range(mitad):
                rol += (nums[i]*pow(base,i,mod)) % mod
                rol %= mod

            set1.add(rol)
            potencia = pow(base, mitad-1, mod)

            for i in range(1,t-mitad+1):
                rol -= nums[i-1]
                rol = (rol*inv) % mod
                rol += (nums[mitad+i-1]*potencia) % mod
                rol %= mod

                if rol in set1:
                    set2.add(rol)
                else:
                    set1.add(rol)

            k = len(set1-set2)

            if k > 0:
                fin = mitad
            else:
                ini = mitad+1

        return ini