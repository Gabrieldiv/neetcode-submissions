class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()


        for indice, valor in enumerate(nums):
            valor1 = valor
            if indice != valor:
                return indice
            else:
                valor1 = valor +1
        return valor1
        
            
        