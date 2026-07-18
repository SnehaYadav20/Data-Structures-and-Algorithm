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
        
        ans = a

        while ans > 0:
            if a % ans == 0 and b % ans == 0:
                break
            ans -= 1

        return ans
        
        