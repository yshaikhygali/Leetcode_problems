class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()

        for i in A:
            s.add(i)

        n = sum(A) - sum(s)

        return n/(len(s)-2)
