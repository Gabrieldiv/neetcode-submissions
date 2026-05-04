class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dicionario = {}

        for letra in s:
            if letra in dicionario:
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1
        
        for letra in t:
            if letra in dicionario:
                dicionario[letra] -=1
            else:
                return False
        
        for letra, valor in dicionario.items():
            if valor != 0 :
                return False

        return True
        
        
        