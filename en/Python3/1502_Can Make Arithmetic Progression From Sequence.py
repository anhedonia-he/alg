# @algorithm @lc id=1626 lang=python3 
# @title can-make-arithmetic-progression-from-sequence


from en.Python3.mod.preImport import *
# @test([3,5,1])=true
# @test([1,2,4])=false
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        i = 0
        arr.sort()
        gap = arr[i+1] - arr[i]
        for i in range(len(arr)-1):
            if gap != arr[i+1] - arr[i]:
                return False
        return True