class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        count = 0
        #Jset = set(J)
        #since letters are case sensitive  
        for s in S:
            if s in J:
                count+=1
        return count
