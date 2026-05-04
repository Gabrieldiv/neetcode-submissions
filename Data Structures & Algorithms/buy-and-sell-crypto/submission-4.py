class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        menor_preco = prices[0]
        profit = 0

        for preco in prices:
            if preco < menor_preco:
                menor_preco = preco
            if (preco - menor_preco) > profit:
                profit = (preco - menor_preco)
        
        return profit
            
