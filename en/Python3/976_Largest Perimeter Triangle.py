# @algorithm @lc id=1018 lang=python3 
# @title largest-perimeter-triangle


from en.Python3.mod.preImport import *
# @test([2,1,2])=5
# @test([1,2,1])=0
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        for i in range(len(nums)-2):
            base, len1, len2 = nums[i], nums[i+1], nums[i+2]
            if len1 + len2 > base:
                return base + len1 + len2
        return 0