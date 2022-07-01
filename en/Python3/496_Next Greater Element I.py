# @algorithm @lc id=496 lang=python3 
# @title next-greater-element-i


from en.Python3.mod.preImport import *
# @test([4,1,2],[1,3,4,2])=[-1,3,-1]
# @test([2,4],[1,2,3,4])=[3,-1]
# @test([1,3,5,2,4],[6,5,4,3,2,1,7])=[7,7,7,7,7]
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in nums1:
            i_index = nums2.index(i)
            for j in range(i_index, len(nums2)):
                if nums2[j] > i:
                    output.append(nums2[j])
                    break
            else:
                output.append(-1)

        return output