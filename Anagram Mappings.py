from collections import Counter
class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        #creating a dictionary for B. We can use Counter as well
        bdict = {nums:i for i,nums in enumerate(B)}
        return [bdict[i] for i in A]
           
