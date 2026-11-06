class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        numSet = set(nums)
        def factorizacion_con_criba(num, lista_primos):
            factores = set()

            for primo in lista_primos:
                if primo * primo > num:
                    break
            
                while num % primo == 0:
                    factores.add(primo)
                    num //= primo
            
            if num > 1:
                factores.add(num)
            
            return factores

        n = max(nums)
        primo = [True] * (n + 1)
        primo[0] = primo[1] = False
        for p in range(2, int(math.sqrt(n)) + 1):
            if primo[p]:
                for i in range(p * p, n + 1, p):
                    primo[i] = False
        lista_primos = [i for i, es_primo in enumerate(primo) if es_primo]
        parent = {}
        rank = {}
        for i in range(n+1):
            if primo[i]:
                parent["P"+str(i)] = "P"+str(i)
                rank["P"+str(i)] = 0
        for i in nums:
            parent[i] = i
            rank[i] = 0

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                return True
            return False
        
        def find_biggest():
            familias = {}
        
            for num in nums:
                raiz = find(num)
                
                if raiz not in familias:
                    familias[raiz] = []
                familias[raiz].append(num)
            max_tamano = 0
            for raiz, integrantes in familias.items():
                tamano_actual = len(integrantes)
                if tamano_actual > max_tamano:
                    max_tamano = tamano_actual
        
            return max_tamano
            
        for num in nums:
            res = factorizacion_con_criba(num, lista_primos)
            for primo in res:
                union("P"+str(primo), num)
        return find_biggest()

        
        
