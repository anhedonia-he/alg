# @algorithm @lc id=566 lang=python3 
# @title reshape-the-matrix


from en.Python3.mod.preImport import *
# @test([[1,2],[3,4]],1,4)=[[1,2,3,4]]
# @test([[1,2],[3,4]],2,4)=[[1,2],[3,4]]
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = [mat[row][col] for row in range(rmat) \
                                for col in range(cmat)]
        flatten.reverse()
        reshape = []
        for i in range(len(mat)):
            reshape.append([])
            for j in range(len(mat[0])):
                reshape[i].append(flatten.pop()
                
        return reshape

