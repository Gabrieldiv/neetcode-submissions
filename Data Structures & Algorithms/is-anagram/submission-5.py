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
                dicionario[letra] -= 1
            else:
                return False
            if dicionario[letra] == 0:
                del dicionario[letra]
            
        return len(dicionario) == 0
        
        
        