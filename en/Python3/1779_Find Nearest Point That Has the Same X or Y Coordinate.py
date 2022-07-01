# @algorithm @lc id=1888 lang=python3 
# @title find-nearest-point-that-has-the-same-x-or-y-coordinate


from en.Python3.mod.preImport import *
# @test(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]])=2
# @test(3,4,[[3,4]])=0
# @test(3,4,[[2,3]])=-1
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        i, j, result, index = 0, 0, -1, 0
        small = float('inf')
        for i in range(len(points)):
            if points[i][j] == x or points[i][j+1] == y:
                if small > abs(x-points[i][j]) + abs(y-points[i][j+1]):
                    small = abs(x-points[i][j]) + abs(y-points[i][j+1])
                    result = i
        return result
