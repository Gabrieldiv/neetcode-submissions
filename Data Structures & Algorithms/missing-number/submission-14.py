class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        valor = 0

        for num in nums:
            valor += num
        return (n * (n + 1)) // 2 - valor
        
            
        