class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        menor_valor = prices[0]
        max_profit = 0

        for i in prices:
            if i < menor_valor:
                menor_valor = i

            if i - menor_valor > max_profit:
                max_profit = i - menor_valor
        return max_profit    
        
