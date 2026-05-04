class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for indice, valor in enumerate(nums):
            diff = target - valor
            if diff in seen:
                return [seen[diff], indice]
            else:
                seen[valor] = indice
        return False
        
            
        