class Solution:
    def removeVowels(self, S: str) -> str:
        #check if input string is present
        if not str:
            return
        ret = ""
        vowels = ['a','e','i','o','u']
        #basic for loop check
        for i in S:
            if i not in vowels:
                ret+=i
        return ret
