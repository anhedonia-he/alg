# @algorithm @lc id=1950 lang=python3 
# @title sign-of-the-product-of-an-array


from en.Python3.mod.preImport import *
# @test([-1,-2,-3,-4,3,2,1])=1
# @test([1,5,0,2,-3])=0
# @test([-1,1,-1,1,-1])=-1
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        i, result = 0, 1
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            result = result * nums[i]
        if result > 0:
            return 1
        elif result < 0:
            return -1
        else: 
            return 0


