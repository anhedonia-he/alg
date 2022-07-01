# @algorithm @lc id=1693 lang=python3 
# @title sum-of-all-odd-length-subarrays


from re import sub
from en.Python3.mod.preImport import *
# @test([1,4,2,5,3])=58
# @test([1,2])=3
# @test([10,11,12])=66
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)+1, 2):
                result += sum(arr[i:j])

        return result
            