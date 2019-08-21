class Solution:
    def removeVowels(self, S: str) -> str:
        if not str:
            return
        ret = ""
        vowels = ['a','e','i','o','u']
        for i in S:
            if i not in vowels:
                ret+=i
        return ret
