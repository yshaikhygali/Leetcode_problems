class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        num_jewels = []
        for j in list(J):
            for s in list(S):
                if j == s:
                    num_jewels.append(j)

        return len(num_jewels)
