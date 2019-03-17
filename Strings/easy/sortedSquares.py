class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        b = []
        for i in A:
            b.append(i**2)

        b.sort()

        return b
