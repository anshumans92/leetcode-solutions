class Solution:
    def defangIPaddr(self, address: str) -> str:
        #simplest solution is to use string replace method
        return address.replace(".","[.]")
