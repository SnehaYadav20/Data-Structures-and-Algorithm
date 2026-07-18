class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = min(nums)
        b = max(nums)

        if(a==0 or b==0):
            return max(a, b)

        while b:
            a, b = b, a % b

        return a
        
        