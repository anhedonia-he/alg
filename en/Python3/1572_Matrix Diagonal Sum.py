# @algorithm @lc id=1677 lang=python3 
# @title matrix-diagonal-sum


from en.Python3.mod.preImport import *
# @test([[1,2,3],[4,5,6],[7,8,9]])=25
# @test([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])=8
# @test([[5]])=5
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j or i+j==len(mat[0])-1:
                    result += mat[i][j]
        return result